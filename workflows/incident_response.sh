#!/usr/bin/env bash
set -euo pipefail

[ -z "${1:-}" ] && echo "Usage: $0 <incident_id>" && exit 1
ID="$1"
OUTDIR="logs/incident_${ID}"
mkdir -p "$OUTDIR"

echo "[*] DFIR for ${ID} started"
{
    echo "DFIR Report | Incident: ${ID} | $(date -u)"
    echo "============================="
    echo "RUNNING PROCESSES:"
    ps aux
    echo ""
    echo "NETWORK CONNECTIONS:"
    ss -tulnp 2>/dev/null || netstat -tulnp 2>/dev/null || true
    echo ""
    echo "DISK USAGE:"
    df -h
    echo ""
    echo "RECENT LOG FILES:"
    ls -lt logs/ 2>/dev/null | head -20
} > "${OUTDIR}/dfir_report.log"

echo "[✓] DFIR complete -> ${OUTDIR}/dfir_report.log"
