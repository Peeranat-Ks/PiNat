import os
import time
from datetime import datetime

import cv2

import backend_client
import config
from camera_stream import open_csi_process, read_csi_frame
from detector import PersonDetector
from patrol import PatrolScheduler, within_restricted_hours


class RemoteConfig:
    """Operating parameters pulled from the backend. Local fallback values
    from config.py are used only until the first successful fetch, so the
    robot can still boot (in a safe/default mode) if the network or backend
    is unavailable at startup."""

    def __init__(self):
        self.patrol_start_hour = config.RESTRICTED_HOUR_START
        self.patrol_end_hour = config.RESTRICTED_HOUR_END
        self.always_alert = config.ALWAYS_ALERT
        self.patrol_minutes = config.PATROL_MINUTES
        self.rest_minutes = config.REST_MINUTES
        self.detection_scale = config.DETECTION_SCALE
        self.min_detections_to_alert = config.MIN_DETECTIONS_TO_ALERT
        self.alert_cooldown_seconds = config.ALERT_COOLDOWN_SECONDS

    def apply(self, data: dict):
        self.patrol_start_hour = data["patrol_start_hour"]
        self.patrol_end_hour = data["patrol_end_hour"]
        self.always_alert = data["always_alert"]
        self.patrol_minutes = data["patrol_minutes"]
        self.rest_minutes = data["rest_minutes"]
        self.detection_scale = data["detection_scale"]
        self.min_detections_to_alert = data["min_detections_to_alert"]
        self.alert_cooldown_seconds = data["alert_cooldown_seconds"]


def ensure_dirs():
    os.makedirs("snapshots", exist_ok=True)


def save_snapshot(frame) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"snapshots/person_{ts}.jpg"
    cv2.imwrite(path, frame)
    return path


def main():
    ensure_dirs()

    remote_config = RemoteConfig()
    fetched = backend_client.fetch_config()
    if fetched:
        remote_config.apply(fetched)
    else:
        print("[startup] Backend unreachable; using local fallback config.")

    detector = PersonDetector()
    scheduler = PatrolScheduler(remote_config.patrol_minutes, remote_config.rest_minutes)
    process, width, height = open_csi_process(config.FRAME_WIDTH, config.FRAME_HEIGHT, config.FRAME_FPS)

    last_alert_time = 0.0
    last_config_refresh = time.time()
    last_heartbeat = 0.0

    print("PiNat started. Press q to quit.")

    try:
        while True:
            now = time.time()

            # Periodically re-pull config so admin changes made on the
            # website take effect without redeploying the robot.
            if now - last_config_refresh >= config.CONFIG_REFRESH_SECONDS:
                fetched = backend_client.fetch_config()
                if fetched:
                    remote_config.apply(fetched)
                    scheduler.update_intervals(remote_config.patrol_minutes, remote_config.rest_minutes)
                last_config_refresh = now

            resting = scheduler.tick()

            if now - last_heartbeat >= config.HEARTBEAT_INTERVAL_SECONDS:
                backend_client.send_heartbeat(message="resting" if resting else "patrolling")
                last_heartbeat = now

            frame = read_csi_frame(process, width, height)
            if frame is None:
                continue

            boxes = []
            if not resting:
                boxes, detection_count = detector.detect(frame, remote_config.detection_scale)

                should_alert = (
                    detection_count >= remote_config.min_detections_to_alert
                    and within_restricted_hours(
                        remote_config.patrol_start_hour,
                        remote_config.patrol_end_hour,
                        remote_config.always_alert,
                    )
                    and now - last_alert_time >= remote_config.alert_cooldown_seconds
                )
                if should_alert:
                    image_path = save_snapshot(frame)
                    detected_at_iso = datetime.now().astimezone().isoformat()
                    ok, result = backend_client.upload_detection(image_path, detected_at_iso)
                    print("Detection uploaded" if ok else f"Detection upload failed: {result}")
                    last_alert_time = now

            if config.DISPLAY_PREVIEW:
                for (x, y, w, h) in boxes:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow("PiNat Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        process.terminate()
        process.wait()
        if config.DISPLAY_PREVIEW:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

