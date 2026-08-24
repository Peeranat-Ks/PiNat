# PiNat

AI-powered indoor surveillance robot project for Raspberry Pi 4 + Camera Module 3.

This robot is one of three parts of the overall system (`web/backend`, `web/frontend`
admin website, and this robot code). The robot no longer talks to any
messenger platform directly -- it reports to a central backend, which owns
config, detection history, and alert delivery. This makes the project
scalable to many robots across different buildings, all managed from one
admin website.

## Architecture

```
Robot (this project)  <-- poll config, push heartbeat/detections -->  Backend API (web/backend)
                                                                              |
                                                                              v
                                                                    Messenger adapters (Telegram/LINE/...)
                                                                              |
                                                                              v
                                                                    Admin website (web/frontend)
```

- The robot pulls its patrol schedule, patrol/rest interval, and detection
  tuning from the backend via `GET /api/v1/robot/config`.
- The robot sends periodic liveness reports via `POST /api/v1/robot/heartbeat`.
- On detecting a person, the robot uploads the snapshot to
  `POST /api/v1/robot/detections`; the backend stores it, logs the event, and
  sends the messenger alert itself (Telegram/LINE/etc., whichever is
  configured for that robot by an admin).
- Each robot authenticates with its own API key (`ROBOT_API_KEY`), issued
  once by an admin via the website when the robot is created.

## What is included

- Camera capture using `rpicam-vid` (`camera_stream.py`)
- Person detection using OpenCV HOG (`detector.py`)
- Patrol/rest duty cycle and restricted-hours logic (`patrol.py`)
- Backend API client for config/heartbeat/detections (`backend_client.py`)
- Main detection and patrol loop (`main.py`)
- Quick backend connectivity test (`backend_test.py`)
- Install and run helper scripts

## Project structure

- `src/main.py`: Main patrol/detection loop; wires together the camera, detector, scheduler, and backend client
- `src/camera_stream.py`: Camera Module 3 stream helper using `rpicam-vid`
- `src/detector.py`: OpenCV HOG person-detection wrapper
- `src/patrol.py`: Patrol/rest duty cycle and restricted-hours scheduling
- `src/backend_client.py`: HTTP client for the central backend (config pull, heartbeat, detection upload)
- `src/backend_test.py`: Quick script to verify robot -> backend connectivity
- `src/config.py`: Environment configuration loader (backend URL/API key + local fallback defaults)
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

Fill in `.env`:
- `BACKEND_URL`: URL of the deployed `web/backend` (e.g. `https://your-backend.example.com`)
- `ROBOT_API_KEY`: the per-robot API key, obtained from the admin website when the robot is created there (Robots -> Add Robot)

The patrol schedule, patrol/rest interval, and messenger integration are all
configured on the admin website, not in this `.env` file. Local values in
`.env` are only a fallback used if the backend is unreachable at startup.

## Quick tests

```bash
chmod +x scripts/camera_test.sh
./scripts/camera_test.sh
source .venv/bin/activate
python3 src/backend_test.py
```

## Run

```bash
chmod +x run.sh
./run.sh
```

## Notes

- Patrol schedule, interval, detection tuning, and messenger credentials all live on the backend and are pulled by the robot periodically (`CONFIG_REFRESH_SECONDS`).
- Snapshots are saved locally under `snapshots/` and also uploaded to the backend on detection.
- Detection history is retained by the backend for 30 days before automatic purge.

