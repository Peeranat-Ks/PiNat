import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()

ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", "10"))
RESTRICTED_HOUR_START = int(os.getenv("RESTRICTED_HOUR_START", "22"))
ALWAYS_ALERT = os.getenv("ALWAYS_ALERT", "false").strip().lower() == "true"

FRAME_WIDTH = int(os.getenv("FRAME_WIDTH", "320"))
FRAME_HEIGHT = int(os.getenv("FRAME_HEIGHT", "240"))
FRAME_FPS = int(os.getenv("FRAME_FPS", "20"))

DETECTION_SCALE = float(os.getenv("DETECTION_SCALE", "1.05"))
MIN_DETECTIONS_TO_ALERT = int(os.getenv("MIN_DETECTIONS_TO_ALERT", "1"))

DISPLAY_PREVIEW = os.getenv("DISPLAY_PREVIEW", "false").strip().lower() == "true"
