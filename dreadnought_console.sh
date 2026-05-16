#!/usr/bin/env bash
while true; do
    clear
    echo "================================================="
    echo " DREADNOUGHT: PURPLE TEAM COMMAND CENTER        "
    echo "================================================="
    echo "1. BLUE: Start Hardware-Agnostic Watchdog"
    echo "2. BLUE: Launch Tactical Radar Console View"
    echo "3. BLUE: Launch Web-Native GodMod3e Dashboard"
    echo "4. RED: Launch Metasploit Framework"
    echo "5. RED: Download & Execute LinPEAS"
    echo "6. RED: Search GTFOBins"
    echo "7. PURPLE: View Legacy Arsenal Scripts"
    echo "8. PURPLE: Sync & Update Code Baseline (Git)"
    echo "9. EXIT"
    echo "================================================="
    read -p "Select Deployment Option: " choice

    case $choice in
        1)
            echo "[*] Igniting Watchdog Sentry..."
            nohup python3 scripts/watchdog_v2.py > /dev/null 2>&1 &
            echo "[+] Watchdog engine initialized in the background."
            sleep 2
            ;;
        2)
            clear
            echo "================================================="
            echo " PROJECT DREADNOUGHT: TACTICAL RADAR CONSOLE VIEW"
            echo "================================================="
            if [ -f "vault/logs/threat_radar.json" ]; then
                tail -n 20 vault/logs/threat_radar.json
            else
                echo "[-] No telemetry data found yet."
            fi
            echo "================================================="
            read -p "Press Enter to return to menu..."
            ;;
        3)
            echo "[*] Booting G0DM0D3 Cockpit..."
            pkill -f dashboard.py
            nohup python3 scripts/dashboard.py > /dev/null 2>&1 &
            echo "[+] GodMod3e UI Grid exposed on http://127.0.0.1:8080"
            sleep 2
            ;;
        8)
            echo "[*] Synchronizing code repositories..."
            git pull origin main
            sleep 2
            ;;
        9)
            echo "[*] Securing station. Exiting."
            exit 0
            ;;
        *)
            echo "[-] Invalid option selection."
            sleep 1
            ;;
    esac
done
