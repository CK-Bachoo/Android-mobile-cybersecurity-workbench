#!/usr/bin/env python3
import time, subprocess, os, json, re, gzip, shutil
from datetime import datetime

LOG_FILE = os.path.expanduser("~/Android-mobile-cybersecurity-workbench/Vault/Logs/watchdog.json")
MAX_SIZE = 5 * 1024 * 1024
MAX_BACKUPS = 7

PII_PATTERNS = [
    (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[REDACTED-EMAIL]'),
    (r'\b\d{3}[-.]?\d{2}[-.]?\d{4}\b', '[REDACTED-SSN]'),
    (r'\b\d{16}\b', '[REDACTED-CC]'),
    (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[REDACTED-IP]')
]

def sanitize_pii(text):
    for pattern, repl in PII_PATTERNS:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

def rotate_log():
    dir_path = os.path.dirname(LOG_FILE)
    os.makedirs(dir_path, exist_ok=True)
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_SIZE:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(LOG_FILE, 'rb') as f_in, gzip.open(f"{LOG_FILE}.{ts}.gz", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        open(LOG_FILE, 'w').close()

def log_event(event_type, message, **kwargs):
    try:
        rotate_log()
        entry = {"timestamp": datetime.now().isoformat(), "event": event_type, "message": sanitize_pii(message), **kwargs}
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception: pass

def get_active_interface():
    try:
        res = subprocess.run(["ip", "-o", "-4", "addr", "show"], capture_output=True, text=True)
        for iface in ["tun0", "ppp0", "wg0", "tap0", "wlan0", "eth0"]:
            if any(re.search(rf"^\d+:\s+{iface}\b", line) for line in res.stdout.splitlines()):
                return iface
    except Exception: pass
    return None

def is_healthy(interface):
    if not interface: return False
    try:
        res = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
        return res.returncode == 0 and "state UP" in res.stdout
    except Exception: return False

if __name__ == "__main__":
    log_event("watchdog", "Started - Strict VPN-aware monitoring")
    active_iface = get_active_interface()
    while True:
        if not is_healthy(active_iface):
            if active_iface: os.system(f"ip link set {active_iface} up 2>/dev/null")
        time.sleep(30)
