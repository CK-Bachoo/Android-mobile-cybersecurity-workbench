#!/usr/bin/env python3
import urllib.request, json, sys, time

def sanitize_target(target):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_")
    return "".join(c for c in target if c in allowed)

def fetch_ip_intel(target):
    target = sanitize_target(target)
    print(f"[*] OSINT sweep: {target}")
    sources = [f"https://ipapi.co/{target}/json/", f"http://ip-api.com/json/{target}"]
    for api in sources:
        try:
            req = urllib.request.Request(api, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode("utf-8"))
                print(f"[✓] Source: {api.split('/')[2]}")
                return data
        except Exception as e:
            print(f"[!] Source failed: {e}")
            time.sleep(1)
    return {"error": "All sources unreachable", "target": target}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 osint_agent.py <IP_OR_DOMAIN>")
        print("Note: Authorized environments only")
        sys.exit(1)
    result = fetch_ip_intel(sys.argv[1])
    print(json.dumps(result, indent=2))
    print("\n[SUMMARY]")
    for key in ["org","country","city","region","isp","asn"]:
        if key in result:
            print(f"  {key.upper()}: {result[key]}")
