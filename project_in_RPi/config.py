import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")

CAMERA_SOURCE = os.getenv("CAMERA_SOURCE", "auto").strip().lower()

try:
    USB_CAMERA_INDEX = int(os.getenv("USB_CAMERA_INDEX", "0"))
except ValueError:
    USB_CAMERA_INDEX = 0

try:
    ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", "10"))
except ValueError:
    ALERT_COOLDOWN_SECONDS = 10
