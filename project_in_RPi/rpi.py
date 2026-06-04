import cv2
import subprocess
import numpy as np
import requests
import time
from config import (
    BOT_TOKEN,
    CHAT_ID,
    ALERT_COOLDOWN_SECONDS,
    CAMERA_SOURCE,
    USB_CAMERA_INDEX,
)


def send_telegram(image_path):
    if not BOT_TOKEN or not CHAT_ID:
        print("Missing BOT_TOKEN or CHAT_ID. Skipping Telegram alert.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(image_path, "rb") as img:
            files = {"photo": img}
            data = {"chat_id": CHAT_ID, "caption": "Person detected"}
            response = requests.post(url, files=files, data=data, timeout=10)
            print("Telegram status:", response.status_code)
    except Exception as e:
        print("Telegram error:", e)

# HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def open_csi_process(width=320, height=240, fps=20):
    cmd = [
        "rpicam-vid",
        "--inline",
        "--nopreview",
        "--width",
        str(width),
        "--height",
        str(height),
        "--framerate",
        str(fps),
        "--codec",
        "yuv420",
        "-t",
        "0",
        "-o",
        "-",
    ]
    return subprocess.Popen(cmd, stdout=subprocess.PIPE), width, height


def read_csi_frame(process, width, height):
    expected_bytes = width * height * 3 // 2
    raw_frame = process.stdout.read(expected_bytes)
    if len(raw_frame) != expected_bytes:
        return None

    yuv = np.frombuffer(raw_frame, dtype=np.uint8)
    return cv2.cvtColor(
        yuv.reshape((height * 3 // 2, width)),
        cv2.COLOR_YUV2BGR_I420,
    )


def open_usb_camera(index=0):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 20)
    return cap


last_sent = 0
process = None
cap = None
mode = None

print("System started. Press q to quit")

try:
    if CAMERA_SOURCE in ("usb", "auto"):
        cap = open_usb_camera(USB_CAMERA_INDEX)
        if cap.isOpened():
            mode = "usb"
            print(f"Using USB webcam at index {USB_CAMERA_INDEX}")
        else:
            cap.release()
            cap = None

    if mode is None and CAMERA_SOURCE in ("csi", "auto"):
        try:
            process, csi_w, csi_h = open_csi_process()
            test_frame = read_csi_frame(process, csi_w, csi_h)
            if test_frame is not None:
                mode = "csi"
                print("Using CSI camera via rpicam-vid")
            else:
                process.terminate()
                process.wait()
                process = None
        except FileNotFoundError:
            process = None

    if mode is None:
        raise RuntimeError(
            "No camera source available. Set CAMERA_SOURCE=usb for /dev/video0 or connect CSI camera."
        )

    while True:
        if mode == "csi":
            frame = read_csi_frame(process, csi_w, csi_h)
            if frame is None:
                print("CSI frame read failed")
                continue
        else:
            ok, frame = cap.read()
            if not ok or frame is None:
                print("USB frame read failed")
                continue

        # Resize for better detection
        small = cv2.resize(frame, (320, 240))

        # Detect people
        boxes, weights = hog.detectMultiScale(
            small,
            winStride=(8, 8),
            padding=(8, 8),
            scale=1.05,
        )

        print("People detected:", len(boxes))

        # Draw and send alert
        if len(boxes) > 0:
            for (x, y, w, h) in boxes:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if time.time() - last_sent > ALERT_COOLDOWN_SECONDS:
                img_path = "person.jpg"
                cv2.imwrite(img_path, frame)
                send_telegram(img_path)
                print("Alert sent")
                last_sent = time.time()

        cv2.imshow("Person Detection", frame)

        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    print("Cleaning up")
    if process is not None:
        process.terminate()
        process.wait()
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
