#!/usr/bin/env bash
echo "[*] Purging zombie processes..."
pkill -f watchdog_v2.py
pkill -f dashboard.py
sleep 1
echo "[*] Igniting Watchdog Sentry..."
nohup python3 scripts/watchdog_v2.py > /dev/null 2>&1 &
echo "[*] Booting G0DM0D3 Cockpit..."
nohup python3 scripts/dashboard.py > /dev/null 2>&1 &
echo "[+] Matrix online. Connect viewport to http://127.0.0.1:8080"
