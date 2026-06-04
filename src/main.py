import os
import time
from datetime import datetime

import cv2

from camera_stream import open_csi_process, read_csi_frame
from config import (
    ALERT_COOLDOWN_SECONDS,
    ALWAYS_ALERT,
    BOT_TOKEN,
    CHAT_ID,
    DETECTION_SCALE,
    DISPLAY_PREVIEW,
    FRAME_FPS,
    FRAME_HEIGHT,
    FRAME_WIDTH,
    MIN_DETECTIONS_TO_ALERT,
    RESTRICTED_HOUR_START,
)
from telegram_alert import send_telegram_photo


def within_restricted_hours():
    if ALWAYS_ALERT:
        return True
    return datetime.now().hour >= RESTRICTED_HOUR_START


def ensure_dirs():
    os.makedirs("snapshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


def save_snapshot(frame):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"snapshots/person_{ts}.jpg"
    cv2.imwrite(path, frame)
    return path


def main():
    ensure_dirs()

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    process, width, height = open_csi_process(FRAME_WIDTH, FRAME_HEIGHT, FRAME_FPS)
    last_alert_time = 0.0

    print("PiNat started. Press q to quit.")

    try:
        while True:
            frame = read_csi_frame(process, width, height)
            if frame is None:
                continue

            boxes, _ = hog.detectMultiScale(
                frame,
                winStride=(8, 8),
                padding=(8, 8),
                scale=DETECTION_SCALE,
            )

            detection_count = len(boxes)
            now = time.time()

            if detection_count >= MIN_DETECTIONS_TO_ALERT and within_restricted_hours():
                if now - last_alert_time >= ALERT_COOLDOWN_SECONDS:
                    image_path = save_snapshot(frame)
                    caption = (
                        f"Person detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    )
                    ok, msg = send_telegram_photo(BOT_TOKEN, CHAT_ID, image_path, caption)
                    print("Alert sent" if ok else f"Alert failed: {msg}")
                    last_alert_time = now

            if DISPLAY_PREVIEW:
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
        if DISPLAY_PREVIEW:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
