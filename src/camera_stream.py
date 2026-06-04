import subprocess
import numpy as np
import cv2


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
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return process, width, height


def read_csi_frame(process, width, height):
    expected_bytes = width * height * 3 // 2
    raw = process.stdout.read(expected_bytes)
    if len(raw) != expected_bytes:
        return None

    yuv = np.frombuffer(raw, dtype=np.uint8)
    frame = cv2.cvtColor(
        yuv.reshape((height * 3 // 2, width)),
        cv2.COLOR_YUV2BGR_I420,
    )
    return frame
