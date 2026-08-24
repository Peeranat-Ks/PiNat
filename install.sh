#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update
sudo apt-get install -y \
  python3 \
  python3-venv \
  python3-pip \
  python3-opencv \
  libopenblas-dev \
  rpicam-apps

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Install completed. Copy .env.example to .env and fill BACKEND_URL + ROBOT_API_KEY."
