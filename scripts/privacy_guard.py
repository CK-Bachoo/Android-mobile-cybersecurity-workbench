#!/usr/bin/env python3
"""
privacy_guard.py — Bunker PII Scrubber
Operator: C.K. Bachoo | NY IF-CS-26 | The Knowledge House
Purpose:  Scrub Student IDs, names, and PII from outgoing logs
          before pushing to GitHub. Documented in README Section XIX.
Usage:    python3 scripts/privacy_guard.py <input_file> [output_file]
"""

import re
import sys
import os
from datetime import datetime

PII_PATTERNS = [
    (re.compile(r'\b\d{6,10}\b'), '[REDACTED-ID]'),
    (re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'), '[REDACTED-EMAIL]'),
    (re.compile(r'Bearer\s+[A-Za-z0-9\-._~+/]+=*', re.IGNORECASE), 'Bearer [REDACTED-TOKEN]'),
    (re.compile(r'token[=:\s]+[A-Za-z0-9\-._~+/]{20,}', re.IGNORECASE), 'token=[REDACTED-TOKEN]'),
    (re.compile(r'ghp_[A-Za-z0-9]{36}'), '[REDACTED-PAT]'),
    (re.compile(r'AIza[A-Za-z0-9\-_]{35}'), '[REDACTED-GEMINI-KEY]'),
    (re.compile(r'\b(\+1[\s\-.]?)?\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}\b'), '[REDACTED-PHONE]'),
    (re.compile(
        r'\b(?!127\.|10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)'
        r'(?:\d{1,3}\.){3}\d{1,3}\b'
    ), '[REDACTED-IP]'),
]

def scrub_line(line):
    for pattern, replacement in PII_PATTERNS:
        line = pattern.sub(replacement, line)
    return line

def scrub_file(input_path):
    if not os.path.isfile(input_path):
        print(f"[ERROR] File not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    clean_lines = []
    hits = 0
    with open(input_path, 'r', errors='replace') as fh:
        for lineno, line in enumerate(fh, start=1):
            scrubbed = scrub_line(line)
            if scrubbed != line:
                hits += 1
                print(f"  [SCRUBBED] Line {lineno}: PII removed", file=sys.stderr)
            clean_lines.append(scrubbed)
    print(f"\n[PRIVACY GUARD] Scan complete — {hits} line(s) scrubbed.", file=sys.stderr)
    return clean_lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/privacy_guard.py <input_file> [output_file]")
        sys.exit(0)
    input_path  = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) >= 3 else None
    print(f"\n[PRIVACY GUARD] Starting PII sweep — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[PRIVACY GUARD] Target: {input_path}\n", file=sys.stderr)
    clean_lines = scrub_file(input_path)
    if output_path:
        with open(output_path, 'w') as fh:
            fh.writelines(clean_lines)
        print(f"[PRIVACY GUARD] Clean file written → {output_path}", file=sys.stderr)
    else:
        sys.stdout.writelines(clean_lines)

if __name__ == '__main__':
    main()
