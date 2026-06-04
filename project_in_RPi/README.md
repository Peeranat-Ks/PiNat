# Raspberry Pi Person Detection Setup

This folder contains a simple Raspberry Pi person detection script using:
- `rpicam-vid` for camera stream
- OpenCV HOG person detector
- Telegram alert with image snapshot

## Files
- `rpi.py`: main detection script
- `config.py`: environment configuration loader
- `.env.example`: template for secrets and settings
- `requirements.txt`: Python dependencies
- `install.sh`: one-time setup script
- `run.sh`: start script
- `person-detection.service`: optional systemd service for auto start

## 1) Configure environment

```bash
cp .env.example .env
nano .env
```

Set:
- `BOT_TOKEN`
- `CHAT_ID`
- `ALERT_COOLDOWN_SECONDS` (optional)

## 2) Install dependencies

```bash
chmod +x install.sh run.sh
./install.sh
```

If the pip step is interrupted by the network, rerun `./install.sh`. Large wheels such as `numpy` can occasionally fail to download on slower Pi connections.

## 3) Run manually

```bash
./run.sh
```

If the file is not executable on your Pi, use:

```bash
bash run.sh
```

Press `q` to quit.

## 4) Optional: run automatically at boot (systemd)

1. Update paths in `person-detection.service` if your path is different.
2. Install service:

```bash
sudo cp person-detection.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable person-detection.service
sudo systemctl start person-detection.service
```

3. Check logs:

```bash
sudo journalctl -u person-detection.service -f
```
