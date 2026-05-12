#!/bin/bash
# =============================================
# BUNKER AUDIT v2.8 - NIST + Android Hardening
# =============================================

echo -e "\033[1;34m🔒 BUNKER AUDIT v2.8 - Mobile Cybersecurity Workbench\033[0m"
echo "Started: $(date)"
echo "========================================"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check() {
    echo -e "\( {YELLOW}[CHECK] \){NC} $1"
}

pass() { echo -e "\( {GREEN}[PASS] \){NC} $1"; }
warn() { echo -e "\( {YELLOW}[WARN] \){NC} $1"; }
fail() { echo -e "\( {RED}[FAIL] \){NC} $1"; }

# 1. Basic System Info
check "System Information"
echo "Device: $(getprop ro.product.model 2>/dev/null || echo 'N/A')"
echo "Android Version: $(getprop ro.build.version.release 2>/dev/null || echo 'N/A')"
echo "Kernel: $(uname -r)"
echo "User: $USER"

# 2. Root / Privilege Check
check "Root / SELinux Status"
if command -v su >/dev/null 2>&1; then
    warn "Root access (su) is available"
else
    pass "No su binary found"
fi

# 3. Network & Connectivity
check "Network Interfaces"
ip addr show 2>/dev/null | grep -E "inet " | awk '{print $2}' || echo "No ip command output"

check "Listening Ports"
(netstat -tuln 2>/dev/null || ss -tuln 2>/dev/null) || echo "No network tools available"

# 4. Security Features
check "Developer Options & USB Debugging"
settings get global adb_enabled 2>/dev/null || echo "N/A"

check "Unknown Sources"
settings get secure install_non_market_apps 2>/dev/null || echo "N/A"

# 5. File System Permissions
check "Sensitive Directories Permissions"
ls -ld /sdcard /data /system 2>/dev/null || echo "Limited access (normal in Termux)"

# 6. Running Processes
check "Top Running Processes"
ps -ef | head -n 15

echo -e "\n\033[1;32m✅ Audit completed at $(date)\033[0m"
echo "Recommendation: Review output and run individual hardening scripts."
