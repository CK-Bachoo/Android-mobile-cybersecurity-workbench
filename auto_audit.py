import nmap
import datetime
import subprocess

def run_audit():
    nm = nmap.PortScanner()
    
    # Phase 1: High Priority (1-1024) - Results in ~30 seconds
    print("Phase 1: Scanning High-Priority Ports (1-1024)...")
    nm.scan('127.0.0.1', '1-1024', arguments='-T4')
    
    with open("audit_log.txt", "a") as f:
        f.write(f"\n--- CORE AUDIT: {datetime.datetime.now()} ---\n")
        if not nm.all_hosts():
            f.write("No active services detected in core range.\n")
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = sorted(nm[host][proto].keys())
                for port in ports:
                    f.write(f"Port: {port}\tState: {nm[host][proto][port]['state']}\n")
    
    print("Phase 1 Complete. Results saved to audit_log.txt.")
    
    # Phase 2: Detached Deep Scan (1025-10000) - Background Only
    print("Phase 2: Launching Deep Scan in background. You are free to move.")
    subprocess.Popen(["nmap", "-T4", "-p", "1025-10000", "127.0.0.1", "-oN", "deep_audit.txt"], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    run_audit()
