Here is your beautifully formatted README:Markdown# 🛡️ Android Mobile Cybersecurity Workbench (The Bunker) v2.8

Mobile-first Purple Team automation lab running on Samsung Galaxy Note 20 Ultra + Termux.
A living proof that enterprise-grade security operations, threat hunting, defensive automation, and AI orchestration can run effectively on constrained Android hardware.

## ✨ v2.8 Release Highlights

* `bunker_audit.sh` — NIST-style mobile security audit engine with colored output
* **Automation Suite (`scripts/` folder)** — Fully deployed and improved:

| Script | Purpose |
|--------|---------|
| `privacy_guard.py` | PII, secrets & token sanitizer before Git pushes |
| `port_harden.py` | Continuous port sentry & trap trigger |
| `air_gap_isolate.py` | Emergency air-gap / trap-door isolation |
| `osint_agent.py` | Passive reconnaissance agent |
| `threat_hunt_logs.py` | TTP & IoC log analyzer |

## 🚀 Quick Start

```bash
cd ~/Android-mobile-cybersecurity-workbench

# Run full NIST audit
bash bunker_audit.sh                    

# Make scripts executable
chmod 700 scripts/*.py && chmod +x bunker_audit.sh
Core StrengthsPurple Team operations on mobile hardwareDefensive automation & threat huntingAI-assisted analysis (Jarvis + Gemini + Claude + local Ollama)Zero Trust enforcement in resource-limited environmentsMobile-to-cloud secure pipelinesOperator: C.K. Bachoo | Navy VeteranCurrent Role: Cybersecurity Innovation Fellow — The Knowledge House NY (IF-CS-26)Last updated: May 12, 2026📋 Table of ContentsHardware & DeploymentAutomation SuiteGodMode AI OrchestrationOPSEC & SecurityTactical PhasesHardware Benchmarking & Field ReportsInfrastructure as Code & Desktop RenderingFull Setup & Troubleshooting GuideHardware & DeploymentPrimary Device: Samsung Galaxy Note 20 Ultra (Exynos 990, 12GB RAM, 256GB + MicroSD)Environment: Termux + proot-distro (Kali) + X11Philosophy: "The mission does not wait for better equipment."Automation SuiteAll scripts are built with zero third-party dependencies to prevent RAM spikes and OOM kills on Android. Run bunker_audit.sh regularly to verify system hardening and compliance.GodMode AI OrchestrationJarvis Voice AI as primary interfaceMulti-LLM support (Gemini, Claude, local Ollama/Gemma)GodMode web wrapper for concurrent model accessStrict sandboxing and Zero Trust gatesOPSEC & SecuritySensitive data stays in Vault/ (never committed)privacy_guard.py scrubs PII/secrets before every pushAir-gap trap door via air_gap_isolate.pyStrong .gitignore + secrets folder protection"The mission does not wait for better equipment." — C.K. Bachoo ⚓🫡Connect: Open to collaboration on mobile security, Purple Team ops, DevSecOps automation, and constrained-environment security.Full Portfolio: CK-Bachoo/IF-Cyber-PortfolioAndroid Mobile Cybersecurity Workbench: The Bunker SOP 🛡️DEFCON Status: CHARLIE (Active Threat: ShinyHunters May 12 Deadline)00 / Core Directives & GodMode AI OrchestrationThe Bunker utilizes a native GodMode AI orchestration framework to manage multiple LLMs simultaneously. This prevents vendor lock-in, ensures operational continuity during network degradation, and enables multi-model cross-validation for complex threat hunting.GodMode Chat Browser Initialization (smol-ai)The GodMode webview wrapper is deployed to access ChatGPT, Claude 3.5, Bard, Bing, and Gemini 1.5 Pro concurrently.Execution (The Agile Pivot):Bashcd ~/GodMode && python -m http.server 8000
Architecture Context: Running multiple heavy web-apps natively in Android Chrome crashes the Exynos 990 due to RAM constraints. The GodMode wrapper bypasses standard browser memory limits, creating a unified, lightweight interface for all API-less chat models, completely tunneled through our encrypted VPN.OpenClaw / PicoClaw Agentic AutomationLocal AI agents deployed via OpenClaw to perform autonomous log parsing, system audits, and threat hunting without requiring human-in-the-loop for every command.Security Constraint (MCP Security 101): The Model Context Protocol (MCP) acts as the API layer. To prevent "God-Mode" privilege escalation, all MCP tools are strictly sandboxed.Enforcement: Implemented Client-Side Validation to strip Prompt Injection vectors before execution. Principle of Least Privilege is strictly enforced.Local Fallback (Ollama + Llama 3.2 / Gemma 2B)When external networks are compromised or air-gapped, the Bunker relies on 100% local, offline inference to parse sensitive logs.Execution: ollama serve & ollama run gemma:2bConstraint: Never run Ollama simultaneously with X11/Jarvis. The Android kernel's Signal 9 (Out of Memory) Phantom Process Killer will terminate the session. Graceful teardown requires pkill ollama.01 / Tactical Phases (Canvas Aligned)Phase 0: System Foundations (S01 - S03)CTI & Navigation: Linux Scavenger Hunt & Access Control Hardening (harden.sh). Mastered the Filesystem Hierarchy Standard (FHS).Permissions: Applied the Read-Write-Execute (RWX) matrix (700 for private, 755 for scripts, 644 for standard files).Text Plumbing: Advanced log filtering using Grep, Sed, and Awk.Phase 1: Network & Protocol Defense (S04 - S06)Operation Broken Link (L1-L3): Restored Layer 3 connectivity by diagnosing a missing default route and manually rebuilding the routing table (sudo ip route add default via 10.0.0.1).Operation Grid Lock (Subnetting Crucible): Bypassed isolation caused by a CIDR mismatch. Expanded the subnet mask from a /26 to a /24.Operation Hidden Door: Protocol interrogation using ss -tuln and curl -I localhost:8080. Remediated local DNS deception by purging poisoned entries in /etc/hosts.Phase 2: Virtualization & Automation (S07 - S09)Infrastructure: Sandboxed Debian via Proot-Distro in Termux, replacing resource-heavy Type-2 Hypervisors.The Forge: Developed Python-based security automation (port_check.py, log_filter.py, firewall_bot.py). Implemented try/except error handlers for graceful script failures.Phase 3: Cross-Platform Zero-Trust Enclave (Proton VPN + Kill Switch)Hardening Obsolete Infrastructure (MacBook Pivot): Enforced a Strict Kill Switch on a legacy MacBook Pro.The Mobile Bunker (Note 20 Ultra): Implemented Layer 3 Traffic Isolation via Android's "Block connections without VPN" kernel setting. The Termux terminal now operates as a "Ghost."Secure AI Orchestration: Achieved a Hybrid Intelligence Pipeline. Heavy compute is securely passed to Gemini/Claude, while sensitive telemetry is analyzed offline by Gemma 2B.02 / Hardware Benchmarking & Field Reports[MISSION]: MiroFish-Offline Red/Blue SwarmStatus: SUCCESSFUL TASK EXECUTION / STRATEGIC HARDWARE DECOMMISSIONINGHardware: Samsung Note 20 Ultra 5GConditions: 20% SOC | No Sleep | Manual OS Override (Phantom Process Killer Bypass)Tactical Deployment & System Overrides: Encountered Signal 9 (OOM) execution kills and pip-metadata locks due to aggressive Android limits. Bypassed the Android Phantom Process Killer to force-initialize the swarm on a 20% SOC battery baseline.Hardware Preservation & Uninstall Logic:The Audit: System maintained a 32°C battery baseline during active GraphRAG builds (thermal "Red Line" for an Exynos 990).The Decision: UNINSTALLED & PURGED. Sustained heat from a recursive AI swarm would ruin the rig. I proved the "Orchestra" works; then I decommissioned to save the hardware.03 / Infrastructure as Code & Desktop RenderingTermux-X11 & Hardware AccelerationBypassing standard VNC overhead to run XFCE4 natively on Android.Initialization: termux-x11 :1 & DISPLAY=:1 xfce4-session &GPU Acceleration: Virglrenderer deployed to bypass llvmpipe CPU rendering, allowing graphical analysis tools (Wireshark, Autopsy) to run smoothly.Audio Routing: PulseAudio TCP bridge established via PULSE_SERVER=tcp:127.0.0.1:4713.x86 Emulation: Box86/Box64 and Wine installed via proot to execute legacy Windows/Linux x86 security binaries on the ARM64 architecture.⚙️ RAW WORKBENCH LOGS & HISTORICAL SPECSI. Hardware MatrixDeviceRAMStatusSamsung Galaxy Note 20 Ultra 5G12GBPrimary — Fully VerifiedSamsung S21/S22/S23/S24/S25/S26 Ultra12GBVerifiedSamsung Z-Fold 3/4/5/6/Trifold12GBVerifiedGoogle Pixel 6/7/8/9 Pro/Fold8-12GBVerifiediPhone (iOS)AnyCodespaces + iSH/UTM PivotMinimum Requirements: Android 10+, 8GB RAM (12GB rec.), 5G/Fiber Wi-Fi, 256GB storage. S-Pen recommended.Hardware TroubleshootingProblemFixPhone overheats during setupStop all processes. Cool device. Restart one tool at a time.Not enough storageMove Vault to MicroSD: ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/VaultAndroid version too oldCodespaces browser fallback works on any Android versionMicroSD not detectedSettings → Device Care → Storage → check SD card mount statusII. Pre-Flight Checklist[ ] Termux installed from F-Droid (not Play Store)[ ] Termux-API installed from F-Droid[ ] Termux-X11 companion app installed[ ] Battery above 50%[ ] Battery optimization DISABLED for Termux in Android SettingsPre-Flight TroubleshootingProblemFixTermux from Play Store installedUninstall it. Install from F-Droid only. Play Store version is outdated.Battery optimization keeps re-enablingSamsung One UI resets this. Check after every phone restart.No F-Droid on phoneGo to f-droid.org in browser. Download and install APK directly.III. Base InitializationOpen Termux and run each command one at a time:Bash# Step 1 — Grant storage access
termux-setup-storage

# Step 2 — Update and upgrade
pkg update -y && pkg upgrade -y

# Step 3 — Install core tools
pkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y

# Step 4 — Install Python security packages
pip install requests scapy paramiko

# Step 5 — Verify installations
python --version && git --version && nmap --version && ssh -V

# Step 6 — Clone repository
cd ~ && git clone --depth 1 [https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git](https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git) && cd Android-mobile-cybersecurity-workbench

# Step 7 — Set your wake word
bash scripts/set_wakeword.sh
IV. OPSEC Data IsolationAll sensitive scan results, packet captures, and logs stay in the Vault/.Bash# Create Vault structure
mkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence

# Add Vault to gitignore
echo "Vault/" >> .gitignore
echo ".pcap" >> .gitignore
echo ".secrets/" >> .gitignore
git config --local core.excludesfile .gitignore
OPSEC Rules: Never commit real IP addresses, API keys, PAT tokens, or pcap files to GitHub.V. SSH Keys for GitHubBashssh-keygen -t ed25519 -C "YOUR-GITHUB-USERNAME"
cat ~/.ssh/id_ed25519.pub
Copy output -> GitHub Profile Settings -> SSH and GPG Keys -> New SSH Key. Test with ssh -T git@github.com.VI. X11 Graphical InterfaceBash# Install X11
pkg install xfce4 xfce4-goodies x11-repo xorg-xrandr -y

# Launch X11 (Manual Mode)
termux-x11 :1 & DISPLAY=:1 xfce4-session &
CRITICAL: Always acquire "Wakelock" from the Termux notification bar to prevent freezing.VII. Kali Linux VirtualizationBash# Install and enter Kali
proot-distro install kali
proot-distro login kali

# Update and install tools inside Kali
apt update -y && apt install nmap wireshark-cli tshark metasploit-framework sqlmap nikto -y
VIII. AI Stack Deployment & Security ToolingResource Management MatrixToolRAM UsageTypeSafe to Run Together?Jarvis Voice AI~50MB LocalPython + CloudYES — PrimaryGemini API~0MB localCloud OnlyYES — Built into JarvisClaude AI~0MB localCloud OnlyYES — Built into JarvisX11 Desktop~400MB LocalGUIYES — With JarvisWireshark X11~300MB LocalGUIYES — With X11 activeOllama / Gemma4-6GB LocalLocal LLMNO — Run separatelyGolden Rule: Never run Ollama with anything else. Exynos 990 will overheat and 12GB RAM will max out.IX. GitHub PAT Cloud SyncBash# Store PAT Securely
mkdir -p ~/.secrets && chmod 700 ~/.secrets
echo "PASTE-YOUR-PAT-HERE" > ~/.secrets/github_pat.txt
chmod 600 ~/.secrets/github_pat.txt

# Load and Push
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
git remote set-url origin https://YOUR-GITHUB-USERNAME:${GITHUB_PAT}@[github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git](https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git)
git add . && git commit -m "Sync" && git push origin master
X. Operational Commands Cheat SheetActionCommandNetwork Discoverynmap -sn 192.168.1.0/24Full Port Scannmap -A 192.168.1.1Packet Capturetshark -i wlan0 -w Vault/PCAPs/cap.pcapWireshark X11DISPLAY=:1 wireshark Vault/PCAPs/cap.pcap &Wake Full Bunkerbunker (or your chosen wake word)XI. Wake and Close CommandsSafe full shutdown: ```bashpkill -f jarvis.py && pkill ollama && pkill xfce4-session && pkill termux-x11Nuclear shutdown: pkill -9 -u $(whoami)XII. Thermal Safety ProtocolCheck temperature:Bashcat /sys/class/thermal/thermal_zone0/temp
(Divide by 1000 for Celsius. 45000 = 45C. Stop operations immediately if > 45C).XVI. Voice-Sec Terminal & Automation Suite 🤖ComponentScriptStatusPII Sanitizerscripts/privacy_guard.pyDEPLOYEDPort Sentry / Trap-Doorscripts/port_harden.pyDEPLOYEDTrap-Door Air-Gapscripts/air_gap_isolate.pyDEPLOYEDOSINT Recon Agentscripts/osint_agent.pyDEPLOYEDTTP Log Analyzerscripts/threat_hunt_logs.pyDEPLOYEDNIST Audit Enginebunker_audit.shDEPLOYEDAutomation Suite ArchitectureThe Bunker's Python automation suite operates on a single architectural constraint: zero third-party dependencies. Every script runs on Python's standard library only.Deployment CommandsBashchmod 700 scripts/*.py && chmod +x bunker_audit.sh

# Run PII sweep before any push
python3 scripts/privacy_guard.py Vault/Logs/access.log

# Start port sentry (runs continuously)
python3 scripts/port_harden.py &

# Hunt for IoCs in access log
python3 scripts/threat_hunt_logs.py Vault/Logs/access.log
XVII. Threat Intelligence Log: Aeternum C2 (Blockchain C2) 🔗Threat Actor Vector: LenAI C++ Loader (x32/x64)Infrastructure: Polygon Mainnet (Smart Contracts)Status: ACTIVE (MAR 2026)Bunker Countermeasures:Bash# RPC Traffic Interception
tshark -i any -Y 'http.request.method == "POST"' -T fields -e http.file_data | grep -E "eth_call|eth_getStorageAt"
XVIII. Forensic Mission Report: Neutralizing DNS Sabotage via OOB ⚓🛡️Threat Vector: DNS Poisoning / Localized Network SabotageBunker Countermeasures: Leveraged independent Spectrum LTE stack (rmnet_data2) for Out-of-Band (OOB) recovery. Redirected terminal pathing to $PREFIX/etc/resolv.conf to bypass Android kernel-level permission denied errors.XIX. Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense 🚨Target: Canvas LMS (Student PII)The "Trap-Door Air-Gap" Defense: If the automated port sentry (port_harden.py) detects an unauthorized IP binding to Port 8022 (SSH) or Port 8080 (AI Server), it instantly triggers air_gap_isolate.py. The device immediately drops all network interfaces, locking the attacker inside a dead session.Analyst: C.K. Bachoo | Verified: XO | Date: MAY 2026 
