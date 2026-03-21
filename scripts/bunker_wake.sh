#!/data/data/com.termux/files/usr/bin/bash
echo "⚓ BUNKER WAKE — C.K. Bachoo"
source ~/.bashrc
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt 2>/dev/null)
cd ~/Android-mobile-cybersecurity-workbench
echo "[1/4] Starting X11 server..."
termux-x11 :1 &
sleep 3
echo "[2/4] Starting XFCE desktop..."
DISPLAY=:1 xfce4-session &
sleep 3
echo "[3/4] Opening X11 display..."
am start -n com.termux.x11/.MainActivity 2>/dev/null
sleep 2
echo "[4/4] Starting Jarvis AI..."
python3 scripts/jarvis.py
