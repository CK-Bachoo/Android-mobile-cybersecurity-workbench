#!/usr/bin/env python3
"""
osint_agent.py — Bunker OSINT Recon Agent
Operator: C.K. Bachoo | NY IF-CS-26 | The Knowledge House
Purpose:  Passive recon — DNS, WHOIS, port probe. No third-party libs.
Usage:    python3 scripts/osint_agent.py <domain_or_ip>
NOTE:     Only run against targets you own or have permission to test.
"""

import os
import re
import socket
import subprocess
import sys
from datetime import datetime

VAULT_DIR = os.path.expanduser(
    '~/Android-mobile-cybersecurity-workbench/Vault/Logs')
DNS_RECORD_TYPES = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME']

def banner(title):
    return f"\n{'─'*50}\n  {title}\n{'─'*50}"

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return result.stdout.strip() or result.stderr.strip() or '(no output)'
    except FileNotFoundError:
        return f"(not found: {cmd[0]} — pkg install dnsutils)"
    except subprocess.TimeoutExpired:
        return '(timed out)'
    except OSError as exc:
        return f'(error: {exc})'

def resolve_hostname(target):
    results = {}
    try:
        addrs = socket.getaddrinfo(target, None)
        results['resolved_ips'] = list({a[4][0] for a in addrs})
    except socket.gaierror as exc:
        results['resolved_ips'] = [f'(failed: {exc})']
    for ip in results.get('resolved_ips', []):
        if not ip.startswith('('):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                results.setdefault('reverse_dns', []).append(f'{ip} → {hostname}')
            except socket.herror:
                results.setdefault('reverse_dns', []).append(f'{ip} → (no PTR)')
    return results

def dns_enum(target):
    return {rtype: run_cmd(['dig', '+short', rtype, target]) for rtype in DNS_RECORD_TYPES}

def whois_lookup(target):
    return run_cmd(['whois', target])

def port_probe(target, ports=None):
    if ports is None:
        ports = [21,22,25,53,80,443,8080,8443,3306,5432]
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return {'error': 'Could not resolve target'}
    results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        try:
            results[port] = 'OPEN' if sock.connect_ex((ip, port)) == 0 else 'CLOSED'
        except OSError:
            results[port] = 'FILTERED'
        finally:
            sock.close()
    return results

def build_report(target):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = ['='*60,
             '  BUNKER OSINT AGENT — Recon Report',
             f'  Target    : {target}',
             f'  Timestamp : {timestamp}',
             f'  Operator  : C.K. Bachoo | NY IF-CS-26',
             '='*60]
    lines.append(banner('1. DNS Resolution'))
    res = resolve_hostname(target)
    lines.append(f"  Resolved IPs : {', '.join(res.get('resolved_ips',[]))}")
    for entry in res.get('reverse_dns', []):
        lines.append(f"  Reverse DNS  : {entry}")
    lines.append(banner('2. DNS Records (dig)'))
    for rtype, value in dns_enum(target).items():
        lines.append(f"  {rtype:<8}: {value}")
    lines.append(banner('3. WHOIS'))
    for l in whois_lookup(target).splitlines()[:30]:
        lines.append(f"  {l}")
    lines.append(banner('4. Port Probe (TCP connect)'))
    ports = port_probe(target)
    if 'error' in ports:
        lines.append(f"  {ports['error']}")
    else:
        open_ports = [str(p) for p,s in ports.items() if s == 'OPEN']
        lines.append(f"  Open: {', '.join(open_ports) if open_ports else 'none'}")
        for port, status in ports.items():
            lines.append(f"  Port {port:<6}: {status}")
    lines += ['\n'+'='*60, '  END OF REPORT', '='*60+'\n']
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/osint_agent.py <domain_or_ip>')
        print('NOTE:  Only test targets you own or have permission to scan.')
        sys.exit(0)
    target = sys.argv[1].strip()
    print(f'\n[OSINT AGENT] Target: {target}')
    print('[OSINT AGENT] Running passive recon (~30 seconds)...\n')
    report = build_report(target)
    print(report)
    try:
        os.makedirs(VAULT_DIR, exist_ok=True)
        safe   = target.replace('.','_').replace('/','_')
        ts     = datetime.now().strftime('%Y%m%d_%H%M%S')
        out    = os.path.join(VAULT_DIR, f'osint_{safe}_{ts}.txt')
        with open(out, 'w') as fh:
            fh.write(report)
        print(f'[OSINT AGENT] Report saved → {out}')
    except OSError as exc:
        print(f'[OSINT AGENT] Could not save: {exc}')

if __name__ == '__main__':
    main()
