#!/usr/bin/env bash
set -euo pipefail

[ -z "${1:-}" ] && echo "Usage: $0 <logfile>" && exit 1
LOGFILE="$1"
OUTDIR="logs"
mkdir -p "$OUTDIR"
OUTFILE="${OUTDIR}/mitre_tagged_$(date +%Y%m%d_%H%M%S).log"

echo "[*] MITRE ATT&CK Tagger | Input: ${LOGFILE}"
{
    echo "# MITRE ATT&CK TAGGED LOG"
    echo "# Operator: C.K. Bachoo | NY IF-CS-26"
    echo "TIMESTAMP: $(date -u)"
    echo "SOURCE: ${LOGFILE}"
    echo "---"
} > "$OUTFILE"

TAGGED=0; TOTAL=0
while IFS= read -r line; do
    TOTAL=$((TOTAL+1)); TAG=""
    echo "$line" | grep -qi "failed.*login\|invalid.*password\|auth.*fail" && TAG="T1110-Brute-Force"
    echo "$line" | grep -qi "cmd.exe\|powershell\|/bin/sh\|exec\|spawn" && TAG="T1059-Command-Interpreter"
    echo "$line" | grep -qi "port.*scan\|nmap\|masscan" && TAG="T1046-Network-Discovery"
    echo "$line" | grep -qi "wget\|curl.*download\|base64" && TAG="T1105-Ingress-Tool-Transfer"
    echo "$line" | grep -qi "crontab\|systemd\|rc.local\|autorun" && TAG="T1053-Scheduled-Task"
    echo "$line" | grep -qi "sudo\|privilege\|escalat\|SUID" && TAG="T1548-Elevation-Control"
    echo "$line" | grep -qi "exfil\|ftp.*out\|scp.*remote" && TAG="T1048-Exfiltration"
    echo "$line" | grep -qi "dns.*query\|nslookup\|resolv" && TAG="T1071.004-DNS-Protocol"
    echo "$line" | grep -qi "lateral\|psexec\|smb\|rdp" && TAG="T1021-Remote-Services"
    echo "$line" | grep -qi "delete.*log\|clear.*history\|wipe" && TAG="T1070-Indicator-Removal"
    if [ -n "$TAG" ]; then
        echo "[MITRE:${TAG}] ${line}" >> "$OUTFILE"
        TAGGED=$((TAGGED+1))
    else
        echo "[UNTAGGED] ${line}" >> "$OUTFILE"
    fi
done < "$LOGFILE"

echo "[✓] Tagged: ${TAGGED}/${TOTAL} | Output: ${OUTFILE}"
