#!/usr/bin/env python3
"""
air_gap_isolate.py — Bunker Trap-Door Air-Gap
Operator: C.K. Bachoo | NY IF-CS-26 | The Knowledge House
Purpose:  Emergency network isolation. Drops interfaces, flushes
          bash_history and git-credentials. README Section XIX.
Usage:    python3 scripts/air_gap_isolate.py [--port PORT] [--ip IP] [--dry-run]
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime

TARGET_INTERFACES = ['wlan0', 'rmnet_data0', 'rmnet_data1', 'rmnet_data2']
SENSITIVE_FILES   = [
    os.path.expanduser('~/.bash_history'),
    os.path.expanduser('~/.git-credentials'),
]
LOG_PATH = os.path.expanduser(
    '~/Android-mobile-cybersecurity-workbench/Vault/Logs/air_gap_incidents.log')

def log(msg, dry_run=False):
    prefix    = '[DRY-RUN] ' if dry_run else ''
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry     = f"[{timestamp}] [AIR-GAP] {prefix}{msg}"
    print(entry)
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, 'a') as fh:
            fh.write(entry + '\n')
    except OSError:
        pass

def drop_interface(iface, dry_run):
    cmd = ['ip', 'link', 'set', iface, 'down']
    log(f"Dropping interface: {iface}", dry_run)
    if dry_run:
        return
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            log(f"Interface {iface} DOWN — success.")
        else:
            log(f"Interface {iface}: {result.stderr.strip()} (root required — logged)")
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        log(f"Interface {iface}: failed — {exc}")

def wipe_file(path, dry_run):
    log(f"Wiping: {path}", dry_run)
    if dry_run:
        return
    if not os.path.isfile(path):
        log(f"  {path} — not found, skipping.")
        return
    try:
        size = os.path.getsize(path)
        with open(path, 'r+b') as fh:
            fh.write(b'\x00' * size)
            fh.truncate(0)
        log(f"  {path} — wiped ({size} bytes zeroed).")
    except OSError as exc:
        log(f"  {path} — wipe failed: {exc}")

def main():
    parser = argparse.ArgumentParser(description='Bunker Trap-Door Air-Gap')
    parser.add_argument('--port',    default='unknown')
    parser.add_argument('--ip',      default='unknown')
    parser.add_argument('--dry-run', action='store_true')
    args    = parser.parse_args()
    dry_run = args.dry_run

    log('=' * 50, dry_run)
    log('TRAP-DOOR AIR-GAP PROTOCOL INITIATED', dry_run)
    log(f'Trigger — Port: {args.port} | IP: {args.ip}', dry_run)
    log('=' * 50, dry_run)
    log('STEP 1: Dropping network interfaces...', dry_run)
    for iface in TARGET_INTERFACES:
        drop_interface(iface, dry_run)
    log('STEP 2: Flushing volatile credentials...', dry_run)
    for path in SENSITIVE_FILES:
        wipe_file(path, dry_run)
    log('STEP 3: Isolation complete.', dry_run)
    log('To restore Wi-Fi: toggle Airplane Mode off/on', dry_run)
    log('=' * 50, dry_run)
    if dry_run:
        print('\n[DRY-RUN COMPLETE] No actual changes made.')

if __name__ == '__main__':
    main()
