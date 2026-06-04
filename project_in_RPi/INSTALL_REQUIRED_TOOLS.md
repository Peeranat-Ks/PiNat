# Install Required Tools (Raspberry Pi)

This guide installs every required tool for the person-detection project in `project_in_RPi`.

## 1. Update system packages

```bash
sudo apt-get update
sudo apt-get upgrade -y
```

## 2. Install system tools (camera + Python runtime)

Install these packages:
- `python3`
- `python3-venv`
- `python3-pip`
- `python3-opencv`
- `libopenblas-dev`
- `rpicam-apps`

`libatlas-base-dev` is not available on some current Raspberry Pi OS releases, so this guide uses `libopenblas-dev` instead.

Command:

```bash
sudo apt-get install -y \
  python3 \
  python3-venv \
  python3-pip \
  python3-opencv \
  libopenblas-dev \
  rpicam-apps
```

## 3. Verify camera tool installation

```bash
rpicam-vid --version
```

If this command works, the camera app is installed.

## 4. Create Python virtual environment

Run these commands in the `project_in_RPi` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --retries 10 --timeout 120 --prefer-binary -r requirements.txt
```

## 5. Install Python packages from requirements

`requirements.txt` contains:
- `numpy`
- `requests`
- `python-dotenv`
- `opencv-python`

Install all at once:

```bash
pip install --retries 10 --timeout 120 --prefer-binary -r requirements.txt
```

If the download is interrupted on the Pi, rerun the same command. The larger wheels, especially `numpy`, can fail on an unstable connection.

## 6. Verify Python packages

```bash
python3 -c "import cv2, numpy, requests, dotenv; print('All imports OK')"
```

## 7. Configure Telegram secrets

Create `.env` from template:

```bash
cp .env.example .env
nano .env
```

Set values in `.env`:
- `BOT_TOKEN=...`
- `CHAT_ID=...`
- `ALERT_COOLDOWN_SECONDS=10` (optional)

## 8. Run the project

```bash
./run.sh
```

If `./run.sh` returns `Permission denied`, run it with Bash instead:

```bash
bash run.sh
```

If `run.sh` is not executable:

```bash
chmod +x run.sh
./run.sh
```

## Optional: one-command installer

You can also run the existing script:

```bash
chmod +x install.sh
./install.sh
```

This script performs the same core setup automatically.
