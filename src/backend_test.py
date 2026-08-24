"""Quick connectivity test for the robot -> backend integration.

Usage (from project_in_RPi/ with venv activated and .env configured):
    python3 src/backend_test.py
"""

import glob
from datetime import datetime

import backend_client


def main():
    print("Fetching config...")
    cfg = backend_client.fetch_config()
    if cfg:
        print("Config OK:", cfg)
    else:
        print("Config fetch FAILED (check BACKEND_URL / ROBOT_API_KEY)")

    print("Sending heartbeat...")
    backend_client.send_heartbeat(message="backend_test.py")
    print("Heartbeat sent (check the admin website for last_seen_at update).")

    images = sorted(glob.glob("snapshots/*.jpg"))
    if not images:
        print("No snapshot found in snapshots/. Run scripts/camera_test.sh first to test detection upload.")
        return

    image = images[-1]
    detected_at_iso = datetime.now().astimezone().isoformat()
    ok, result = backend_client.upload_detection(image, detected_at_iso)
    print("Detection upload OK:" if ok else "Detection upload FAILED:", result)


if __name__ == "__main__":
    main()
