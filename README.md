🛡️ Android Mobile Cybersecurity Workbench (The Bunker)
Mobile-first Purple Team automation lab engineered for ARM64 Android environments (Samsung Galaxy Note 20 Ultra + Termux).

This repository stands as living proof that enterprise-grade security operations, proactive threat hunting, defensive automation, and zero-trust AI orchestration can execute flawlessly on constrained mobile hardware. Built on the core philosophy that the mission does not wait for better equipment, this workbench bypasses standard x86 hypervisor limitations by leveraging native Linux sub-systems and remote cloud-bridge infrastructure.

Status Version Platform

Current Role: Cybersecurity Innovation Fellow — The Knowledge House NY (IF-CS-26)
Operator: C.K. Bachoo | Navy Veteran

📋 Table of Contents
Executive Summary & Philosophy
Architectural Paradigm: Desktop vs. Mobile
v2.8 Release Highlights & Automation Suite
Hardware & Deployment Stack
GodMode AI Orchestration & Local Fallback
Zero Trust & OPSEC Protocols
Quick Start
Tactical Phases (Canvas Aligned)
Hardware Benchmarking: MiroFish Swarm
Infrastructure as Code & Desktop Rendering
Historical Specs & Base Initialization
Threat Intelligence Log: Aeternum C2
Forensic Mission Report: DNS Sabotage / OOB Recovery
Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense
Executive Summary & Philosophy
When standard computing infrastructure fails or is unavailable, security operations must maintain continuity. Following a total system hardware failure (Black Screen of Death on a legacy 2011 MacBook Pro), this entire workbench was pivoted to a mobile-native architecture. Operating under a disciplined, stoic framework, the Bunker strips away resource-heavy graphical user interfaces (GUIs) in favor of raw command-line interface (CLI) execution, Python-driven automation, and secure API routing.

Every script and protocol in this repository is designed to execute with maximum efficiency, zero third-party dependencies where possible, and strict adherence to NIST Cybersecurity Framework compliance.

Architectural Paradigm: Desktop vs. Mobile
Standard cybersecurity curriculum relies heavily on x86 architecture and Type-2 hypervisors (VirtualBox, VMware). To achieve the same learning and operational objectives on an ARM64 mobile device without rooting the kernel (triggering Samsung Knox hardware trips), tactical workarounds are deployed.

Operational Requirement	Standard Desktop User (x86)	Android Cyber Workbench (Note 20 Ultra)
Execution Environment	Heavy Local VirtualBox VMs	Ephemeral Google Cloud Shell Bridge / Termux PRoot
Network Isolation	Local VM Subnets	Direct Docker Subnet Routing / VPN Tunneling
Privilege Escalation	Standard sudo binary abuse	Native Headless Binary Exploitation (GTFOBins)
Graphical Rendering	Native Desktop GUI (GNOME/KDE)	Termux-X11 / VirGL Hardware Acceleration
Artifact Synchronization	Native Desktop IDE	Termux Git CLI ➔ GitHub
Technical Analysis: By utilizing Google Cloud Shell and GitHub Codespaces as a remote compute layer, enterprise-grade containers are orchestrated directly from the mobile terminal. This Mobile-to-Cloud Bridge offloads thermal strain and compute risks to an isolated sandbox, preserving the integrity of the local mobile device while establishing a secure, encrypted command and control pipeline.

v2.8 Release Highlights & Automation Suite
All Python automation scripts are built with zero third-party dependencies (utilizing only the Python Standard Library) to prevent RAM spikes, avoid dependency conflicts, and eliminate Android Signal 9 (Out of Memory) kernel kills on the Exynos 990 processor.

bunker_audit.sh — The core NIST-style mobile security audit engine. Verifies root status, ADB daemon state, VPN tunnel interfaces, active listening ports, and ensures the automation script arsenal is fully intact. Outputs severity-sorted, color-coded terminal reports.
The Python Arsenal (scripts/ directory)
Script	Operational Purpose	Technical Mechanism
privacy_guard.py	Pre-Commit Data Sanitization	Automatically scrubs PII, secrets, API keys, and public IP addresses from logs before Git pushes. Whitelists safe private ranges (127.x, 10.x).
port_harden.py	Continuous Port Sentry	Polls local network states every 15 seconds. Monitors Port 8022 (SSH) and 8080 (AI Server). Any unauthorized external IP binding triggers immediate isolation.
air_gap_isolate.py	Trap-Door Emergency Isolation	Triggered by the port sentry. Instantly drops wlan0 and rmnet_data* interfaces via ip link set down, zeroes out ~/.bash_history, and flushes volatile memory to lock out intruders.
osint_agent.py	Passive Reconnaissance	Performs DNS resolution, multi-record dig enumeration (A/AAAA/MX/TXT/NS), WHOIS lookups, and TCP connect probes without requiring nmap or root access.
threat_hunt_logs.py	TTP & IoC Log Analyzer	Scans access logs against 18 specific Indicators of Compromise (IoC) patterns, including SQL injection, directory traversal, and command injection.
Hardware & Deployment Stack
Primary Device: Samsung Galaxy Note 20 Ultra 5G
Compute Specs: Exynos 990, 12GB LPDDR5 RAM, 256GB Internal Storage + High-Speed MicroSD Vault
Operating Environment: Termux + PRoot-Distro (Kali/Ubuntu) + Termux-X11
Cloud Bridge: Google Cloud Shell, GitHub Codespaces, AWS (us-east-2) for serverless offloading.
GodMode AI Orchestration & Local Fallback
The Bunker integrates advanced AI orchestration while strictly maintaining a Zero Trust security posture.

GodMode Web Wrapper: Deploys a unified, lightweight interface for concurrent access to Claude, Gemini, and ChatGPT. By serving the UI locally over a native Python HTTP server (python -m http.server 8000), it bypasses standard Android browser memory limits and prevents the OS from crashing under heavy NodeJS/npm dependencies.
MCP Security (Model Context Protocol): To prevent "God-Mode" privilege escalation (e.g., tool poisoning), all agentic MCP tools are strictly sandboxed. Client-Side Validation strips Prompt Injection vectors, and agents are restricted to read-only access for critical log directories.
Local Fallback (Ollama + Gemma 2B): When operating in highly sensitive environments or during network degradation, the workbench relies on 100% local, offline inference. This allows for the autonomous parsing of sensitive telemetry without leaking proprietary data to cloud providers. (Note: Ollama requires dedicated RAM allocation and is never run simultaneously with the X11 GUI to maintain thermal safety).
Zero Trust & OPSEC Protocols
Vault Isolation: Sensitive data (scans, PCAPs, raw logs) is stored in the Vault/ directory. This directory is strictly excluded via .gitignore and is physically mapped to the encrypted MicroSD card.
VPN Kill Switch: Layer 3 traffic isolation is enforced via Android's "Block connections without VPN" kernel setting. The Termux terminal operates as a "Ghost," preventing local network eavesdropping on SSH sessions or payload deliveries.
Immutable Ledger: Every session artifact is staged, scrubbed by privacy_guard.py, committed with descriptive operational messages, and pushed to this repository to create a cryptographically hashed, timestamped forensic ledger of all operations.
🚀 Quick Start
To deploy the audit engine and verify the integrity of the local environment:

# Navigate to the workbench root
cd ~/Android-mobile-cybersecurity-workbench

# Grant execution permissions to the Python suite and bash engine
chmod 700 scripts/*.py && chmod +x bunker_audit.sh

# Execute the primary system diagnostic
bash bunker_audit.sh

# Optional: Run a passive OSINT sweep on an authorized domain
python3 scripts/osint_agent.py example.com
01 / Tactical Phases (Canvas Aligned)
Phase 0: System Foundations (S01 - S03)
CTI & Navigation: Linux Scavenger Hunt & Access Control Hardening (harden.sh). Mastered the Filesystem Hierarchy Standard (FHS) to locate and extract hidden tokens from /var/tmp/.blackout/.
Permissions: Applied the Read-Write-Execute (RWX) matrix (700 for private, 755 for scripts, 644 for standard files).
Text Plumbing: Advanced log filtering using Grep, Sed, and Awk. Extracted top malicious IP addresses from a 10,000-line Apache access.log using standard streams.
Phase 1: Network & Protocol Defense (S04 - S06)
Operation Broken Link (L1-L3): Restored Layer 3 connectivity by diagnosing a missing default route and manually rebuilding the routing table (sudo ip route add default via 10.0.0.1).
Operation Grid Lock (Subnetting Crucible): Bypassed isolation caused by a CIDR mismatch. Expanded the subnet mask from a /26 to a /24 to include the gateway, allowing the terminal to successfully ping 10.50.50.1.
Operation Hidden Door: Protocol interrogation using ss -tuln and curl -I localhost:8080. Remediated local DNS deception by purging poisoned entries in /etc/hosts to restore legitimate resolution for Google.
Phase 2: Virtualization & Automation (S07 - S09)
Infrastructure: Sandboxed Debian via Proot-Distro in Termux, replacing resource-heavy Type-2 Hypervisors (VirtualBox/VMware).
The Forge: Developed Python-based security automation (port_check.py, log_filter.py, firewall_bot.py). Implemented try/except error handlers to build graceful failure into scripts, ensuring tools don't crash when logs are missing.
Phase 3: Cross-Platform Zero-Trust Enclave (Proton VPN + Kill Switch)
Hardening Obsolete Infrastructure (MacBook Pivot): Enforced a Strict Kill Switch on a legacy MacBook Pro running macOS High Sierra (End-of-Life). If the encrypted tunnel drops for a millisecond, the network adapter is severed at the hardware level, effectively "air-gapping" the vulnerable machine from the local network while maintaining an AES-256 shield.
The Mobile Bunker (Note 20 Ultra): Implemented Layer 3 Traffic Isolation via Android's "Block connections without VPN" kernel setting. The Termux terminal now operates as a "Ghost." ISP and local eavesdroppers cannot sniff SSH sessions or cloud-bridge payloads.
Secure AI Orchestration: By serving the GodMode UI locally over Python and tunneling it through Proton, we achieved a Hybrid Intelligence Pipeline. Heavy compute is securely passed to Gemini/Claude, while sensitive telemetry is analyzed offline by Gemma 2B.
02 / Hardware Benchmarking & Field Reports
[MISSION]: MiroFish-Offline Red/Blue Swarm (Terminal 0500)
Status: SUCCESSFUL TASK EXECUTION / STRATEGIC HARDWARE DECOMMISSIONING Hardware: Samsung Note 20 Ultra 5G (Exynos 990 / 12GB RAM / 256GB Storage / SD Expanded Vault) Conditions: 20% SOC | No Sleep | Manual OS Override (Phantom Process Killer Bypass) 1. Miro-Swarm-Offline: Terminal Functionality

The Local Handshake: The terminal displayed active negotiation between the Ollama (Tactical Brain) and the Miro-Swarm (Orchestra).
The Mechanism: Executed via local loopback. One terminal instance acted as the "Red" (Offensive) agent querying the Knowledge Graph, while the second instance provided "Blue" (Defensive) feedback—all without an internet handshake.
Data Flow: Logic weights were pulled from the SD Expanded Vault into the 12GB LPDDR5 RAM pool, bypassing standard Android storage latency. 2. Tactical Deployment & System Overrides
Technical Logic: Encountered Signal 9 (OOM) execution kills and pip-metadata locks due to aggressive Android system background limits. Executed manual dependency reconciliation and metadata overrides. Bypassed the Android Phantom Process Killer to force-initialize the swarm on a 20% SOC battery baseline.
(Layman's Version): The phone's software kept trying to "kill" the project to save power. I manually forced it to stay awake and broke through the system's "locks" to finish the install on a dying battery. The Offensive and Defensive AI teams successfully started working together on the terminal for the first time. 3. Hardware Preservation & Uninstall Logic
The Audit: System maintained a 32°C battery baseline during active GraphRAG builds. This is the thermal "Red Line" for an Exynos 990.
The Decision: UNINSTALLED & PURGED. Sustained heat over time from a recursive AI swarm would ruin the Mobile Cybersecurity Workbench. I proved the "Orchestra" works; then I decommissioned to save the rig. 4. Decommissioning Forensic Checklist
 Full Uninstall: Purged 2GB+ of recursive dependencies and model weights.
 Port Sanitization: 7474 (Neo4j), 5001 (Backend), 3000 (Vite) verified CLOSED.
 SD Vault Integrity: Verified vault remains secure and uncompromised post-purge.
 Forensic Clear: ps aux confirms no ghost processes remaining.
03 / Infrastructure as Code & Desktop Rendering
Termux-X11 & Hardware Acceleration
Bypassing standard VNC overhead to run XFCE4 natively on Android.

Initialization: termux-x11 :1 & DISPLAY=:1 xfce4-session &
GPU Acceleration: Virglrenderer deployed to bypass llvmpipe CPU rendering, allowing graphical analysis tools (Wireshark, Autopsy) to run smoothly using the device's native Mali GPU.
Audio Routing: PulseAudio TCP bridge established via PULSE_SERVER=tcp:127.0.0.1:4713 (Pre-loaded libskcodec.so via LD_PRELOAD to fix Samsung OneUI 6.1 codec crashes).
x86 Emulation: Box86/Box64 and Wine installed via proot to execute legacy Windows/Linux x86 security binaries on the ARM64 architecture, bridging the gap between mobile hardware and enterprise software.
⚙️ RAW WORKBENCH LOGS & HISTORICAL SPECS
I. Hardware Matrix
Device	RAM	Status
Samsung Galaxy Note 20 Ultra 5G	12GB	Primary — Fully Verified
Samsung S21 Ultra	12GB	Verified
Samsung S22/S23/S24/S25/S26 Ultra	12GB	Verified
Samsung Z-Fold 3/4/5/6/Trifold	12GB	Verified
Google Pixel 6/7/8/9 Pro/Fold	8-12GB	Verified
iPhone (iOS)	Any	Codespaces + iSH/UTM Pivot
Minimum Requirements:		
Android 10 or higher
8GB RAM minimum (12GB recommended)
5G or Fiber Wi-Fi for GitHub sync and cloud AI
256GB internal storage or 1TB MicroSD for Vault and PCAPs
S-Pen recommended for Wireshark packet precision on Note devices
II. Pre-Flight Checklist
 Termux installed from F-Droid (not Play Store)
 Termux-API installed from F-Droid
 Termux-X11 companion app installed
 Battery optimization DISABLED for Termux in Android Settings
 MicroSD card inserted and mounted
 API keys secured at ~/.secrets/ or within .bashrc
III. Base Initialization
termux-setup-storage
pkg update -y && pkg upgrade -y
pkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y
pip install requests scapy paramiko
IV. OPSEC Data Isolation
mkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence
echo "Vault/" >> .gitignore && echo "*.pcap" >> .gitignore && echo ".secrets/" >> .gitignore && echo ".env" >> .gitignore
git config --local core.excludesfile .gitignore
V. Thermal Safety Protocol
Check temperature: cat /sys/class/thermal/thermal_zone0/temp Divide by 1000 for Celsius. 45000 = 45C.

Safe: Below 40C
Caution: 40C to 45C — reduce workload
Danger: Above 45C — kill switch immediately (pkill -9 -u $(whoami))
XVII. Threat Intelligence Log: Aeternum C2 (Blockchain C2) 🔗
Threat Actor	Vector	Infrastructure	Status
LenAI	C++ Loader (x32/x64)	Polygon Mainnet (Smart Contracts)	ACTIVE (MAR 2026)
A. Technical Breakdown: "Living off the Chain"
Aeternum C2 represents a shift from centralized servers to immutable, decentralized infrastructure.

C2 Mechanism: Commands are stored as encrypted state variables within Solidity smart contracts. The attacker updates the contract to change the "active" payload (Clipper, Stealer, or RAT).
Communication: Infected endpoints utilize JSON-RPC calls (eth_call) to public nodes (e.g., polygon-rpc.com) to retrieve instructions.
Resilience: Since the "server" is the Polygon blockchain, there is no domain to seize or server to take down.
B. Bunker Countermeasures: Note 20 Ultra / Termux Defense
To "project" protection and neutralize this threat on the workbench, the following protocols are deployed:

RPC Traffic Interception (tshark): Monitor for the specific JSON-RPC method used to poll the smart contract:
tshark -i any -Y 'http.request.method == "POST"' -T fields -e http.file_data | grep -E "eth_call|eth_getStorageAt"
Infrastructure Decoupling (DNS Sinkhole): Force the malware to loop harmlessly by redirecting RPC traffic to localhost in the proot environment (/etc/hosts):
127.0.0.1 polygon-rpc.com
127.0.0.1 bor-mainnet.polygon.technology

Behavioral Audit: The workbench uses a background cron job to alert if outbound traffic to known Polygon/Ethereum RPC ports (8545, 443) exceeds a 60-second polling threshold, identifying the C2 "heartbeat." Analyst: C.K. Bachoo | Verified: XO | Date: 21 MAR 2026
XVIII. Forensic Mission Report: Neutralizing DNS Sabotage via OOB ⚓🛡️
Timestamp: March 2026 🕒 Threat Vector: DNS Poisoning / Localized Network Sabotage ("Operation Blackout") ⚠️🔌 Origin: Compromised Local "Wire" (WLAN/Ethernet) at The Knowledge House 🏢🚫

A. Incident Analysis (The Attack) 🕵️‍♂️
The Vector: Sabotage of local name resolution intended to redirect or isolate cohort traffic. 🌪️
Observed Effect: Primary "Wire" nodes failed to resolve external domains; manual pathing to /etc/resolv.conf was blocked by OS-level restrictions. 🔐
Cybersecurity Domain: Network Security / Incident Response (Remediation). 🛠️
B. Bunker Countermeasures: Note 20 Ultra SOC ⚡📱
Action: Leveraged the Workbench's independent Spectrum LTE stack (rmnet_data2) for Out-of-Band (OOB) recovery. 📡🚀
Method: Redirected terminal pathing to $PREFIX/etc/resolv.conf to bypass Android kernel-level permission denied errors. 📂🔓
Result: Successful triage of Google Public DNS (8.8.8.8 / 8.8.4.4). ✅
Resilience: The Workbench remained immune to the "Wire" sabotage because it maintains an independent physical and logical gateway. 🏛️💯
C. Forensic Conclusion & GRC Verification 📝
The Android Mobile Cybersecurity Workbench proved 100% resilient. While the localized network was compromised, the Workbench utilized its native OOB capabilities to maintain technical integrity and connectivity.

~/Android-mobile-cybersecurity-workbench $ ./bunker_audit.sh
--- [BUNKER MOBILE AUDIT ENGINE v1.0] ---
STATUS: NIST CSF COMPLIANCE CHECK
----------------------------------------
[ID.1] Checking Root Status...
  > Device is Not Rooted. Compliance: PASS.
[PR.AC] Checking ADB Status...
  > ADB Daemon: stopped
[DE.CM] Scanning Active Processes...
  PID TTY          TIME CMD
17775 pts/0    00:00:00 bash
17777 pts/0    00:00:00 ps
17778 pts/0    00:00:00 head
----------------------------------------
AUDIT COMPLETE. STANDING BY FOR UPLOAD.
Analyst: C.K. Bachoo | Verified: XO | Date: 23 MAR 2026

XIX. Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense 🚨
Threat Actor	Vector	Target	Deadline / Status
ShinyHunters	Free-For-Teacher Exploit / Credential Harvesting	Canvas LMS (Student PII)	May 6 - May 12, 2026 (ACTIVE EXTORTION)
A. Incident Analysis: The Canvas Breach
The Threat: ShinyHunters compromised the Canvas learning management system, exfiltrating 3.65 TB of data (275M records) including Student IDs, assignments, and private messages. The extortion window closes on May 12.
The Hypothesis: Exfiltrated PII is being leveraged for high-fidelity social engineering, phishing, and credential stuffing attacks against the fellowship cohort.
B. Bunker Countermeasures & Protection
Operating from the Note 20 Ultra "Bunker," I remained completely protected from the SaaS-layer compromise through strict environmental decoupling:

Local Sovereignty: Instead of relying on the compromised Canvas portal, all lab requirements and documentation were served via local Git clones and offline Markdown files.
Jump-Host Isolation: Any necessary downloads originating from Canvas were routed through Google Cloud Shell—an ephemeral, sandboxed environment—preventing any direct connection to my physical hardware.
PrivacyGuard Agent: Used local Python logic via privacy_guard.py to automatically scrub my outgoing logs of Student IDs and names before pushing to GitHub, neutralizing the value of any intercepted PII.
C. The "Trap-Door Air-Gap" (Active Defense)
If an attacker managed to bypass the VPN and breach the local Termux environment, the Bunker employs a sovereign "Trap-Door" defense mechanism:

The Logic: If the automated port sentry (port_harden.py) detects an unauthorized IP binding to Port 8022 (SSH) or Port 8080 (AI Server), it instantly triggers the air_gap_isolate.py protocol.
The Execution: The device immediately drops all network interfaces (ifconfig wlan0 down), severing the connection to the outside world.
The Result: The attacker is locked inside a dead, disconnected session. Simultaneously, the system flushes the volatile memory, wiping ~/.bash_history and ~/.git-credentials. I am no longer in the same "room," and the attacker is left holding an empty, isolated shell. "The mission does not wait for better equipment." — C.K. Bachoo ⚓🫡