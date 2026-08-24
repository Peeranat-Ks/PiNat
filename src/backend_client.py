"""Client for talking to the central web backend (web/backend).

The robot never talks to Telegram/LINE/etc. directly anymore -- it only
pulls its operating config and pushes heartbeats/detections here. The
backend owns messenger delivery, so adding a new messenger platform never
requires a robot-side code change or redeploy.
"""

import requests

import config

_session = requests.Session()
_session.headers.update({"X-API-Key": config.ROBOT_API_KEY})

_TIMEOUT = 10


def fetch_config():
    """Pull the robot's current operating config (patrol schedule, interval,
    detection tuning) from the backend. Returns a dict on success, None on
    failure (caller should keep using the last-known-good config)."""
    try:
        resp = _session.get(f"{config.BACKEND_URL}/api/v1/robot/config", timeout=_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        print(f"[backend] fetch_config failed: {exc}")
        return None


def send_heartbeat(battery_percent=None, zone=None, message=None):
    """Report liveness/status. Best-effort; failures are logged, not raised."""
    payload = {"battery_percent": battery_percent, "zone": zone, "message": message}
    try:
        _session.post(f"{config.BACKEND_URL}/api/v1/robot/heartbeat", json=payload, timeout=_TIMEOUT)
    except requests.RequestException as exc:
        print(f"[backend] heartbeat failed: {exc}")


def upload_detection(image_path, detected_at_iso, zone=None, confidence=None):
    """Upload a detection snapshot. The backend stores it, logs the event,
    and sends the messenger alert itself. Returns (success, message)."""
    data = {"detected_at": detected_at_iso}
    if zone is not None:
        data["zone"] = zone
    if confidence is not None:
        data["confidence"] = confidence

    try:
        with open(image_path, "rb") as photo:
            resp = _session.post(
                f"{config.BACKEND_URL}/api/v1/robot/detections",
                data=data,
                files={"photo": ("snapshot.jpg", photo, "image/jpeg")},
                timeout=20,
            )
        if resp.status_code == 201:
            return True, resp.json()
        return False, f"HTTP {resp.status_code}: {resp.text[:200]}"
    except requests.RequestException as exc:
        return False, str(exc)
