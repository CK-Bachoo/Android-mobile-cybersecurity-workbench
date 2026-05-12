# 🛡️ Mobile-first cybersecurity practitioner building enterprise-grade Purple Team capabilities on constrained Android hardware (Samsung Note 20 Ultra + Termux).

**Core Strengths**

Purple Team operations and defensive automation
Mobile-to-cloud security pipelines
AI-assisted analysis and documentation
Zero Trust enforcement in resource-limited environments

Current Deployment

The Knowledge House NY Innovation Fellowship (IF-CS-26)
Full Portfolio: https://github.com/CK-Bachoo/IF-Cyber-Portfolio
Mobile SOC Rig: https://github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench

Open to connecting on mobile security, DevSecOps, automation, and Purple Team topics.

Android Mobile Cybersecurity Workbench: The Bunker SOP 🛡️
Role: 🛡️Cybersecurity Innovation Fellow. Purple Team Ops | Mobile-to-Cloud Lab Environments | IT Support & AI Security Architect | Navy Veteran
Deployment: Samsung Note 20 Ultra Exynos 990 12 GB RAM 256 GB internal storage with exp. SD card storage & Legacy MacBook Pro 13 2011 High Sierra (Decommissioned Feb 1, 2025 - Black Screen of Death)
Operator: | Bachoo, C. K. | Cybersecurity Innovation Fellow NY IF-CS-26 | The Knowledge House Bronx, NY
DEFCON Status: CHARLIE (Active Threat: ShinyHunters May 12 Deadline)
00 / Core Directives & GodMode AI Orchestration
GodMode AI & OpenClaw Agent Integration
The Bunker utilizes a native GodMode AI orchestration framework to manage multiple LLMs simultaneously. This prevents vendor lock-in, ensures operational continuity during network degradation, and enables multi-model cross-validation for complex threat hunting.

GodMode Chat Browser Initialization (smol-ai): The GodMode webview wrapper is deployed to access ChatGPT, Claude 3.5, Bard, Bing, and Gemini 1.5 Pro concurrently.
Execution (The Agile Pivot): cd ~/GodMode && python -m http.server 8000 (Pivoted from heavy NodeJS/npm dependencies to a native Python HTTP server for "Intelligent Laziness" resource optimization, eliminating compiler overhead).
Architecture Context: Running multiple heavy web-apps natively in Android Chrome crashes the Exynos 990 due to RAM constraints. The GodMode wrapper bypasses standard browser memory limits, creating a unified, lightweight interface for all API-less chat models, completely tunneled through our encrypted VPN.
OpenClaw / PicoClaw Agentic Automation: Local AI agents deployed via OpenClaw to perform autonomous log parsing, system audits, and threat hunting without requiring human-in-the-loop for every command.
Security Constraint (MCP Security 101): The Model Context Protocol (MCP) acts as the API layer for these agents. To prevent "God-Mode" privilege escalation (e.g., tool poisoning or unauthorized system writes), all MCP tools are strictly sandboxed.
Enforcement: Implemented Client-Side Validation to strip Prompt Injection vectors before execution, and the Principle of Least Privilege is strictly enforced on the Termux environment (e.g., agents cannot write to /var/log, only read).

Local Fallback (Ollama + Llama 3.2 / Gemma 2B):
When external networks are compromised or air-gapped, the Bunker relies on 100% local, offline inference to parse sensitive logs without leaking proprietary data to cloud providers.

Hardware Pool: 12GB LPDDR5 RAM.
Execution: ollama serve & ollama run gemma:2b
Constraint: Never run Ollama simultaneously with X11/Jarvis. The Android kernel's Signal 9 (Out of Memory) Phantom Process Killer will terminate the session. Graceful teardown requires pkill ollama to flush RAM.


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
Status: SUCCESSFUL TASK EXECUTION / STRATEGIC HARDWARE DECOMMISSIONING
Hardware: Samsung Note 20 Ultra 5G (Exynos 990 / 12GB RAM / 256GB Storage / SD Expanded Vault)
Conditions: 20% SOC | No Sleep | Manual OS Override (Phantom Process Killer Bypass)
1. Miro-Swarm-Offline: Terminal Functionality

The Local Handshake: The terminal displayed active negotiation between the Ollama (Tactical Brain) and the Miro-Swarm (Orchestra).
The Mechanism: Executed via local loopback. One terminal instance acted as the "Red" (Offensive) agent querying the Knowledge Graph, while the second instance provided "Blue" (Defensive) feedback — all without an internet handshake.
Data Flow: Logic weights were pulled from the SD Expanded Vault into the 12GB LPDDR5 RAM pool, bypassing standard Android storage latency.

2. Tactical Deployment & System Overrides

Technical Logic: Encountered Signal 9 (OOM) execution kills and pip-metadata locks due to aggressive Android system background limits. Executed manual dependency reconciliation and metadata overrides. Bypassed the Android Phantom Process Killer to force-initialize the swarm on a 20% SOC battery baseline.
(Layman's Version): The phone's software kept trying to "kill" the project to save power. I manually forced it to stay awake and broke through the system's "locks" to finish the install on a dying battery. The Offensive and Defensive AI teams successfully started working together on the terminal for the first time.

3. Hardware Preservation & Uninstall Logic

The Audit: System maintained a 32°C battery baseline during active GraphRAG builds. This is the thermal "Red Line" for an Exynos 990.
The Decision: UNINSTALLED & PURGED. Sustained heat over time from a recursive AI swarm would ruin the Mobile Cybersecurity Workbench. I proved the "Orchestra" works; then I decommissioned to save the rig.

4. Decommissioning Forensic Checklist

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


⚙️ RAW WORKBENCH LOGS & HISTORICAL SPECS BELOW:
🛡️ ARM64 Mobile-to-Cloud Security Workbench (The Bunker)
Operator: Bachoo, C. K. | Navy Veteran | Dual Google/CompTIA A+ | Innovation Fellow | New York IF-CS-26 | AI Security Architect | Principal Security Engineer (Purple Team & GRC)
Platform: Samsung Galaxy Note 20 Ultra | Termux | Mobile-Only Architecture
Mission: Scale enterprise-level cybersecurity workflows on constrained mobile hardware.
"The mission does not wait for better equipment." — C.K. Bachoo ⚓

📋 Table of Contents

I. Hardware Matrix
II. Pre-Flight Checklist
III. Base Initialization
IV. OPSEC Data Isolation
V. SSH Keys for GitHub
VI. X11 Graphical Interface
VII. Kali Linux Virtualization
VIII. AI Stack Deployment
IX. GitHub PAT Cloud Sync
X. Operational Commands
XI. Wake and Close Commands
XII. Thermal Safety Protocol
XIII. Full Troubleshooting Guide
XIV. Business Integration Guide
XV. Professional Verification
XVI. Voice-Sec Terminal & Automation Suite 🤖
XVII. Threat Intelligence Log: Aeternum C2 🔗
XVIII. Forensic Mission Report: DNS Sabotage / OOB Recovery 🛡️📡
XIX. Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense 🚨


⚙️ I. Hardware Matrix
DeviceRAMStatusSamsung Galaxy Note 20 Ultra 5G12GBPrimary — Fully VerifiedSamsung S21 Ultra12GBVerifiedSamsung S22/S23/S24/S25/S26 Ultra12GBVerifiedSamsung Z-Fold 3/4/5/6/Trifold12GBVerifiedGoogle Pixel 6/7/8/9 Pro/Fold8-12GBVerifiediPhone (iOS)AnyCodespaces + iSH/UTM Pivot
Minimum Requirements:

Android 10 or higher
8GB RAM minimum (12GB recommended)
5G or Fiber Wi-Fi for GitHub sync and cloud AI
256GB internal storage or 1TB MicroSD for Vault and PCAPs
S-Pen recommended for Wireshark packet precision on Note devices

Hardware Troubleshooting:
ProblemFixPhone overheats during setupStop all processes. Cool device. Restart one tool at a time.Not enough storageMove Vault to MicroSD. ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/VaultAndroid version too oldCodespaces browser fallback works on any Android versionMicroSD not detectedSettings → Device Care → Storage → check SD card mount status

✅ II. Pre-Flight Checklist
Before starting run through this list:

 Termux installed from F-Droid (not Play Store)
 Termux-API installed from F-Droid
 Termux-X11 companion app installed
 Battery above 50 percent
 Connected to Wi-Fi
 Storage permission granted to Termux
 Battery optimization DISABLED for Termux in Android Settings
 GitHub account created at github.com
 At least 4GB free storage
 MicroSD card inserted and mounted (recommended)
 Gemini API key saved at ~/.secrets/gemini_api_key.txt

How to disable battery optimization:
Android Settings → Apps → Termux → Battery → Unrestricted
Do the same for Termux-API and Termux-X11
Pre-Flight Troubleshooting:
ProblemFixTermux from Play Store installedUninstall it. Install from F-Droid only. Play Store version is outdated.Battery optimization keeps re-enablingSamsung One UI resets this. Check after every phone restart.No F-Droid on phoneGo to f-droid.org in browser. Download and install APK directly.MicroSD not showing in TermuxRun termux-setup-storage and tap Allow

🚀 III. Base Initialization
Open Termux. Run each command one at a time. Wait for each to finish.
Step 1 — Grant storage access:
bashtermux-setup-storage
A popup will appear. Tap Allow.
Step 2 — Update and upgrade:
bashpkg update -y && pkg upgrade -y
Step 3 — Install all required tools:
bashpkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y
Step 4 — Install Python security packages:
bashpip install requests scapy paramiko
Step 5 — Verify everything installed correctly:
bashpython --version && git --version && nmap --version && ssh -V
All four should return version numbers.
Step 6 — Clone this repository:
bashcd ~ && git clone --depth 1 https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git && cd Android-mobile-cybersecurity-workbench
Replace YOUR-GITHUB-USERNAME with your actual GitHub username.
Step 7 — Set your wake word:
bashbash scripts/set_wakeword.sh
Choose any word. That word launches X11 and Jarvis together.
Base Initialization Troubleshooting:
ProblemFixpkg update failsRun termux-change-repo and select a different mirrorPackage not foundRun pkg update first then retry installStorage permission deniedRun termux-setup-storage and tap Allowpip install failsRun pip install --upgrade pip firstgit clone failsCheck Wi-Fi. Verify GitHub username is correct.Python not found after installClose and reopen Termux. Run source ~/.bashrc

🛡️ IV. OPSEC Data Isolation
All sensitive scan results, packet captures, and logs stay in the Vault. Vault is never committed to GitHub.
Create Vault structure:
bashmkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence
Add Vault to gitignore:
bashecho "Vault/" >> .gitignore && echo "*.pcap" >> .gitignore && echo "*.cap" >> .gitignore && echo ".secrets/" >> .gitignore && git config --local core.excludesfile .gitignore
Verify Vault is protected:
bashcat .gitignore && git status
Vault folder should NOT appear in git status output.
Move Vault to MicroSD for physical isolation:
bashmkdir -p /sdcard/Vault && ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/Vault
OPSEC Rules:

Never commit real IP addresses to GitHub
Never commit API keys or PAT tokens
Never commit pcap files — keep in Vault only
Always use YOUR-GITHUB-USERNAME placeholder in public docs
Revoke PAT immediately if accidentally exposed

OPSEC Troubleshooting:
ProblemFixVault appearing in git statusRun git rm -r --cached Vault/ then commitSecrets accidentally committedImmediately revoke PAT on GitHub. Rotate all keys.gitignore not workingRun git config --local core.excludesfile .gitignoreVault files too large for phoneMove Vault to MicroSD using symlink above.secrets folder exposedRun chmod 700 ~/.secrets && chmod 600 ~/.secrets/*

🔑 V. SSH Keys for GitHub
SSH keys give you passwordless GitHub access that never expires.
Step 1 — Generate your key:
bashssh-keygen -t ed25519 -C "YOUR-GITHUB-USERNAME"
Press ENTER three times to accept all defaults.
Step 2 — Display your public key:
bashcat ~/.ssh/id_ed25519.pub
Step 3 — Copy YOUR output. Never share it publicly.
Step 4 — Add to GitHub:

Open github.com in browser
Profile photo → Settings
SSH and GPG keys → New SSH key
Title: Note20Ultra-Termux
Paste YOUR key
Tap Add SSH key

Step 5 — Verify connection:
bashssh -T git@github.com
Should return: Hi YOUR-GITHUB-USERNAME! You've successfully authenticated.
SSH Troubleshooting:
ProblemFixPermission deniedMake sure you copied the .pub file not the private keyConnection refusedRun eval $(ssh-agent -s) then ssh-add ~/.ssh/id_ed25519ssh not foundRun pkg install openssh firstKey not accepted by GitHubDelete the key on GitHub and re-add itAuthentication keeps failingGenerate a new key pair and start fresh

🖥️ VI. X11 Graphical Interface
X11 gives you a full Linux desktop GUI on your phone screen. Required for Wireshark, VS Code visual editing, and multi-window operations.
Install X11:
bashpkg install xfce4 xfce4-goodies x11-repo xorg-xrandr -y
🎯 Choose Your Operating Mode
Mode 1 — Full Automation (Recommended): Set your wake word once. Type it. Everything launches. Jarvis AI online. X11 desktop open. Zero Trust active.
bashbash scripts/set_wakeword.sh
Then type your wake word every session. Example: bunker
Mode 2 — Manual Control: Skip the wake word. Run each tool individually. Use the manual commands below. No AI. No automation.
Mode 3 — Terminal Only: Skip X11 entirely. Run everything in Termux terminal. Lightweight. Fast. Best for low battery or quick operations.
HOW TO WAKE X11
Automatic — wake word:
bashbunker
Replace bunker with your personal wake word.
Manual — step by step:
bashtermux-x11 :1 &
DISPLAY=:1 xfce4-session &
Then open Termux-X11 app. Acquire wakelock from notification bar.
HOW TO LAUNCH APPS IN X11
bashDISPLAY=:1 wireshark &
DISPLAY=:1 thunar &
DISPLAY=:1 xterm &
DISPLAY=:1 [appname] &
HOW TO CLOSE X11
bashpkill xfce4-session && pkill termux-x11
Nuclear option if frozen:
bashpkill -9 -u $(whoami)
X11 Wake Lock — CRITICAL

Swipe down notification bar
Find Termux notification
Tap Acquire Wakelock

Do this EVERY TIME or X11 freezes within minutes.
X11 Troubleshooting:
ProblemFixBlack screenClose Termux-X11 app. Reopen. Run termux-x11 :1 & againGUI freezes immediatelyAcquire wakelock from notification bar firstProcess killed by AndroidDisable battery optimization for Termux in SettingsDisplay variable errorRun export DISPLAY=:1 before any GUI commandxfce4-session not foundRun pkg install xfce4 -y againTermux-X11 app crashesReinstall from F-DroidWake word not workingRun source ~/.bashrc then try againX11 and Jarvis not starting togetherRun bash scripts/bunker_wake.sh directly

🧪 VII. Kali Linux Virtualization
Kali runs as a full Linux environment inside Termux using proot. No root required.
Install Kali:
bashproot-distro install kali
Downloads about 500MB. Takes several minutes on Wi-Fi.
Enter Kali:
bashproot-distro login kali
Your prompt changes to root@localhost.
Update and install security tools:
bashapt update -y && apt install nmap wireshark-cli tshark metasploit-framework sqlmap nikto -y
Verify tools:
bashnmap --version && tshark --version && msfconsole --version
Exit Kali:
bashexit
Run single command without entering Kali:
bashproot-distro login kali -- nmap -sn 192.168.1.0/24
Kali Troubleshooting:
ProblemFixInstall hangs at 0 percentCTRL+C then proot-distro remove kali then reinstallapt not foundYou are not inside Kali. Run proot-distro login kaliTool not foundapt update && apt install [toolname] -y inside KaliKali environment corruptedproot-distro remove kali then proot-distro install kaliCannot push from inside KaliExit Kali first. Push from Termux.Metasploit takes too longNormal. First launch downloads dependencies. Wait 5 minutes.No internet inside KaliExit Kali. Check Wi-Fi. Re-enter Kali.

🤖 VIII. AI Stack Deployment & Security Tooling
Resource Management — Note 20 Ultra 12GB RAM
ToolRAM UsageTypeSafe to Run Together?Jarvis Voice AI~50MBLocal Python + CloudYES — PrimaryGemini API~0MB localCloud OnlyYES — Built into JarvisClaude AI~0MB localCloud OnlyYES — Built into JarvisX11 Desktop~400MBLocal GUIYES — With JarvisVS Code Codespaces~200MB browserCloud IDEYES — With JarvisWireshark X11~300MBLocal GUIYES — With X11 activeNmap~50MBLocal ScannerYES — LightweightOllama / Gemma 2B4-6GBLocal LLMNO — Run separately
Golden Rule: Never run Ollama with anything else. Exynos 990 will overheat and 12GB RAM will max out.
🎙️ Jarvis Voice AI — Primary Command Interface
Voice-activated AI built natively on the Note 20 Ultra. Zero Trust gate on all execute commands. All sessions logged to Vault and 512GB MicroSD and GitHub.
Hardware this was built for:

Device: Samsung Galaxy Note 20 Ultra
Processor: Exynos 990
RAM: 12GB
Storage: 256GB Internal + 512GB MicroSD

Install Jarvis:
bashpkg install termux-api -y && pip install requests
Wake Jarvis manually:
bashcd ~/Android-mobile-cybersecurity-workbench
python3 scripts/jarvis.py
Wake Jarvis automatically with X11:
bashbunker
Jarvis voice commands:

Say anything — Jarvis processes via Gemini and responds
Say "hardware check" — thermal and storage diagnostics
Say "scan my network" — suggests nmap command with Zero Trust gate
Say "start packet capture" — suggests tshark command
Say "help" — lists all capabilities
Say "exit" or "shutdown" — clean shutdown with session log

Stop Jarvis:
bashpkill -f jarvis.py
Jarvis Troubleshooting:
ProblemFixNo voice input detectedCheck termux-api permissions — Microphone must be allowedTTS not speakingRun termux-tts-speak "test" to verify audioGemini not respondingRun echo $GEMINI_API_KEY — if blank run source ~/.bashrcPhone gets hotStop Jarvis. Never run with Ollama simultaneouslyJarvis loop crashesRun source ~/.bashrc then restart jarvis.pyZero Trust gate not hearing confirmSpeak clearly. Move closer to mic.Wake word not launching JarvisRun source ~/.bashrc then try wake word again
🔑 Bunker Wake System — One Word Launches Everything
First time setup:
bashbash scripts/set_wakeword.sh
Wake WordOperator StylebunkerC.K. Bachoo — OriginalsentinelDefensive posturenighthawkStealth opsfortressMaximum defenseshadowLow profilejarvisClassic AI referenceopsShort and tactical
After setup — type your word and hit ENTER:
bashbunker
What happens automatically:

Environment and PAT load
X11 server starts
XFCE blue desktop launches
Termux-X11 app opens
Jarvis speaks and goes online

Wake Word Troubleshooting:
ProblemFixWake word not recognizedRun source ~/.bashrc then try againWake word launches but X11 is blackAcquire wakelock from notification barJarvis does not speak on wakeCheck termux-api mic permissionsWant to change wake wordRun set_wakeword.sh againWake word disappeared after restartRun source ~/.bashrc — alias reloads
🛰️ Nmap — Network Intelligence
Install:
bashpkg install nmap -y
Essential commands:
bashnmap -sn 192.168.1.0/24
nmap -sV 192.168.1.1
nmap -A 192.168.1.1
nmap -p 22,80,443,8080 192.168.1.1
nmap -F 192.168.1.1
nmap -oN Vault/Scans/scan_$(date +%Y%m%d_%H%M%S).txt 192.168.1.1
nmap -oA Vault/Scans/scan_$(date +%Y%m%d) 192.168.1.1
Nmap + Wireshark workflow:
bashtshark -i wlan0 -w Vault/PCAPs/nmap_capture.pcap &
nmap -sV 192.168.1.1
pkill tshark
DISPLAY=:1 wireshark Vault/PCAPs/nmap_capture.pcap &
Nmap Troubleshooting:
ProblemFixPermission deniedUse -sn ping scan — no root neededNo hosts foundVerify same network. Check subnet.Scan too slowAdd -T4 flag for faster timingnmap not foundpkg install nmap -yResults not savingmkdir -p Vault/ScansSYN scan requires rootEnter Kali proot for root-level scans
🦈 Wireshark — Packet Analysis
Install CLI in Kali:
bashproot-distro login kali && apt install wireshark-cli tshark -y
Essential commands:
bashtshark -D
tshark -i wlan0
tshark -i wlan0 -w Vault/PCAPs/capture_$(date +%Y%m%d_%H%M%S).pcap
tshark -i wlan0 -c 100 -w Vault/PCAPs/capture.pcap
tshark -r Vault/PCAPs/capture.pcap
tshark -i wlan0 -Y "http"
tshark -i wlan0 -Y "dns"
tshark -i wlan0 -Y "ip.addr == 192.168.1.1"
DISPLAY=:1 wireshark Vault/PCAPs/capture.pcap &
Wireshark Troubleshooting:
ProblemFixNo interfaces foundRun termux-setup-storage and grant permissionsPermission denied on captureEnter Kali proot for root accesstshark not foundapt install tshark -y inside KaliWireshark GUI not openingMake sure X11 is running and DISPLAY=:1 is setCapture file too largeAdd -c 500 to limit packet countCannot read pcap fileRun ls Vault/PCAPs/ to verify path
💻 VS Code — Development Environment
bash# Open Kiwi browser
# Go to github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench
# Tap Code → Codespaces → Create codespace on master
VS Code Troubleshooting:
ProblemFixCodespace takes too longClose and reopen. Free tier has limits.Changes not savingCommit and push before closingTerminal not respondingRefresh the browser tabCodespace expiredCreate a new one — repo is safe on GitHub
🖥️ Local AI — Ollama
Offline AI. No internet required. Heavy RAM usage. Run ALONE. Never with other tools.
Wake Ollama — close everything else first:
bashpkill -f jarvis.py && pkill xfce4-session && pkill termux-x11
ollama serve &
ollama run gemma:2b
Stop Ollama:
bashpkill ollama
Ollama Troubleshooting:
ProblemFixServer hangspkill ollama then ollama serve & againOut of memoryClose everything else firstModel download failsCheck Wi-Fi. Retry ollama pull gemma:2bPhone overheatingStop immediately. pkill ollamaResponse too slowUse smaller model or ensure terminal is not overloaded.Cannot run with JarvisBy design. Close Jarvis first. Ollama needs all 12GB.
☁️ Cloud AI — Gemini and Claude
Built into Jarvis automatically. Zero local RAM.
Setup:
bashnano ~/.bashrc
Add at bottom:
bashexport GEMINI_API_KEY="PASTE-YOUR-GEMINI-API-KEY-HERE"
export CLAUDE_API_KEY="PASTE-YOUR-CLAUDE-API-KEY-HERE"
Save with CTRL+X then Y then ENTER. Then:
bashsource ~/.bashrc
Cloud AI Troubleshooting:
ProblemFixGemini not responding in JarvisRun echo $GEMINI_API_KEY — if blank run source ~/.bashrcAPI key expiredGenerate new key at aistudio.google.comRate limit hitWait 60 seconds. Free tier has limits.Claude not respondingVerify key at console.anthropic.comKeys disappear after restartRun source ~/.bashrc at start of every session

🔐 IX. GitHub PAT Cloud Sync
Step 1 — Generate PAT:

github.com → Profile → Settings → Developer settings
Personal access tokens → Tokens classic
Generate new token — Note: Termux-Workbench-Push
Expiration: 90 days — Check repo
Generate — COPY IMMEDIATELY

Step 2 — Store securely:
bashmkdir -p ~/.secrets && chmod 700 ~/.secrets
echo "PASTE-YOUR-PAT-HERE" > ~/.secrets/github_pat.txt
chmod 600 ~/.secrets/github_pat.txt
Step 3 — Load PAT:
bashexport GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
Step 4 — Set remote URL:
bashgit remote set-url origin https://YOUR-GITHUB-USERNAME:${GITHUB_PAT}@github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git
Step 5 — Push:
bashgit add . && git commit -m "Sync — YOUR-GITHUB-USERNAME" && git push origin master
PAT Troubleshooting:
ProblemFixAuthentication failedRegenerate PAT and run Steps 2-4 againPush rejectedRun git pull origin master first then pushFatal not a git repositorycd ~/Android-mobile-cybersecurity-workbenchRemote already existsgit remote remove origin then run Step 4PAT expiredGenerate new 90 day token and repeat Steps 2-4PAT accidentally committedImmediately revoke on GitHub. Generate new one.Divergent branchesgit config pull.rebase false && git pull origin master --no-edit && git push origin master

🛰️ X. Operational Commands
bash# Network Discovery
nmap -sn 192.168.1.0/24
# Full Port Scan
nmap -A 192.168.1.1
# Save Scan to Vault
nmap -oN Vault/Scans/audit_$(date +%Y%m%d).txt 192.168.1.1
# Packet Capture
tshark -i wlan0 -w Vault/PCAPs/capture_$(date +%Y%m%d).pcap
# Read Capture
tshark -r Vault/PCAPs/capture_$(date +%Y%m%d).pcap
# Open Capture in Wireshark X11
DISPLAY=:1 wireshark Vault/PCAPs/capture_$(date +%Y%m%d).pcap &
# Wake Jarvis
python3 scripts/jarvis.py
# Wake full Bunker
bunker
# Sync to GitHub
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt) && git add . && git commit -m "Audit sync $(date +%Y-%m-%d) — CK-Bachoo" && git push origin master
Operational Commands Troubleshooting:
ProblemFixnmap not foundpkg install nmap -ytshark not foundEnter Kali. apt install tshark -ygit push failsexport GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)Vault directory missingmkdir -p Vault/Scans Vault/PCAPs Vault/LogsWireshark not opening in X11Make sure X11 is running first

⚡ XI. Wake and Close Commands
🎯 Choose Your Operating Mode
Mode 1 — Full Automation (Recommended):
bashbash scripts/set_wakeword.sh
Then type your wake word every session. Example: bunker
Mode 2 — Manual Control: Run each tool individually from commands below.
Mode 3 — Terminal Only: Skip X11 entirely. Lightweight. Best for low battery.
WAKE COMMANDS
bash# Wake environment
source ~/.bashrc && export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt) && cd ~/Android-mobile-cybersecurity-workbench
# Wake X11
termux-x11 :1 & DISPLAY=:1 xfce4-session &
# Wake Jarvis
python3 scripts/jarvis.py
# Wake Kali
proot-distro login kali
# Wake Ollama — alone only
ollama serve &
# Wake Wireshark in X11
DISPLAY=:1 wireshark &
# Wake everything at once
bunker
CLOSE COMMANDS
bash# Close Jarvis
pkill -f jarvis.py
# Close X11
pkill xfce4-session && pkill termux-x11
# Close Ollama
pkill ollama
# Close Kali
exit
# Nuclear — close everything
pkill -9 -u $(whoami)
# Safe full shutdown and sync
pkill -f jarvis.py && pkill ollama && pkill xfce4-session && pkill termux-x11 && git add . && git commit -m "End of session — CK-Bachoo" && git push origin master
Wake and Close Troubleshooting:
ProblemFixWake word not recognizedRun source ~/.bashrc then try againX11 black after wakeAcquire wakelock from notification barJarvis silent after wakeCheck termux-api mic permissionsCannot close frozen X11Run pkill -9 -u $(whoami) nuclear optionWake word gone after restartRun source ~/.bashrc to reload aliasesEverything running too slowClose Ollama first. It consumes all RAM.

🌡️ XII. Thermal Safety Protocol
Check temperature:
bashcat /sys/class/thermal/thermal_zone0/temp
Divide by 1000 for Celsius. 45000 = 45C.

Safe: Below 40C
Caution: 40C to 45C — reduce workload
Danger: Above 45C — kill switch immediately

Thermal kill switch:
bashpkill -9 -u $(whoami)
Monitor every 30 seconds:
bashwhile true; do
  TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
  echo "Temp: $((TEMP/1000))C"
  sleep 30
done
Press CTRL+C to stop.
Thermal Troubleshooting:
ProblemFixPhone hot during Nmap scanNormal for intensive scans. Monitor temp. Stop above 45C.Phone hot with OllamaExpected. Stop immediately above 45C.Phone hot with X11 plus JarvisDisable 5G. Use Wi-Fi only during sessions.Thermal sensor not foundTry cat /sys/class/thermal/thermal_zone1/tempPhone restarts from heatCool 10 minutes. Enable airplane mode during heavy ops.Battery drains fastAcquire wakelock AND plug in during long sessions.

🔧 XIII. Full Troubleshooting Guide
Termux Issues
ProblemFixpkg update failsRun termux-change-repo and select different mirrorPackage not foundRun pkg update first then retryStorage permission deniedRun termux-setup-storage and tap AllowTermux killed by AndroidDisable battery optimization in SettingsCommand not found after installClose and reopen Termux. Run source ~/.bashrcTermux crashes on openClear app cache in Android Settings → Apps → Termux
Git Issues
ProblemFixFatal not a git repositorycd ~/Android-mobile-cybersecurity-workbenchAuthentication failedRegenerate PAT and run git remote set-url againPush rejectedRun git pull origin master first then pushDivergent branchesgit config pull.rebase false && git pull origin master --no-edit && git push origin masterMerge conflictRun git status. Edit conflicted files. git add . then commit.Accidental commit of secretsImmediately revoke PAT. Generate new one.
X11 Issues
ProblemFixBlack screenClose Termux-X11 app. Reopen. Run termux-x11 :1 &GUI freezes immediatelyAcquire wakelock from notification bar firstProcess killedBattery optimization must be disabledDisplay errorRun export DISPLAY=:1 before any GUI commandCannot find xfce4pkg install xfce4 -yX11 and Jarvis conflictRun bash scripts/bunker_wake.sh — it sequences them correctly
Kali Issues
ProblemFixInstall hangsCTRL+C then proot-distro remove kali then reinstallapt not foundYou are not inside Kali. Run proot-distro login kaliTool not foundapt update && apt install [toolname] -y inside KaliKali environment brokenproot-distro remove kali then proot-distro install kali
Network Issues
ProblemFixNmap permission deniedUse -sn for ping scan without rootNo hosts foundVerify same network. Check subnet.tshark no interfacesRun termux-setup-storage and grant permissionsCannot reach GitHubCheck Wi-Fi. Try ping github.com
Jarvis and AI Issues
ProblemFixJarvis not hearing voiceCheck Android mic permissions for Termux-APIGemini API rate limitWait 60 seconds. Free tier has limits.Ollama out of memoryClose all other apps. Ollama needs full 12GB.Wake word not workingRun source ~/.bashrc then try againAPI keys not loadingRun source ~/.bashrc at start of every session

💼 XIV. Business Integration Guide
This repository proves enterprise-level cybersecurity runs on a $400 mobile device.
Use Cases:

Field security audits — no laptop required
Rapid deployment in resource-constrained environments
Mobile SOC operations with voice AI command interface
AI-assisted threat analysis via Jarvis plus Gemini plus Claude
Voice-commanded network scanning via Jarvis plus Nmap
Training environments on any Android device
Disaster recovery — rebuild entire lab from one GitHub clone

What this architecture proves:

Zero Trust security enforced from a mobile device
Voice AI command interface with confirmation gates
Full packet capture and analysis via Wireshark and tshark
Vulnerability scanning via Nmap and Metasploit
AI-assisted operations via Jarvis, Gemini, Claude, Ollama
Cloud synchronization with immutable audit trail on GitHub
Reproducible — any team member clones and deploys in 30 minutes

Business Integration Troubleshooting:
ProblemFixTeam member cannot cloneVerify repo is Public on GitHubWake word conflicts with teamEach operator runs set_wakeword.sh independentlyVault data needs sharingCopy specific files from Vault manually. Never git add Vault.Jarvis API costsGemini free tier handles most operations. Monitor at aistudio.google.com
Integration contact: github.com/CK-Bachoo
Operator: Bachoo, C. K. | Navy Veteran | Dual Google/CompTIA A+ | Innovation Fellow | New York IF-CS-26 | AI Architect | Principal Security Engineer (Purple Team & GRC)

🏅 XV. Professional Verification
FieldDetailsOperatorC.K. BachooStatusNavy VeteranCredentialsDual Google/CompTIA A+CohortNew York IF-CS-26Current RoleInnovation FellowOperational TierPurple Team (Offensive/Defensive Ops)ComplianceNIST CSF / GRC / IT Audit ReadyInstitutionThe Knowledge House — New YorkEducationPer Scholas — CompTIA A+ Program — Feb 2025 to May 2025CertificationCompTIA A+ ce — Issued May 2025 — Expires May 2028CertificationGoogle IT Support Professional Certificate — CourseraCertificationGoogle CompTIA Dual Credential — Coursera — Apr 2025CertificationGoogle AI Essentials Specialization — Google — Feb 2026CertificationJunior Cybersecurity Analyst Career Path — Cisco Networking Academy — Mar 2025CertificationNetwork Defense — Cisco Networking Academy — Jan 2025CertificationEndpoint Security — Cisco Networking Academy — Jan 2025CertificationIntroduction to Cybersecurity — Cisco — Dec 2024CertificationOperating Systems Basics — Cisco — Dec 2024CertificationComputer Hardware Basics — Cisco — Dec 2024CertificationGovernance Risk and Compliance GRC and Data Privacy — Udemy — Apr 2025CertificationIdentify and Prevent Phishing Attacks — Udemy — Apr 2025CertificationMicro-Certification Welcome to ServiceNow — ServiceNow — Apr 2025Team AlignmentRed Team Offense — Blue Team Defense — Purple Team Collaboration — Gold Team GRCAI IntegrationAI-Orchestrated Security Operations — Gemini — Claude — Ollama — Jarvis Voice AI ArchitectPlatformSamsung Galaxy Note 20 Ultra — Exynos 990 — 12GB RAM — 256GB + 512GB MicroSDGitHubgithub.com/CK-BachooLinkedInlinkedin.com/in/ckbachooStatusMission Ready — March 2026
"The mission does not wait for better equipment." — C.K. Bachoo, 2026 ⚓🫡

XVI. Voice-Sec Terminal & Automation Suite 🤖
ComponentScriptStatusPII Sanitizerscripts/privacy_guard.pyDEPLOYEDPort Sentry / Trap-Door Triggerscripts/port_harden.pyDEPLOYEDTrap-Door Air-Gapscripts/air_gap_isolate.pyDEPLOYEDOSINT Recon Agentscripts/osint_agent.pyDEPLOYEDTTP Log Analyzerscripts/threat_hunt_logs.pyDEPLOYEDNIST Audit Enginebunker_audit.shDEPLOYED
A. Automation Suite Architecture
The Bunker's Python automation suite operates on a single architectural constraint: zero third-party dependencies. Every script runs on Python's standard library only, eliminating pip install failures, RAM spikes, and Android Signal 9 (OOM) kills on the Exynos 990.

privacy_guard.py: Scrubs Student IDs, emails, API keys, PAT tokens, and public IP addresses from outgoing log files before every GitHub push. Safe private ranges (127.x, 10.x, 192.168.x) are whitelisted and pass through untouched. Operates on a named input file — never recursively rewrites the repo.
port_harden.py: Continuous port sentry polling every 15 seconds. Monitors Port 8022 (SSH) and Port 8080 (AI Server) for unauthorized IP bindings using ss with netstat fallback. Any binding outside 127.0.0.1 / ::1 / 0.0.0.0 immediately triggers air_gap_isolate.py.
air_gap_isolate.py: Trap-Door execution layer. Drops wlan0 and all rmnet_data* interfaces via ip link set down, then zeroes out ~/.bash_history and ~/.git-credentials. Includes --dry-run flag for safe testing without live network disruption. Non-root limitation documented honestly: interface drop is logged and operator is instructed to toggle Airplane Mode if root is unavailable.
osint_agent.py: Passive recon only. Performs DNS resolution, multi-record dig enumeration (A/AAAA/MX/TXT/NS/CNAME), WHOIS lookup, and TCP connect port probe on 10 common ports — no nmap required, no root required. Saves timestamped report to Vault/Logs/ automatically.
threat_hunt_logs.py: Read-only TTP log analyzer. Scans access logs against 18 IoC patterns across six categories: ShinyHunters/Canvas-specific, SQL injection (4 variants including time-based blind), directory traversal, sensitive file probes, command injection/RCE, and scanner fingerprints. Outputs severity-sorted (CRITICAL/HIGH/MEDIUM) color-coded terminal report and saves clean copy to Vault/Logs/.
bunker_audit.sh: NIST CSF 2.0 compliance check engine. Verifies root status, ADB daemon state, VPN tunnel interface, Vault/.gitignore protection, active listening ports, and full automation script arsenal presence. Saves timestamped audit report to Vault/Logs/.

B. Deployment Commands
bash# Make scripts executable
chmod 700 scripts/*.py && chmod +x bunker_audit.sh

# Run PII sweep before any push
python3 scripts/privacy_guard.py Vault/Logs/access.log

# Start port sentry (runs continuously)
python3 scripts/port_harden.py &

# Test air gap safely — no live network disruption
python3 scripts/air_gap_isolate.py --dry-run

# Run OSINT recon on a target you own
python3 scripts/osint_agent.py example.com

# Hunt for IoCs in access log
python3 scripts/threat_hunt_logs.py Vault/Logs/access.log

# Run full NIST audit
bash bunker_audit.sh
C. Script Interaction Map
port_harden.py  ──(breach detected)──▶  air_gap_isolate.py
                                               │
threat_hunt_logs.py  ──(CRITICAL hit)──▶  [operator alert]
                                               │
privacy_guard.py  ──(pre-push sweep)──▶  git push origin master
                                               │
bunker_audit.sh  ──(compliance check)──▶  Vault/Logs/audit_*.txt
Analyst: C.K. Bachoo | Verified: XO | Date: MAY 2026 ⚓🫡

XVII. Threat Intelligence Log: Aeternum C2 (Blockchain C2) 🔗
Threat ActorVectorInfrastructureStatusLenAIC++ Loader (x32/x64)Polygon Mainnet (Smart Contracts)ACTIVE (MAR 2026)
A. Technical Breakdown: "Living off the Chain"
Aeternum C2 represents a shift from centralized servers to immutable, decentralized infrastructure.

C2 Mechanism: Commands are stored as encrypted state variables within Solidity smart contracts. The attacker updates the contract to change the "active" payload (Clipper, Stealer, or RAT).
Communication: Infected endpoints utilize JSON-RPC calls (eth_call) to public nodes (e.g., polygon-rpc.com) to retrieve instructions.
Resilience: Since the "server" is the Polygon blockchain, there is no domain to seize or server to take down.

B. Bunker Countermeasures: Note 20 Ultra / Termux Defense

RPC Traffic Interception (tshark):

bashtshark -i any -Y 'http.request.method == "POST"' -T fields -e http.file_data | grep -E "eth_call|eth_getStorageAt"

Infrastructure Decoupling (DNS Sinkhole):

127.0.0.1 polygon-rpc.com
127.0.0.1 bor-mainnet.polygon.technology

Behavioral Audit: The workbench uses a background cron job to alert if outbound traffic to known Polygon/Ethereum RPC ports (8545, 443) exceeds a 60-second polling threshold, identifying the C2 "heartbeat."

Analyst: C.K. Bachoo | Verified: XO | Date: 21 MAR 2026

XVIII. Forensic Mission Report: Neutralizing DNS Sabotage via OOB ⚓🛡️
Timestamp: March 2026
Threat Vector: DNS Poisoning / Localized Network Sabotage ("Operation Blackout")
Origin: Compromised Local "Wire" (WLAN/Ethernet) at The Knowledge House
A. Incident Analysis (The Attack)

The Vector: Sabotage of local name resolution intended to redirect or isolate cohort traffic.
Observed Effect: Primary "Wire" nodes failed to resolve external domains; manual pathing to /etc/resolv.conf was blocked by OS-level restrictions.
Cybersecurity Domain: Network Security / Incident Response (Remediation).

B. Bunker Countermeasures: Note 20 Ultra SOC

Action: Leveraged the Workbench's independent Spectrum LTE stack (rmnet_data2) for Out-of-Band (OOB) recovery.
Method: Redirected terminal pathing to $PREFIX/etc/resolv.conf to bypass Android kernel-level permission denied errors.
Result: Successful triage of Google Public DNS (8.8.8.8 / 8.8.4.4).
Resilience: The Workbench remained immune to the "Wire" sabotage because it maintains an independent physical and logical gateway.

C. Forensic Conclusion & GRC Verification
The Android Mobile Cybersecurity Workbench proved 100% resilient. While the localized network was compromised, the Workbench utilized its native OOB capabilities to maintain technical integrity and connectivity.
Termux Infrastructure Check
bash~ $ ls -la
drwx------ Android-mobile-cybersecurity-workbench
drwx------ CK-Bachoo
drwx------ Foundations_Lab_Final
drwx------ IF-Cyber-Portfolio
NIST CSF Mobile Audit Execution
bash~/Android-mobile-cybersecurity-workbench $ ./bunker_audit.sh
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
Analyst: C.K. Bachoo | Verified: XO | Date: 23 MAR 2026 ⚓🫡

XIX. Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense 🚨
Threat ActorVectorTargetDeadline / StatusShinyHuntersFree-For-Teacher Exploit / Credential HarvestingCanvas LMS (Student PII)May 6 - May 12, 2026 (ACTIVE EXTORTION)
A. Incident Analysis: The Canvas Breach

The Threat: ShinyHunters compromised the Canvas learning management system, exfiltrating 3.65 TB of data (275M records) including Student IDs, assignments, and private messages. The extortion window closes on May 12.
The Hypothesis: Exfiltrated PII is being leveraged for high-fidelity social engineering, phishing, and credential stuffing attacks against the fellowship cohort.

B. Bunker Countermeasures & Protection
Operating from the Note 20 Ultra "Bunker," I remained completely protected from the SaaS-layer compromise through strict environmental decoupling:

Local Sovereignty: Instead of relying on the compromised Canvas portal, all lab requirements and documentation were served via local Git clones and offline Markdown files.
Jump-Host Isolation: Any necessary downloads originating from Canvas were routed through Google Cloud Shell — an ephemeral, sandboxed environment — preventing any direct connection to my physical hardware.
PrivacyGuard Agent: Used local Gemma 2B via privacy_guard.py to automatically scrub outgoing logs of Student IDs and names before pushing to GitHub, neutralizing the value of any intercepted PII.

C. The "Trap-Door Air-Gap" (Active Defense)
If an attacker managed to bypass the VPN and breach the local Termux environment, the Bunker employs a sovereign "Trap-Door" defense mechanism:

The Logic: If the automated port sentry (port_harden.py) detects an unauthorized IP binding to Port 8022 (SSH) or Port 8080 (AI Server), it instantly triggers the air_gap_isolate.py protocol.
The Execution: The device immediately drops all network interfaces, severing the connection to the outside world.
The Result: The attacker is locked inside a dead, disconnected session. Simultaneously, the system flushes volatile memory, wiping ~/.bash_history and ~/.git-credentials. The operator is no longer in the same "room," and the attacker is left holding an empty, isolated shell.

Analyst: C.K. Bachoo | Verified: XO | Date: MAY 2026
