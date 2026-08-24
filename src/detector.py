"""Human detection wrapper around OpenCV's HOG people detector.

Kept as a small, isolated module so the detection algorithm can be swapped
out (e.g. for a lightweight deep-learning model) without touching the patrol
loop or backend integration in main.py.
"""

import cv2


class PersonDetector:
    def __init__(self):
        self._hog = cv2.HOGDescriptor()
        self._hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame, detection_scale: float):
        """Returns (boxes, count) of detected people in the frame."""
        boxes, _weights = self._hog.detectMultiScale(
            frame,
            winStride=(8, 8),
            padding=(8, 8),
            scale=detection_scale,
        )
        return boxes, len(boxes)
