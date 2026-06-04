import requests


def send_telegram_photo(bot_token, chat_id, image_path, caption):
    if not bot_token or not chat_id:
        return False, "Missing BOT_TOKEN or CHAT_ID"

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    try:
        with open(image_path, "rb") as photo:
            response = requests.post(
                url,
                data={"chat_id": chat_id, "caption": caption},
                files={"photo": photo},
                timeout=20,
            )
        if response.status_code == 200:
            return True, "ok"
        return False, f"HTTP {response.status_code}: {response.text[:200]}"
    except Exception as exc:
        return False, str(exc)
