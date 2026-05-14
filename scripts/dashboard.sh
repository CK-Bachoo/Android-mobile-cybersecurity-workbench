#!/bin/bash
while true; do
    clear
    echo "══════════════════════════════════════════════"
    echo "🚀 MCW DASHBOARD - HYBRID CLOUD/MOBILE NODE"
    echo "Time: $(date '+%H:%M:%S')"
    [ -f watchdog.pid ] && ps -p $(cat watchdog.pid 2>/dev/null) > /dev/null 2>&1 && echo "✅ WATCHDOG: RUNNING" || echo "❌ WATCHDOG: DOWN"
    echo "══════════════════════════════════════════════"
    echo "Recent Logs:"
    [ -f ../Vault/Logs/watchdog.json ] && tail -n 5 ../Vault/Logs/watchdog.json
    sleep 10
done
