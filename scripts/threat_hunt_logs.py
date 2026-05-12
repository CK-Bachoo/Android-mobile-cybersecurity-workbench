#!/usr/bin/env python3
"""
threat_hunt_logs.py — Bunker TTP Log Analyzer
Operator: C.K. Bachoo | NY IF-CS-26 | The Knowledge House
Purpose:  Scan access logs for ShinyHunters IoCs and web attack TTPs.
          Read-only — never modifies the source log.
Usage:    python3 scripts/threat_hunt_logs.py [log_file]
"""

import os
import re
import sys
from collections import defaultdict
from datetime import datetime

DEFAULT_LOG = os.path.expanduser(
    '~/Android-mobile-cybersecurity-workbench/Vault/Logs/access.log')
VAULT_DIR = os.path.expanduser(
    '~/Android-mobile-cybersecurity-workbench/Vault/Logs')

IOC_PATTERNS = [
    ('ShinyHunters actor reference',
     re.compile(r'shinyhunters', re.IGNORECASE), 'CRITICAL'),
    ('Canvas exploit path',
     re.compile(r'/login/canvas|free.for.teacher', re.IGNORECASE), 'CRITICAL'),
    ('Canvas credential stuffing',
     re.compile(r'canvas.*(password|passwd|token)', re.IGNORECASE), 'CRITICAL'),
    ('SQL injection UNION SELECT',
     re.compile(r'union\s+select', re.IGNORECASE), 'CRITICAL'),
    ('SQL injection comment',
     re.compile(r'(--|#|/\*)', re.IGNORECASE), 'HIGH'),
    ('SQL time-based blind',
     re.compile(r'sleep\s*\(\s*\d+\s*\)|benchmark\s*\(', re.IGNORECASE), 'CRITICAL'),
    ('Directory traversal',
     re.compile(r'\.\./|\.\.\\|%2e%2e', re.IGNORECASE), 'HIGH'),
    ('Sensitive file probe',
     re.compile(r'(etc/passwd|etc/shadow|\.env|\.git/config|wp-config\.php)',
                re.IGNORECASE), 'CRITICAL'),
    ('Admin panel enum',
     re.compile(r'/(admin|administrator|wp-admin|phpmyadmin)', re.IGNORECASE), 'MEDIUM'),
    ('Command injection',
     re.compile(r';.*(wget|curl|bash|sh|nc|python|perl)', re.IGNORECASE), 'CRITICAL'),
    ('wget/curl exfil beacon',
     re.compile(r'\b(wget|curl)\b', re.IGNORECASE), 'HIGH'),
    ('Scanner User-Agent',
     re.compile(r'(sqlmap|nikto|nmap|masscan|nuclei|dirbuster|gobuster)',
                re.IGNORECASE), 'HIGH'),
    ('Auth brute-force path',
     re.compile(r'/(login|signin|auth|authenticate)', re.IGNORECASE), 'MEDIUM'),
    ('HTTP 401/403 flood',
     re.compile(r'\s(401|403)\s'), 'MEDIUM'),
]

SEVERITY_ORDER = {'CRITICAL':0,'HIGH':1,'MEDIUM':2}

def color(sev):
    return {'CRITICAL':'\033[91m','HIGH':'\033[93m','MEDIUM':'\033[96m'}.get(sev,'')

RESET = '\033[0m'

def scan_log(log_path):
    if not os.path.isfile(log_path):
        print(f"[ERROR] Log not found: {log_path}")
        print("        Create a test log or pass a path as argument.")
        sys.exit(1)
    hits = []
    line_count = 0
    ip_counter = defaultdict(int)
    with open(log_path, 'r', errors='replace') as fh:
        for lineno, line in enumerate(fh, start=1):
            line_count += 1
            stripped = line.rstrip()
            ip_match = re.match(r'^(\d{1,3}(?:\.\d{1,3}){3})', stripped)
            src_ip   = ip_match.group(1) if ip_match else 'unknown'
            seen     = set()
            for label, pattern, severity in IOC_PATTERNS:
                if pattern.search(stripped) and label not in seen:
                    hits.append({'lineno':lineno,'line':stripped,
                                 'label':label,'severity':severity,'src_ip':src_ip})
                    ip_counter[src_ip] += 1
                    seen.add(label)
    hits.sort(key=lambda h: SEVERITY_ORDER.get(h['severity'],9))
    return {'hits':hits,'line_count':line_count,'ip_counter':dict(ip_counter)}

def build_report(log_path, scan):
    hits       = scan['hits']
    line_count = scan['line_count']
    ip_counter = scan['ip_counter']
    timestamp  = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = ['='*60,
             '  BUNKER TTP LOG ANALYZER — Threat Hunt Report',
             f'  Log File  : {log_path}',
             f'  Scanned   : {line_count} lines',
             f'  Timestamp : {timestamp}',
             f'  Operator  : C.K. Bachoo | NY IF-CS-26',
             '='*60]
    if not hits:
        lines.append('\n  [CLEAR] No IoCs detected.')
    else:
        counts = defaultdict(int)
        for h in hits:
            counts[h['severity']] += 1
        lines.append('\n  SUMMARY')
        for sev in ('CRITICAL','HIGH','MEDIUM'):
            if counts[sev]:
                lines.append(f'  {sev:<10}: {counts[sev]} hit(s)')
        lines.append('\n  TOP OFFENDING IPs')
        for ip, count in sorted(ip_counter.items(), key=lambda x:x[1], reverse=True)[:5]:
            lines.append(f'  {ip:<20} {count} hit(s)')
        lines.append('\n  DETAILED HITS')
        for h in hits:
            lines.append(
                f"\n  [{h['severity']}] Line {h['lineno']} | IP: {h['src_ip']}\n"
                f"  IoC   : {h['label']}\n"
                f"  Trace : {h['line'][:100]}{'...' if len(h['line'])>100 else ''}")
        lines.append('\n  RECOMMENDATION')
        if counts.get('CRITICAL',0) > 0:
            lines.append(f"  {counts['CRITICAL']} CRITICAL hit(s). Run air_gap_isolate.py if breach confirmed.")
        else:
            lines.append('  No CRITICAL hits. Review HIGH findings manually.')
    lines += ['\n'+'='*60,'  END OF REPORT','='*60+'\n']
    return '\n'.join(lines)

def main():
    log_path = sys.argv[1] if len(sys.argv) >= 2 else DEFAULT_LOG
    print(f'\n[THREAT HUNT] Target: {log_path}')
    print('[THREAT HUNT] Read-only scan — source file untouched.\n')
    scan   = scan_log(log_path)
    report = build_report(log_path, scan)
    for line in report.splitlines():
        sev = next((s for s in ('CRITICAL','HIGH','MEDIUM') if f'[{s}]' in line), None)
        print(f"{color(sev)}{line}{RESET}" if sev else line)
    try:
        os.makedirs(VAULT_DIR, exist_ok=True)
        ts      = datetime.now().strftime('%Y%m%d_%H%M%S')
        out     = os.path.join(VAULT_DIR, f'threat_hunt_{ts}.txt')
        clean   = re.sub(r'\033\[[0-9;]*m', '', report)
        with open(out, 'w') as fh:
            fh.write(clean)
        print(f'[THREAT HUNT] Report saved → {out}')
    except OSError as exc:
        print(f'[THREAT HUNT] Save failed: {exc}')

if __name__ == '__main__':
    main()
