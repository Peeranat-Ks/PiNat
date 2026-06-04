#!/usr/bin/env bash
set -euo pipefail

mkdir -p snapshots
OUT="snapshots/cam_test_$(date +%Y%m%d_%H%M%S).jpg"
rpicam-still -o "$OUT" --width 1280 --height 720 --nopreview -t 1200

echo "Saved: $OUT"
