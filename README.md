# PiNat

AI-powered indoor surveillance robot project for Raspberry Pi 4 + Camera Module 3.

## What is included

- Camera snapshot test with `rpicam-still`
- Telegram alert test script
- Main loop with person detection (OpenCV HOG), alert cooldown, and snapshot logging
- Environment-based configuration
- Install and run helper scripts
- Optional systemd service file

## Project structure

- `src/main.py`: Main detection and alert loop
- `src/camera_stream.py`: Camera Module 3 stream helper using `rpicam-vid`
- `src/telegram_alert.py`: Telegram send-photo helper
- `src/telegram_test.py`: Quick Telegram integration test
- `src/config.py`: Environment configuration loader
- `scripts/camera_test.sh`: One-shot image capture test
- `install.sh`: Install system + Python dependencies on Raspberry Pi
- `run.sh`: Run the main application
- `person-detection.service`: Optional startup service

## Raspberry Pi setup

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-venv python3-pip python3-opencv libopenblas-dev rpicam-apps
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
cp .env.example .env
```

Fill `BOT_TOKEN` and `CHAT_ID` in `.env`.

## Quick tests

```bash
chmod +x scripts/camera_test.sh
./scripts/camera_test.sh
source .venv/bin/activate
python3 src/telegram_test.py
```

## Run

```bash
chmod +x run.sh
./run.sh
```

## Notes

- Default restricted hour start is 22 (10:00 PM).
- Alerts are sent only during restricted hours unless `ALWAYS_ALERT=true`.
- Snapshots are saved under `snapshots/`.
