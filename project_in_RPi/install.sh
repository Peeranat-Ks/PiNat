#!/usr/bin/env bash
set -euo pipefail

# Install system dependencies for camera + OpenCV on Raspberry Pi OS.
sudo apt-get update
sudo apt-get install -y \
  python3 \
  python3-venv \
  python3-pip \
  python3-opencv \
  libopenblas-dev \
  rpicam-apps

# Create virtual environment and install Python dependencies.
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --retries 10 --timeout 120 --prefer-binary -r requirements.txt

echo "Installation completed."
