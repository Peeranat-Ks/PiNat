import os
from dotenv import load_dotenv


load_dotenv()

# Backend API (web/backend) that this robot reports to and pulls its
# operating config from. Each robot has its own API key issued by an admin
# via the management website (Robots -> Create -> shows key once).
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")
ROBOT_API_KEY = os.getenv("ROBOT_API_KEY", "").strip()

# How often the robot re-pulls its config and sends a heartbeat, in seconds.
CONFIG_REFRESH_SECONDS = int(os.getenv("CONFIG_REFRESH_SECONDS", "60"))
HEARTBEAT_INTERVAL_SECONDS = int(os.getenv("HEARTBEAT_INTERVAL_SECONDS", "60"))

# Local fallback values, used only if the backend is unreachable at startup
# (e.g. first boot with no network yet). Once a config is successfully
# fetched, these are overridden by the backend's values.
ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", "10"))
RESTRICTED_HOUR_START = int(os.getenv("RESTRICTED_HOUR_START", "22"))
RESTRICTED_HOUR_END = int(os.getenv("RESTRICTED_HOUR_END", "6"))
ALWAYS_ALERT = os.getenv("ALWAYS_ALERT", "false").strip().lower() == "true"
PATROL_MINUTES = int(os.getenv("PATROL_MINUTES", "30"))
REST_MINUTES = int(os.getenv("REST_MINUTES", "30"))

FRAME_WIDTH = int(os.getenv("FRAME_WIDTH", "320"))
FRAME_HEIGHT = int(os.getenv("FRAME_HEIGHT", "240"))
FRAME_FPS = int(os.getenv("FRAME_FPS", "20"))

DETECTION_SCALE = float(os.getenv("DETECTION_SCALE", "1.05"))
MIN_DETECTIONS_TO_ALERT = int(os.getenv("MIN_DETECTIONS_TO_ALERT", "1"))

DISPLAY_PREVIEW = os.getenv("DISPLAY_PREVIEW", "false").strip().lower() == "true"

