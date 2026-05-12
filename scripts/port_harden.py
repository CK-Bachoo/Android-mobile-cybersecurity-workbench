#!/usr/bin/env python3
"""
port_harden.py — Bunker Port Sentry
Operator: C.K. Bachoo | NY IF-CS-26 | The Knowledge House
Purpose:  Monitor Port 8022 (SSH) and Port 8080 (AI Server) for
          unauthorized IP bindings. Triggers air_gap_isolate.py on detection.
          Documented in README Section XIX.
Usage:    python3 scripts/port_harden.py
"""

import os
import re
import subprocess
import sys
import time
from datetime import datetime

WATCHED_PORTS  = [8022, 8080]
ALLOWED_IPS    = {'127.0.0.1', '::1', '0.0.0.0'}
POLL_INTERVAL  = 15
SCRIPT_DIR     = os.path.dirname(os.path.abspath(__file__))
AIR_GAP_SCRIPT = os.path.join(SCRIPT_DIR, 'air_gap_isolate.py')
LOG_PATH       = os.path.expanduser(
    '~/Android-mobile-cybersecurity-workbench/Vault/Logs/port_sentry.log')

def log(msg, level='INFO'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] [{level}] {msg}"
    print(entry)
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, 'a') as fh:
            fh.write(entry + '\n')
    except OSError:
        pass

def get_listening_sockets():
    results = []
    try:
        raw = subprocess.check_output(['ss', '-tuln'], stderr=subprocess.DEVNULL, text=True)
        for line in raw.splitlines()[1:]:
            parts = line.split()
            if len(parts) < 5:
                continue
            local = parts[4]
            match = re.match(r'[\[\]]*([^:\]]+)\]*:(\d+)$', local)
            if match:
                results.append({'ip': match.group(1), 'port': int(match.group(2))})
    except (FileNotFoundError, subprocess.CalledProcessError):
        try:
            raw = subprocess.check_output(['netstat', '-tuln'], stderr=subprocess.DEVNULL, text=True)
            for line in raw.splitlines():
                parts = line.split()
                if len(parts) < 4 or parts[0] not in ('tcp','tcp6','udp','udp6'):
                    continue
                local = parts[3]
                match = re.match(r'[\[\]]*([^:\]]+)\]*:(\d+)$', local)
                if match:
                    results.append({'ip': match.group(1), 'port': int(match.group(2))})
        except (FileNotFoundError, subprocess.CalledProcessError):
            log('Neither ss nor netstat found. Run: pkg install net-tools', 'WARN')
    return results

def trigger_air_gap(port, offending_ip):
    log(f'UNAUTHORIZED BINDING — Port {port} from IP {offending_ip}', 'CRITICAL')
    log('Triggering Trap-Door Air-Gap...', 'CRITICAL')
    if os.path.isfile(AIR_GAP_SCRIPT):
        try:
            subprocess.Popen([sys.executable, AIR_GAP_SCRIPT,
                              '--port', str(port), '--ip', offending_ip], close_fds=True)
            log('air_gap_isolate.py launched.', 'CRITICAL')
        except OSError as exc:
            log(f'Failed to launch air_gap_isolate.py: {exc}', 'ERROR')
    else:
        log(f'air_gap_isolate.py not found — manual isolation required!', 'ERROR')

def main():
    log('Port Sentry online.')
    log(f'Watching: {WATCHED_PORTS} | Allowed IPs: {ALLOWED_IPS}')
    log(f'Poll interval: {POLL_INTERVAL}s | CTRL+C to stop.\n')
    try:
        while True:
            for sock in get_listening_sockets():
                if sock['port'] in WATCHED_PORTS:
                    if sock['ip'] not in ALLOWED_IPS:
                        trigger_air_gap(sock['port'], sock['ip'])
                    else:
                        log(f"Port {sock['port']} — OK ({sock['ip']})")
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        log('Port Sentry stopped by operator.')

if __name__ == '__main__':
    main()
