import glob
from datetime import datetime

from config import BOT_TOKEN, CHAT_ID
from telegram_alert import send_telegram_photo


images = sorted(glob.glob("snapshots/*.jpg"))
if not images:
    raise SystemExit("No snapshot found in snapshots/. Run scripts/camera_test.sh first.")

image = images[-1]
caption = f"PiNat test alert {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
ok, msg = send_telegram_photo(BOT_TOKEN, CHAT_ID, image, caption)

print("Success:" if ok else "Failed:", msg)
