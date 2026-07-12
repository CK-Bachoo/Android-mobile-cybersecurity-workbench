#!/usr/bin/env bash
set -euo pipefail

[ -z "${1:-}" ] && echo "Usage: $0 <target_ip>" && exit 1
TARGET="$1"
OUTDIR="logs/ctf_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTDIR"

echo "========================================================="
echo "[*] CTF RECON | Target: ${TARGET}"
echo "[*] AUTHORIZED CTF/LAB ENVIRONMENTS ONLY"
echo "========================================================="

python3 workflows/osint_agent.py "$TARGET" > "${OUTDIR}/osint.json" 2>&1 || true
echo "[✓] OSINT complete"

{
    echo "Target: ${TARGET} | $(date -u)"
    command -v nslookup &>/dev/null && nslookup "$TARGET" 2>/dev/null || true
    command -v dig &>/dev/null && dig "$TARGET" 2>/dev/null || true
} > "${OUTDIR}/dns_recon.txt" 2>&1
echo "[✓] DNS complete"

if command -v nmap &>/dev/null; then
    nmap -sV --top-ports 100 -T4 "$TARGET" -oN "${OUTDIR}/nmap_scan.txt" 2>/dev/null || true
    echo "[✓] Nmap complete"
else
    for port in 22 80 443 8080 3306 5432; do
        timeout 2 bash -c "echo >/dev/tcp/${TARGET}/${port}" 2>/dev/null && echo "OPEN: ${port}" || echo "CLOSED: ${port}"
    done > "${OUTDIR}/port_check.txt" 2>&1
fi

cat > "${OUTDIR}/SUMMARY.md" << SUMEOF
# CTF Recon Report
Target: ${TARGET}
Operator: C.K. Bachoo | NY IF-CS-26
Timestamp: $(date -u)
Environment: Authorized CTF/Lab Only
Legal: Unauthorized access is illegal and was not conducted.
SUMEOF

echo "[✓] CTF recon complete -> ${OUTDIR}/"
