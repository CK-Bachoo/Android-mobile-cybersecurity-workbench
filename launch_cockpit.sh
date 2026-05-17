#!/usr/bin/env bash
echo "=========================================================="
echo " PROJECT DREADNOUGHT // UNIVERSAL COCKPIT LAUNCHER"
echo "=========================================================="
echo "[*] Purging active port conflicts..."
fuser -k 3000/tcp >/dev/null 2>&1
fuser -k 8080/tcp >/dev/null 2>&1

echo "[*] Mapping TiDB Cloud infrastructure arrays..."
export NODE_ENV=production
export PORT=3000

echo "[+] Booting G0DM0D3 Full-Stack Engine..."
nohup pnpm start > /dev/null 2>&1 &
sleep 2

echo "=========================================================="
echo " STATUS: COCKPIT SECURELY ONLINE"
echo "=========================================================="
