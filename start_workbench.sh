#!/usr/bin/env bash
echo "=== INITIALIZING GODMOD3 // ORIGINAL COCKPIT LAYOUT ==="
pkill -9 -f "dashboard_v2.py"
pkill -9 -f "streamlit"
pkill -9 -f "ttyd"
kill -9 $(lsof -t -i:8081) 2>/dev/null
sleep 1
python3 /data/data/com.termux/files/home/Project-Dreadnought/scripts/dashboard_v2.py
