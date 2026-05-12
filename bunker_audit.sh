#!/bin/bash
# BUNKER MOBILE AUDIT ENGINE v1.0
# Operator : C.K. Bachoo | NY IF-CS-26 | The Knowledge House
# Purpose  : NIST CSF 2.0 compliance check
# Usage    : bash bunker_audit.sh

VAULT_DIR="$HOME/Android-mobile-cybersecurity-workbench/Vault/Logs"
LOG_FILE="$VAULT_DIR/audit_$(date '+%Y%m%d_%H%M%S').txt"
mkdir -p "$VAULT_DIR"

log() {
    echo -e "$1"
    echo -e "$1" | sed 's/\x1b\[[0-9;]*m//g' >> "$LOG_FILE" 2>/dev/null
}

log "--- [BUNKER MOBILE AUDIT ENGINE v1.0] ---"
log "STATUS: NIST CSF COMPLIANCE CHECK"
log "Timestamp : $(date '+%Y-%m-%d %H:%M:%S')"
log "Operator  : C.K. Bachoo | NY IF-CS-26"
log "----------------------------------------"

log "[ID.1] Checking Root Status..."
if [ -f "/system/xbin/su" ] || [ -f "/system/bin/su" ] || [ -f "/sbin/su" ]; then
    log "  > su binary detected. Compliance: WARNING."
else
    log "  > Device is Not Rooted. Compliance: PASS."
fi

log "[PR.AC] Checking ADB Status..."
ADB_STATUS=""
if command -v getprop >/dev/null 2>&1; then
    ADB_STATUS=$(getprop init.svc.adbd 2>/dev/null)
fi
if [ "$ADB_STATUS" = "running" ]; then
    log "  > ADB Daemon: RUNNING — WARNING open attack surface"
else
    log "  > ADB Daemon: stopped"
fi

log "[PR.IP] Checking VPN / Network Isolation..."
if ip link show 2>/dev/null | grep -qE 'tun|ppp'; then
    log "  > Tunnel interface detected (VPN active). PASS."
else
    log "  > No tunnel interface found. VPN may be inactive. WARNING."
fi

log "[PR.DS] Checking Vault OPSEC..."
GITIGNORE="$HOME/Android-mobile-cybersecurity-workbench/.gitignore"
if [ -f "$GITIGNORE" ] && grep -q "Vault/" "$GITIGNORE"; then
    log "  > Vault/ in .gitignore. PASS."
else
    log "  > Vault/ NOT in .gitignore. FAIL."
fi

log "[DE.CM] Scanning Active Processes..."
log "  PID TTY          TIME CMD"
ps -o pid,tname,time,comm 2>/dev/null | head -n 4 | tail -n 3 | \
    while read -r line; do log "  $line"; done

log "[RS.MI] Checking Automation Scripts..."
SCRIPT_DIR="$HOME/Android-mobile-cybersecurity-workbench/scripts"
for script in privacy_guard.py port_harden.py air_gap_isolate.py osint_agent.py threat_hunt_logs.py; do
    if [ -f "$SCRIPT_DIR/$script" ]; then
        log "  > $script — PASS"
    else
        log "  > $script — NOT FOUND — FAIL"
    fi
done

log "----------------------------------------"
log "AUDIT COMPLETE. STANDING BY FOR UPLOAD."
log "Report: $LOG_FILE"
