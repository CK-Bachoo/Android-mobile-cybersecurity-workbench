🛡️ Mobile Cybersecurity: Independent Purple Team Lab Environments on Constrained Android Hardware

(Samsung Note 20 Ultra 5G Exynos 990 + Termux App + Chrome Browser + Google Cloud Shell + Azure + AWS + GitHub)

This is a live, operational security workbench built and run entirely on a Samsung Galaxy Note 20 Ultra. No shortcuts. Built by a Navy veteran and Cybersecurity Innovation Fellow to prove enterprise-inspired Purple Team workflows are a function of discipline, not hardware.

### Core Strengths
* Purple Team operations and defensive automation
* Mobile-to-cloud security pipelines
* AI-assisted analysis and documentation
* Zero Trust enforcement in resource-limited environments

### Current Deployment
* The Knowledge House NY Innovation Fellowship (IF-CS-26)
* Full Portfolio: https://github.com/CK-Bachoo/IF-Cyber-Portfolio
* Mobile SOC Rig: https://github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench

Open to connecting on mobile security, DevSecOps, automation, and Purple Team topics.

---

## Android Mobile Cybersecurity Workbench: The Bunker SOP 🛡️

* **Role:** 🛡️Cybersecurity Innovation Fellow. Purple Team Ops | Mobile-to-Cloud Lab Environments | IT Support & AI Security Architect | Navy Veteran
* **Deployment:** Samsung Note 20 Ultra Exynos 990 12 GB RAM 256 GB internal storage with exp. SD card storage & Legacy MacBook Pro 13 2011 High Sierra (Decommissioned Feb 1, 2025 - Black Screen of Death)
* **Operator:** | Bachoo, C. K. | Cybersecurity Innovation Fellow NY IF-CS-26 | The Knowledge House Bronx, NY
* **DEFCON Status:** CHARLIE (Active Threat: ShinyHunters May 12 Deadline)

---

## 00 / Core Directives & GodMode AI Orchestration

### GodMode AI & OpenClaw Agent Integration
The Bunker utilizes a native GodMode AI orchestration framework to manage multiple LLMs simultaneously. This prevents vendor lock-in, ensures operational continuity during network degradation, and enables multi-model cross-validation for complex threat hunting.

* **GodMode Chat Browser Initialization (smol-ai):** The GodMode webview wrapper is deployed to access ChatGPT, Claude 3.5, Bard, Bing, and Gemini 1.5 Pro concurrently.
* **Execution (The Agile Pivot):** `cd ~/GodMode && python -m http.server 8000` (Pivoted from heavy NodeJS/npm dependencies to a native Python HTTP server for "Intelligent Laziness" resource optimization, eliminating compiler overhead).
* **Architecture Context:** Running multiple heavy web-apps natively in Android Chrome crashes the Exynos 990 due to RAM constraints. The GodMode wrapper bypasses standard browser memory limits, creating a unified, lightweight interface for all API-less chat models, completely tunneled through our encrypted VPN.
* **OpenClaw / PicoClaw Agentic Automation:** Local AI agents deployed via OpenClaw to perform autonomous log parsing, system audits, and threat hunting without requiring human-in-the-loop for every command.
* **Security Constraint (MCP Security 101):** The Model Context Protocol (MCP) acts as the API layer for these agents. To prevent privilege escalation (e.g., tool poisoning or unauthorized system writes), all MCP tools are strictly sandboxed.
* **Enforcement:** Implemented Client-Side Validation to strip Prompt Injection vectors before execution, and the Principle of Least Privilege is strictly enforced on the Termux environment (e.g., agents cannot write to `/var/log`, only read).

### Local Fallback (Ollama + Llama 3.2 / Gemma 2B)
When external networks are compromised or air-gapped, the Bunker relies on 100% local, offline inference to parse sensitive logs without leaking proprietary data to cloud providers.

* **Hardware Pool:** 12GB LPDDR5 RAM.
* **Execution:** `ollama serve & ollama run gemma:2b`
* **Constraint:** Never run Ollama simultaneously with X11/Jarvis. The Android kernel's Signal 9 (Out of Memory) Phantom Process Killer will terminate the session. Graceful teardown requires `pkill ollama` to flush RAM.

---

## 01 / Tactical Phases (Canvas Aligned)

### Phase 0: System Foundations (S01 - S03)
* **CTI & Navigation:** Linux Scavenger Hunt & Access Control Hardening (`harden.sh`). Mastered the Filesystem Hierarchy Standard (FHS) to locate and extract hidden tokens from `/var/tmp/.blackout/`.
* **Permissions:** Applied the Read-Write-Execute (RWX) matrix (700 for private, 755 for scripts, 644 for standard files).
* **Text Plumbing:** Advanced log filtering using Grep, Sed, and Awk. Extracted top malicious IP addresses from a 10,000-line Apache `access.log` using standard streams.

### Phase 1: Network & Protocol Defense (S04 - S06)
* **Operation Broken Link (L1-L3):** Restored Layer 3 connectivity by diagnosing a missing default route and manually rebuilding the routing table (`sudo ip route add default via 10.0.0.1`).
* **Operation Grid Lock (Subnetting Crucible):** Bypassed isolation caused by a CIDR mismatch. Expanded the subnet mask from a `/26` to a `/24` to include the gateway, allowing the terminal to successfully ping `10.50.50.1`.
* **Operation Hidden Door:** Protocol interrogation using `ss -tuln` and `curl -I localhost:8080`. Remediated local DNS deception by purging poisoned entries in `/etc/hosts` to restore legitimate resolution for Google.

### Phase 2: Virtualization & Automation (S07 - S09)
* **Infrastructure:** Sandboxed Debian via Proot-Distro in Termux, replacing resource-heavy Type-2 Hypervisors (VirtualBox/VMware).
* **The Forge:** Developed Python-based security automation (`port_check.py`, `log_filter.py`, `firewall_bot.py`). Implemented `try/except` error handlers to build graceful failure into scripts, ensuring tools don't crash when logs are missing.

### Phase 3: Cross-Platform Zero-Trust Enclave (Proton VPN + Kill Switch)
* **Hardening Obsolete Infrastructure (MacBook Pivot):** Enforced a Strict Kill Switch on a legacy MacBook Pro running macOS High Sierra (End-of-Life). If the encrypted tunnel drops for a millisecond, the network adapter is severed at the hardware level, effectively "air-gapping" the vulnerable machine from the local network while maintaining an AES-256 shield.
* **The Mobile Bunker (Note 20 Ultra):** Implemented Layer 3 Traffic Isolation via Android's "Block connections without VPN" kernel setting. The Termux terminal now operates silently. ISP and local eavesdroppers cannot sniff SSH sessions or cloud-bridge payloads.
* **Secure AI Orchestration:** By serving the GodMode UI locally over Python and tunneling it through Proton, we achieved a Hybrid Intelligence Pipeline. Heavy compute is securely passed to Gemini/Claude, while sensitive telemetry is analyzed offline by Gemma 2B.

---

## 02 / Hardware Benchmarking & Field Reports

### [MISSION]: MiroFish-Offline Red/Blue Swarm (Terminal 0500)

* **Status:** SUCCESSFUL TASK EXECUTION / STRATEGIC HARDWARE DECOMMISSIONING
* **Hardware:** Samsung Note 20 Ultra 5G (Exynos 990 / 12GB RAM / 256GB Storage / SD Expanded Vault)
* **Conditions:** 20% SOC | No Sleep | Manual OS Override (Phantom Process Killer Bypass)

#### 1. Miro-Swarm-Offline: Terminal Functionality
* **The Local Handshake:** The terminal displayed active negotiation between the Ollama (Tactical Brain) and the Miro-Swarm (Orchestra).
* **The Mechanism:** Executed via local loopback. One terminal instance acted as the "Red" (Offensive) agent querying the Knowledge Graph, while the second instance provided "Blue" (Defensive) feedback — all without an internet handshake.
* **Data Flow:** Logic weights were pulled from the SD Expanded Vault into the 12GB LPDDR5 RAM pool, bypassing standard Android storage latency.

#### 2. Tactical Deployment & System Overrides
* **Technical Logic:** Encountered Signal 9 (OOM) execution kills and pip-metadata locks due to aggressive Android system background limits. Executed manual dependency reconciliation and metadata overrides. Bypassed the Android Phantom Process Killer to force-initialize the swarm on a 20% SOC battery baseline.
* **(Layman's Version):** The phone's software kept trying to "kill" the project to save power. I manually forced it to stay awake and broke through the system's "locks" to finish the install on a dying battery. The Offensive and Defensive AI teams successfully started working together on the terminal for the first time.

#### 3. Hardware Preservation & Uninstall Logic
* **The Audit:** System maintained a 32°C battery baseline during active GraphRAG builds. This is the thermal "Red Line" for an Exynos 990.
* **The Decision:** UNINSTALLED & PURGED. Sustained heat over time from a recursive AI swarm would ruin the Mobile Cybersecurity Workbench. I proved the "Orchestra" works; then I decommissioned to save the rig.

#### 4. Decommissioning Forensic Checklist
* [x] Full Uninstall: Purged 2GB+ of recursive dependencies and model weights.
* [x] Port Sanitization: 7474 (Neo4j), 5001 (Backend), 3000 (Vite) verified CLOSED.
* [x] SD Vault Integrity: Verified vault remains secure and uncompromised post-purge.
* [x] Forensic Clear: `ps aux` confirms no ghost processes remaining.

---

## 03 / Infrastructure as Code & Desktop Rendering

### Termux-X11 & Hardware Acceleration
Bypassing standard VNC overhead to run XFCE4 natively on Android.

* **Initialization:** `termux-x11 :1 & DISPLAY=:1 xfce4-session &`
* **GPU Acceleration:** Virglrenderer deployed to bypass llvmpipe CPU rendering, allowing graphical analysis tools (Wireshark, Autopsy) to run smoothly using the device's native Mali GPU.
* **Audio Routing:** PulseAudio TCP bridge established via `PULSE_SERVER=tcp:127.0.0.1:4713` (Pre-loaded `libskcodec.so` via `LD_PRELOAD` to fix Samsung OneUI 6.1 codec crashes).
* **x86 Emulation:** Box86/Box64 and Wine installed via proot to execute legacy Windows/Linux x86 security binaries on the ARM64 architecture, bridging the gap between mobile hardware and enterprise software.

---

## ⚙️ RAW WORKBENCH LOGS & HISTORICAL SPECS BELOW: 🛡️
**ARM64 Mobile-to-Cloud Security Workbench (The Bunker)**  
**Operator:** Bachoo, C. K. | Navy Veteran | Dual Google/CompTIA A+ | Innovation Fellow | New York IF-CS-26  
**Platform:** Samsung Galaxy Note 20 Ultra | Termux | Mobile-Only Architecture  
**Mission:** Scale enterprise-level cybersecurity workflows on constrained mobile hardware.  
*"The mission does not wait for better equipment." — C.K. Bachoo ⚓*

### 📋 Table of Contents
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

---

### ⚙️ I. Hardware Matrix

| Device | RAM | Status |
| :--- | :--- | :--- |
| Samsung Galaxy Note 20 Ultra 5G | 12GB | Primary — Fully Verified |
| Samsung S21 Ultra | 12GB | Verified |
| Samsung S22/S23/S24/S25/S26 Ultra | 12GB | Verified |
| Samsung Z-Fold 3/4/5/6/Trifold | 12GB | Verified |
| Google Pixel 6/7/8/9 Pro/Fold | 8-12GB | Verified |
| iPhone (iOS) | Any | Codespaces + iSH/UTM Pivot |

#### Minimum Requirements
* Android 10 or higher
* 8GB RAM minimum (12GB recommended)
* 5G or Fiber Wi-Fi for GitHub sync and cloud AI
* 256GB internal storage or 1TB MicroSD for Vault and PCAPs
* S-Pen recommended for Wireshark packet precision on Note devices

#### Hardware Troubleshooting
* **Problem:** Phone overheats during setup  
  **Fix:** Stop all processes. Cool device. Restart one tool at a time.
* **Problem:** Not enough storage  
  **Fix:** Move Vault to MicroSD. `ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/Vault`
* **Problem:** Android version too old  
  **Fix:** Codespaces browser fallback works on any Android version
* **Problem:** MicroSD not detected  
  **Fix:** Settings → Device Care → Storage → check SD card mount status

---

### ✅ II. Pre-Flight Checklist

Before starting run through this list:
* [x] Termux installed from F-Droid (not Play Store)
* [x] Termux-API installed from F-Droid
* [x] Termux-X11 companion app installed
* [x] Battery above 50 percent
* [x] Connected to Wi-Fi
* [x] Storage permission granted to Termux
* [x] Battery optimization DISABLED for Termux in Android Settings
* [x] GitHub account created at github.com
* [x] At least 4GB free storage
* [x] MicroSD card inserted and mounted (recommended)
* [x] Gemini API key saved at `~/.secrets/gemini_api_key.txt`

#### How to disable battery optimization
Android Settings → Apps → Termux → Battery → Unrestricted  
*Do the same for Termux-API and Termux-X11*

#### Pre-Flight Troubleshooting
* **Problem:** Termux from Play Store installed  
  **Fix:** Uninstall it. Install from F-Droid only. Play Store version is outdated.
* **Problem:** Battery optimization keeps re-enabling  
  **Fix:** Samsung One UI resets this. Check after every phone restart.
* **Problem:** No F-Droid on phone  
  **Fix:** Go to f-droid.org in browser. Download and install APK directly.
* **Problem:** MicroSD not showing in Termux  
  **Fix:** Run `termux-setup-storage` and tap Allow

---

### 🚀 III. Base Initialization

Open Termux. Run each command one at a time. Wait for each to finish.

**Step 1 — Grant storage access:**
```bash
termux-setup-storage
A popup will appear. Tap Allow.Step 2 — Update and upgrade:Bashpkg update -y && pkg upgrade -y
Step 3 — Install all required tools:Bashpkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y
Step 4 — Install Python security packages:Bashpip install requests scapy paramiko
Step 5 — Verify everything installed correctly:Bashpython --version && git --version && nmap --version && ssh -V
All four should return version numbers.Step 6 — Clone this repository:Bashcd ~ && git clone --depth 1 [https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git](https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git) && cd Android-mobile-cybersecurity-workbench
Replace YOUR-GITHUB-USERNAME with your actual GitHub username.Step 7 — Set your wake word:Bashbash scripts/set_wakeword.sh
Choose any word. That word launches X11 and Jarvis together.Base Initialization TroubleshootingProblem: pkg update failsFix: Run termux-change-repo and select a different mirrorProblem: Package not foundFix: Run pkg update first then retry installProblem: Storage permission deniedFix: Run termux-setup-storage and tap AllowProblem: pip install failsFix: Run pip install --upgrade pip firstProblem: git clone failsFix: Check Wi-Fi. Verify GitHub username is correct.Problem: Python not found after installFix: Close and reopen Termux. Run source ~/.bashrc🛡️ IV. OPSEC Data IsolationAll sensitive scan results, packet captures, and logs stay in the Vault. Vault is never committed to GitHub.Android-mobile-cybersecurity-workbench/
├── Vault/
│   ├── Scans/
│   ├── PCAPs/
│   ├── Logs/
│   └── Evidence/
└── scripts/
Create Vault structure:Bashmkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence
Add Vault to gitignore:Bashecho "Vault/" >> .gitignore && echo "*.pcap" >> .gitignore && echo "*.cap" >> .gitignore && echo ".secrets/" >> .gitignore && git config --local core.excludesfile .gitignore
Verify Vault is protected:Bashcat .gitignore && git status
Vault folder should NOT appear in git status output.Move Vault to MicroSD for physical isolation:Bashmkdir -p /sdcard/Vault && ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/Vault
OPSEC RulesNever commit real IP addresses to GitHubNever commit API keys or PAT tokensNever commit pcap files — keep in Vault onlyAlways use YOUR-GITHUB-USERNAME placeholder in public docsRevoke PAT immediately if accidentally exposedOPSEC TroubleshootingProblem: Vault appearing in git statusFix: Run git rm -r --cached Vault/ then commitProblem: Secrets accidentally committedFix: Immediately revoke PAT on GitHub. Rotate all keys.Problem: gitignore not workingFix: Run git config --local core.excludesfile .gitignoreProblem: Vault files too large for phoneFix: Move Vault to MicroSD using symlink above.Problem: secrets folder exposedFix: Run chmod 700 ~/.secrets && chmod 600 ~/.secrets/*🔑 V. SSH Keys for GitHubSSH keys give you passwordless GitHub access that never expires.Step 1 — Generate your key:Bashssh-keygen -t ed25519 -C "YOUR-GITHUB-USERNAME"
Press ENTER three times to accept all defaults.Step 2 — Display your public key:Bashcat ~/.ssh/id_ed25519.pub
Step 3 — Copy YOUR output. Never share it publicly.Step 4 — Add to GitHub:Open github.com in browserProfile photo → SettingsSSH and GPG keys → New SSH keyTitle: Note20Ultra-TermuxPaste YOUR keyTap Add SSH keyStep 5 — Verify connection:Bashssh -T git@github.com
Should return: Hi YOUR-GITHUB-USERNAME! You've successfully authenticated.SSH TroubleshootingProblem: Permission deniedFix: Make sure you copied the .pub file not the private keyProblem: Connection refusedFix: Run eval $(ssh-agent -s) then ssh-add ~/.ssh/id_ed25519Problem: ssh not foundFix: Run pkg install openssh firstProblem: Key not accepted by GitHubFix: Delete the key on GitHub and re-add itProblem: Authentication keeps failingFix: Generate a new key pair and start fresh🖥️ VI. X11 Graphical InterfaceX11 gives you a full Linux desktop GUI on your phone screen. Required for Wireshark, VS Code visual editing, and multi-window operations.Install X11:Bashpkg install xfce4 xfce4-goodies x11-repo xorg-xrandr -y
🎯 Choose Your Operating ModeMode 1 — Full Automation (Recommended): Set your wake word once. Type it. Everything launches. Jarvis AI online. X11 desktop open. Zero Trust active.Bashbash scripts/set_wakeword.sh
Then type your wake word every session. Example: bunkerMode 2 — Manual Control: Skip the wake word. Run each tool individually. Use the manual commands below. No AI. No automation.Mode 3 — Terminal Only: Skip X11 entirely. Run everything in Termux terminal. Lightweight. Fast. Best for low battery or quick operations.HOW TO WAKE X11Automatic — wake word:Bashbunker
Replace bunker with your personal wake word.Manual — step by step:Bashtermux-x11 :1 & DISPLAY=:1 xfce4-session &
Then open Termux-X11 app. Acquire wakelock from notification bar.HOW TO LAUNCH APPS IN X11BashDISPLAY=:1 wireshark &
DISPLAY=:1 thunar &
DISPLAY=:1 xterm &
DISPLAY=:1 [appname] &
HOW TO CLOSE X11Bashpkill xfce4-session && pkill termux-x11
Nuclear option if frozen:Bashpkill -9 -u $(whoami)
X11 Wake Lock — CRITICALSwipe down notification barFind Termux notificationTap Acquire WakelockDo this EVERY TIME or X11 freezes within minutes.X11 TroubleshootingProblem: Black screenFix: Close Termux-X11 app. Reopen. Run termux-x11 :1 & againProblem: GUI freezes immediatelyFix: Acquire wakelock from notification bar firstProblem: Process killed by AndroidFix: Disable battery optimization for Termux in SettingsProblem: Display variable errorFix: Run export DISPLAY=:1 before any GUI commandProblem: xfce4-session not foundFix: Run pkg install xfce4 -y againProblem: Termux-X11 app crashesFix: Reinstall from F-DroidProblem: Wake word not workingFix: Run source ~/.bashrc then try againProblem: X11 and Jarvis not starting togetherFix: Run bash scripts/bunker_wake.sh directly🧪 VII. Kali Linux VirtualizationKali runs as a full Linux environment inside Termux using proot. No root required.Install Kali:Bashproot-distro install kali
Downloads about 500MB. Takes several minutes on Wi-Fi.Enter Kali:Bashproot-distro login kali
Your prompt changes to root@localhost.Update and install security tools:Bashapt update -y && apt install nmap wireshark-cli tshark metasploit-framework sqlmap nikto -y
Verify tools:Bashnmap --version && tshark --version && msfconsole --version
Exit Kali:Bashexit
Run single command without entering Kali:Bashproot-distro login kali -- nmap -sn 192.168.1.0/24
Kali TroubleshootingProblem: Install hangs at 0 percentFix: CTRL+C then proot-distro remove kali then reinstallProblem: apt not foundFix: You are not inside Kali. Run proot-distro login kaliProblem: Tool not foundFix: apt update && apt install [toolname] -y inside KaliProblem: Kali environment corruptedFix: proot-distro remove kali then proot-distro install kaliProblem: Cannot push from inside KaliFix: Exit Kali first. Push from Termux.Problem: Metasploit takes too longFix: Normal. First launch downloads dependencies. Wait 5 minutes.Problem: No internet inside KaliFix: Exit Kali. Check Wi-Fi. Re-enter Kali.🤖 VIII. AI Stack Deployment & Security ToolingResource Management — Note 20 Ultra 12GB RAMToolRAM UsageTypeSafe to Run Together?Jarvis Voice AI~50MBLocal Python + CloudYES — PrimaryGemini API~0MB localCloud OnlyYES — Built into JarvisClaude AI~0MB localCloud OnlyYES — Built into JarvisX11 Desktop~400MBLocal GUIYES — With JarvisVS Code Codespaces~200MB browserCloud IDEYES — With JarvisWireshark X11~300MBLocal GUIYES — With X11 activeNmap~50MBLocal ScannerYES — LightweightOllama / Gemma 2B4-6GBLocal LLMNO — Run separatelyGolden Rule: Never run Ollama with anything else. Exynos 990 will overheat and 12GB RAM will max out.🎙️ Jarvis Voice AI — Primary Command InterfaceVoice-activated AI built natively on the Note 20 Ultra. Zero Trust gate on all execute commands. All sessions logged to Vault and 512GB MicroSD and GitHub.Hardware this was built for: Note 20 Ultra, Exynos 990, 12GB RAM, 256GB Internal + 512GB MicroSDInstall Jarvis:Bashpkg install termux-api -y && pip install requests
Wake Jarvis manually:Bashcd ~/Android-mobile-cybersecurity-workbench
python3 scripts/jarvis.py
Wake Jarvis automatically with X11:Bashbunker
Jarvis voice commands:Say anything — Jarvis processes via Gemini and respondsSay "hardware check" — thermal and storage diagnosticsSay "scan my network" — suggests nmap command with Zero Trust gateSay "start packet capture" — suggests tshark commandSay "help" — lists all capabilitiesSay "exit" or "shutdown" — clean shutdown with session logStop Jarvis:Bashpkill -f jarvis.py
Jarvis TroubleshootingProblem: No voice input detectedFix: Check termux-api permissions — Microphone must be allowedProblem: TTS not speakingFix: Run termux-tts-speak "test" to verify audioProblem: Gemini not respondingFix: Run echo $GEMINI_API_KEY — if blank run source ~/.bashrcProblem: Phone gets hotFix: Stop Jarvis. Never run with Ollama simultaneouslyProblem: Jarvis loop crashesFix: Run source ~/.bashrc then restart jarvis.pyProblem: Zero Trust gate not hearing confirmFix: Speak clearly. Move closer to mic.Problem: Wake word not launching JarvisFix: Run source ~/.bashrc then try wake word again🔑 Bunker Wake System — One Word Launches EverythingFirst time setup:Bashbash scripts/set_wakeword.sh
Wake WordOperator StylebunkerC.K. Bachoo — OriginalsentinelDefensive posturenighthawkStealth opsfortressMaximum defensesshadowLow profilejarvisClassic AI referenceopsShort and tacticalAfter setup — type your word and hit ENTER:Bashbunker
What happens automatically: Environment and PAT load, X11 server starts, XFCE blue desktop launches, Termux-X11 app opens, Jarvis speaks and goes online.Wake Word TroubleshootingProblem: Wake word not recognizedFix: Run source ~/.bashrc then try againProblem: Wake word launches but X11 is blackFix: Acquire wakelock from notification barProblem: Jarvis does not speak on wakeFix: Check termux-api mic permissionsProblem: Want to change wake wordFix: Run set_wakeword.sh againProblem: Wake word disappeared after restartFix: Run source ~/.bashrc — alias reloads🛰️ Nmap — Network IntelligenceInstall:Bashpkg install nmap -y
Essential commands:Bashnmap -sn 192.168.1.0/24
nmap -sV 192.168.1.1
nmap -A 192.168.1.1
nmap -p 22,80,443,8080 192.168.1.1
nmap -F 192.168.1.1
nmap -oN Vault/Scans/scan_$(date +%Y%m%d_%H%M%S).txt 192.168.1.1
nmap -oA Vault/Scans/scan_$(date +%Y%m%d) 192.168.1.1
Nmap + Wireshark workflow:Bashtshark -i wlan0 -w Vault/PCAPs/nmap_capture.pcap &
nmap -sV 192.168.1.1
pkill tshark
DISPLAY=:1 wireshark Vault/PCAPs/nmap_capture.pcap &
Nmap TroubleshootingProblem: Permission deniedFix: Use -sn ping scan — no root neededProblem: No hosts foundFix: Verify same network. Check subnet.Problem: Scan too slowFix: Add -T4 flag for faster timingProblem: nmap not foundFix: pkg install nmap -yProblem: Results not savingFix: mkdir -p Vault/ScansProblem: SYN scan requires rootFix: Enter Kali proot for root-level scans🦈 Wireshark — Packet AnalysisInstall CLI in Kali:Bashproot-distro login kali && apt install wireshark-cli tshark -y
Essential commands:Bashtshark -D
tshark -i wlan0
tshark -i wlan0 -w Vault/PCAPs/capture_$(date +%Y%m%d_%H%M%S).pcap
tshark -i wlan0 -c 100 -w Vault/PCAPs/capture.pcap
tshark -r Vault/PCAPs/capture.pcap
tshark -i wlan0 -Y "http"
tshark -i wlan0 -Y "dns"
tshark -i wlan0 -Y "ip.addr == 192.168.1.1"
DISPLAY=:1 wireshark Vault/PCAPs/capture.pcap &
Wireshark TroubleshootingProblem: No interfaces foundFix: Run termux-setup-storage and grant permissionsProblem: Permission denied on captureFix: Enter Kali proot for root accessProblem: tshark not foundFix: apt install tshark -y inside KaliProblem: Wireshark GUI not openingFix: Make sure X11 is running and DISPLAY=:1 is setProblem: Capture file too largeFix: Add -c 500 to limit packet countProblem: Cannot read pcap fileFix: Run ls Vault/PCAPs/ to verify path💻 VS Code — Development EnvironmentBash# Open Kiwi browser
# Go to [https://github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench](https://github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench)
# Tap Code → Codespaces → Create codespace on master
VS Code TroubleshootingProblem: Codespace takes too longFix: Close and reopen. Free tier has limits.Problem: Changes not savingFix: Commit and push before closingProblem: Terminal not respondingFix: Refresh the browser tabProblem: Codespace expiredFix: Create a new one — repo is safe on GitHub🖥️ Local AI — OllamaOffline AI. No internet required. Heavy RAM usage. Run ALONE. Never with other tools.Wake Ollama — close everything else first:Bashpkill -f jarvis.py && pkill xfce4-session && pkill termux-x11
ollama serve &
ollama run gemma:2b
Stop Ollama:Bashpkill ollama
Ollama TroubleshootingProblem: Server hangsFix: pkill ollama then ollama serve & againProblem: Out of memoryFix: Close everything else firstProblem: Model download failsFix: Check Wi-Fi. Retry ollama pull gemma:2bProblem: Phone overheatingFix: Stop immediately. pkill ollamaProblem: Response too slowFix: Use smaller model or ensure terminal is not overloaded.Problem: Cannot run with JarvisFix: By design. Close Jarvis first. Ollama needs all 12GB.☁️ Cloud AI — Gemini and ClaudeBuilt into Jarvis automatically. Zero local RAM.Setup:Bashnano ~/.bashrc
Add at bottom:Bashexport GEMINI_API_KEY="PASTE-YOUR-GEMINI-API-KEY-HERE"
export CLAUDE_API_KEY="PASTE-YOUR-CLAUDE-API-KEY-HERE"
Save with CTRL+X then Y then ENTER. Then:Bashsource ~/.bashrc
Cloud AI TroubleshootingProblem: Gemini not responding in JarvisFix: Run echo $GEMINI_API_KEY — if blank run source ~/.bashrcProblem: API key expiredFix: Generate new key at aistudio.google.comProblem: Rate limit hitFix: Wait 60 seconds. Free tier has limits.Problem: Claude not respondingFix: Verify key at console.anthropic.comProblem: Keys disappear after restartFix: Run source ~/.bashrc at start of every session🔐 IX. GitHub PAT Cloud SyncStep 1 — Generate PAT:github.com → Profile → Settings → Developer settings → Personal access tokens → Tokens classic → Generate new tokenNote: Termux-Workbench-PushExpiration: 90 daysScopes: Check repoGenerate — COPY IMMEDIATELYStep 2 — Store securely:Bashmkdir -p ~/.secrets && chmod 700 ~/.secrets
echo "PASTE-YOUR-PAT-HERE" > ~/.secrets/github_pat.txt
chmod 600 ~/.secrets/github_pat.txt
Step 3 — Load PAT:Bashexport GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
Step 4 — Set remote URL:Bashgit remote set-url origin https://YOUR-GITHUB-USERNAME:${GITHUB_PAT}@[github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git](https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git)
Step 5 — Push:Bashgit add . && git commit -m "Sync — YOUR-GITHUB-USERNAME" && git push origin master
PAT TroubleshootingProblem: Authentication failedFix: Regenerate PAT and run Steps 2-4 againProblem: Push rejectedFix: Run git pull origin master first then pushProblem: Fatal not a git repositoryFix: cd ~/Android-mobile-cybersecurity-workbenchProblem: Remote already existsFix: git remote remove origin then run Step 4Problem: PAT expiredFix: Generate new 90 day token and repeat Steps 2-4Problem: PAT accidentally committedFix: Immediately revoke on GitHub. Generate new one.Problem: Divergent branchesFix: git config pull.rebase false && git pull origin master --no-edit && git push origin master🛰️ X. Operational CommandsBash# Network Discovery
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
Operational Commands TroubleshootingProblem: nmap not foundFix: pkg install nmap -yProblem: tshark not foundFix: Enter Kali. apt install tshark -yProblem: git push failsFix: export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)Problem: Vault directory missingFix: mkdir -p Vault/Scans Vault/PCAPs Vault/LogsProblem: Wireshark not opening in X11Fix: Make sure X11 is running first⚡ XI. Wake and Close Commands🎯 Choose Your Operating ModeMode 1 — Full Automation (Recommended):Bashbash scripts/set_wakeword.sh
Then type your wake word every session. Example: bunkerMode 2 — Manual Control: Run each tool individually from commands below.Mode 3 — Terminal Only: Skip X11 entirely. Lightweight. Best for low battery.WAKE COMMANDSBash# Wake environment
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
CLOSE COMMANDSBash# Close Jarvis
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
Wake and Close TroubleshootingProblem: Wake word not recognizedFix: Run source ~/.bashrc then try againProblem: X11 black after wakeFix: Acquire wakelock from notification barProblem: Jarvis silent after wakeFix: Check termux-api mic permissionsProblem: Cannot close frozen X11Fix: Run pkill -9 -u $(whoami) nuclear optionProblem: Wake word gone after restartFix: Run source ~/.bashrc to reload aliasesProblem: Everything running too slowFix: Close Ollama first. It consumes all RAM.🌡️ XII. Thermal Safety ProtocolCheck temperature:Bashcat /sys/class/thermal/thermal_zone0/temp
Divide by 1000 for Celsius. 45000 = 45C.Safe: Below 40°CCaution: 40°C to 45°C — reduce workloadDanger: Above 45°C — kill switch immediatelyThermal kill switch:Bashpkill -9 -u $(whoami)
Monitor every 30 seconds:Bashwhile true; do  TEMP=$(cat /sys/class/thermal/thermal_zone0/temp);  echo "Temp: $((TEMP/1000))C";  sleep 30; done
Press CTRL+C to stop.Thermal TroubleshootingProblem: Phone hot during Nmap scanFix: Normal for intensive scans. Monitor temp. Stop above 45°C.Problem: Phone hot with OllamaFix: Expected. Stop immediately above 45°C.Problem: Phone hot with X11 plus JarvisFix: Disable 5G. Use Wi-Fi only during sessions.Problem: Thermal sensor not foundFix: Try cat /sys/class/thermal/thermal_zone1/tempProblem: Phone restarts from heatFix: Cool 10 minutes. Enable airplane mode during heavy ops.Problem: Battery drains fastFix: Acquire wakelock AND plug in during long sessions.🔧 XIII. Full Troubleshooting GuideTermux IssuesProblem: pkg update failsFix: Run termux-change-repo and select different mirrorProblem: Package not foundFix: Run pkg update first then retryProblem: Storage permission deniedFix: Run termux-setup-storage and tap AllowProblem: Termux killed by AndroidFix: Disable battery optimization in SettingsProblem: Command not found after installFix: Close and reopen Termux. Run source ~/.bashrcProblem: Termux crashes on openFix: Clear app cache in Android Settings → Apps → TermuxGit IssuesProblem: Fatal not a git repositoryFix: cd ~/Android-mobile-cybersecurity-workbenchProblem: Authentication failedFix: Regenerate PAT and run git remote set-url againProblem: Push rejectedFix: Run git pull origin master first then pushProblem: Divergent branchesFix: git config pull.rebase false && git pull origin master --no-edit && git push origin masterProblem: Merge conflictFix: Run git status. Edit conflicted files. git add . then commit.Problem: Accidental commit of secretsFix: Immediately revoke PAT. Generate new one.X11 IssuesProblem: Black screenFix: Close Termux-X11 app. Reopen. Run termux-x11 :1 &Problem: GUI freezes immediatelyFix: Acquire wakelock from notification bar firstProblem: Process killedFix: Battery optimization must be disabledProblem: Display errorFix: Run export DISPLAY=:1 before any GUI commandProblem: Cannot find xfce4Fix: pkg install xfce4 -yProblem: X11 and Jarvis conflictFix: Run bash scripts/bunker_wake.sh — it sequences them correctlyKali IssuesProblem: Install hangsFix: CTRL+C then proot-distro remove kali then reinstallProblem: apt not foundFix: You are not inside Kali. Run proot-distro login kaliProblem: Tool not foundFix: apt update && apt install [toolname] -y inside KaliProblem: Kali environment brokenFix: proot-distro remove kali then proot-distro install kaliNetwork IssuesProblem: Nmap permission deniedFix: Use -sn for ping scan without rootProblem: No hosts foundFix: Verify same network. Check subnet.Problem: tshark no interfacesFix: Run termux-setup-storage and grant permissionsProblem: Cannot reach GitHubFix: Check Wi-Fi. Try ping github.comJarvis and AI IssuesProblem: Jarvis not hearing voiceFix: Check Android mic permissions for Termux-APIProblem: Gemini API rate limitFix: Wait 60 seconds. Free tier has limits.Problem: Ollama out of memoryFix: Close all other apps. Ollama needs full 12GB.Problem: Wake word not workingFix: Run source ~/.bashrc then try againProblem: API keys not loadingFix: Run source ~/.bashrc at start of every sessionDreadnought Console IssuesProblem: dreadnought_console.sh exits immediatelyFix: Run chmod +x scripts/dreadnought_console.shProblem: Environment variables not loadingFix: Verify files exist in ~/.secrets/Problem: Console launches but tools missingFix: Run pkg update && pkg upgrade -yProblem: Safe mode required repeatedlyFix: Close X11 or Ollama to free RAM💼 XIV. Business Integration GuideThis repository proves enterprise-level cybersecurity runs on a mobile device.Use CasesField security audits — no laptop requiredRapid deployment in resource-constrained environmentsMobile SOC operations with voice AI command interfaceAI-assisted threat analysis via Jarvis plus Gemini plus ClaudeVoice-commanded network scanning via Jarvis plus NmapTraining environments on any Android deviceDisaster recovery — rebuild entire lab from one GitHub cloneWhat this architecture provesZero Trust security enforced from a mobile deviceVoice AI command interface with confirmation gatesFull packet capture and analysis via Wireshark and tsharkVulnerability scanning via Nmap and MetasploitAI-assisted operations via Jarvis, Gemini, Claude, OllamaCloud synchronization with immutable audit trail on GitHubReproducible — any team member clones and deploys in 30 minutesBusiness Integration TroubleshootingProblem: Team member cannot cloneFix: Verify repo is Public on GitHubProblem: Wake word conflicts with teamFix: Each operator runs set_wakeword.sh independentlyProblem: Vault data needs sharingFix: Copy specific files from Vault manually. Never git add Vault.Problem: Jarvis API costsFix: Gemini free tier handles most operations. Monitor at aistudio.google.comIntegration contact: github.com/CK-BachooOperator: Bachoo, C. K. | Navy Veteran | Dual Google/CompTIA A+ | Innovation Fellow | New York IF-CS-26🏅 XV. Professional VerificationFieldDetailsOperatorC.K. BachooStatusNavy VeteranCredentialsDual Google/CompTIA A+CohortNew York IF-CS-26Current RoleInnovation FellowOperational TierPurple Team Lab EnvironmentsComplianceNIST CSF / GRC / IT Audit ReadyInstitutionThe Knowledge House — New YorkEducationPer Scholas — CompTIA A+ Program — Feb 2025 to May 2025CertificationCompTIA A+ ce — Issued May 2025 — Expires May 2028CertificationGoogle IT Support Professional Certificate — CourseraCertificationGoogle CompTIA Dual Credential — Coursera — Apr 2025CertificationGoogle AI Essentials Specialization — Google — Feb 2026CertificationJunior Cybersecurity Analyst Career Path — Cisco Networking Academy — Mar 2025CertificationNetwork Defense — Cisco Networking Academy — Jan 2025CertificationEndpoint Security — Cisco Networking Academy — Jan 2025CertificationIntroduction to Cybersecurity — Cisco — Dec 2024CertificationOperating Systems Basics — Cisco — Dec 2024CertificationComputer Hardware Basics — Cisco — Dec 2024CertificationGovernance Risk and Compliance GRC and Data Privacy — Udemy — Apr 2025CertificationIdentify and Prevent Phishing Attacks — Udemy — Apr 2025CertificationMicro-Certification Welcome to ServiceNow — ServiceNow — Apr 2025Team AlignmentRed Team Offense — Blue Team Defense — Purple Team Collaboration — Gold Team GRCAI IntegrationAI-Orchestrated Security Operations — Gemini — Claude — Ollama — Jarvis Voice AI InterfacePlatformSamsung Galaxy Note 20 Ultra — Exynos 990 — 12GB RAM — 256GB + 512GB MicroSDGitHubgithub.com/CK-BachooLinkedInlinkedin.com/in/ckbachooStatusMission Ready — March 2026"The mission does not wait for better equipment." — C.K. Bachoo, 2026 ⚓🫡XVI. Voice-Sec Terminal & Automation Suite 🤖ComponentScriptStatusPII Sanitizerscripts/privacy_guard.pyDEPLOYEDPort Sentry / Trap-Door Triggerscripts/port_harden.pyDEPLOYEDTrap-Door Air-Gapscripts/air_gap_isolate.pyDEPLOYEDOSINT Recon Agentscripts/osint_agent.pyDEPLOYEDTTP Log Analyzerscripts/threat_hunt_logs.pyDEPLOYEDNIST Audit Enginebunker_audit.shDEPLOYEDDreadnought Secure Consolescripts/dreadnought_console.shDEPLOYEDA. Automation Suite ArchitectureThe Bunker's Python automation suite operates on a single architectural constraint: zero third-party dependencies. Every script runs on Python's standard library only, eliminating pip install failures, RAM spikes, and Android Signal 9 (OOM) kills on the Exynos 990.privacy_guard.py: Scrubs Student IDs, emails, API keys, PAT tokens, and public IP addresses from outgoing log files before every GitHub push. Safe private ranges (127.x, 10.x, 192.168.x) are whitelisted and pass through untouched. Operates on a named input file — never recursively rewrites the repo.port_harden.py: Continuous port sentry polling every 15 seconds. Monitors Port 8022 (SSH) and Port 8080 (AI Server) for unauthorized IP bindings using ss with netstat fallback. Any binding outside 127.0.0.1 / ::1 / 0.0.0.0 immediately triggers air_gap_isolate.py.air_gap_isolate.py: Trap-Door execution layer. Drops wlan0 and all rmnet_data* interfaces via ip link set down, then zeroes out ~/.bash_history and ~/.git-credentials. Includes --dry-run flag for safe testing without live network disruption. Non-root limitation documented honestly: interface drop is logged and operator is instructed to toggle Airplane Mode if root is unavailable.osint_agent.py: Passive recon only. Performs DNS resolution, multi-record dig enumeration (A/AAAA/MX/TXT/NS/CNAME), WHOIS lookup, and TCP connect port probe on 10 common ports — no nmap required, no root required. Saves timestamped report to Vault/Logs/ automatically.threat_hunt_logs.py: Read-only TTP log analyzer. Scans access logs against 18 IoC patterns across six categories: ShinyHunters/Canvas-specific, SQL injection (4 variants including time-based blind), directory traversal, sensitive file probes, command injection/RCE, and scanner fingerprints. Outputs severity-sorted (CRITICAL/HIGH/MEDIUM) color-coded terminal report and saves clean copy to Vault/Logs/.bunker_audit.sh: NIST CSF 2.0 compliance check engine. Verifies root status, ADB daemon state, VPN tunnel interface, Vault/.gitignore protection, active listening ports, and full automation script arsenal presence. Saves timestamped audit report to Vault/Logs/.dreadnought_console.sh: Hardened operator launch console for sanitized Purple Team operations. Loads isolated environment variables, verifies Vault protections, strips exposed secrets from shell history, and launches defensive tooling through a controlled execution layer. Prevents accidental disclosure of API keys, PAT tokens, usernames, internal paths, and student identifiers during screen sharing, logging, or GitHub synchronization. Includes safe-mode startup to prevent high-RAM process collisions on constrained Android hardware.B. Deployment CommandsBash# Make scripts executable
chmod 700 scripts/*.py && chmod +x bunker_audit.sh scripts/dreadnought_console.sh

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

# Launch hardened operator console
bash scripts/dreadnought_console.sh

# Launch in safe mode (reduced RAM footprint)
bash scripts/dreadnought_console.sh --safe

# Verify environment sanitization
env | grep -Ei 'key|token|secret|pat'
C. Script Interaction Mapport_harden.py       ──(breach detected)──▶  air_gap_isolate.py
threat_hunt_logs.py  ──(CRITICAL hit)────▶  [operator alert]
privacy_guard.py     ──(pre-push sweep)──▶  git push origin master
bunker_audit.sh      ──(compliance check)─▶  Vault/Logs/audit_*.txt
Analyst: C.K. Bachoo | Verified: XO | Date: MAY 2026 ⚓🫡XVII. Threat Intelligence Log: Aeternum C2 (Blockchain C2) 🔗Threat ActorVectorTargetInfrastructureStatusLenAIC++ Loader (x32/x64)Enterprise SystemsPolygon Mainnet (Smart Contracts)ACTIVE (MAR 2026)A. Technical Breakdown: "Living off the Chain"Aeternum C2 represents a shift from centralized servers to immutable, decentralized infrastructure.C2 Mechanism: Commands are stored as encrypted state variables within Solidity smart contracts. The attacker updates the contract to change the "active" payload (Clipper, Stealer, or RAT).Communication: Infected endpoints utilize JSON-RPC calls (eth_call) to public nodes (e.g., polygon-rpc.com) to retrieve instructions.Resilience: Since the "server" is the Polygon blockchain, there is no domain to seize or server to take down.B. Bunker Countermeasures: Note 20 Ultra / Termux DefenseRPC Traffic Interception (tshark):Bashtshark -i any -Y 'http.request.method == "POST"' -T fields -e http.file_data | grep -E "eth_call|eth_getStorageAt"
Infrastructure Decoupling (DNS Sinkhole):127.0.0.1 polygon-rpc.com
127.0.0.1 bor-mainnet.polygon.technology
Behavioral Audit: The workbench uses a background cron job to alert if outbound traffic to known Polygon/Ethereum RPC ports (8545, 443) exceeds a 60-second polling threshold, identifying the C2 "heartbeat."Analyst: C.K. Bachoo | Verified: XO | Date: 21 MAR 2026XVIII. Forensic Mission Report: Neutralizing DNS Sabotage via OOB ⚓🛡️Timestamp: March 2026Threat Vector: DNS Poisoning / Localized Network Sabotage ("Operation Blackout")Origin: Compromised Local "Wire" (WLAN/Ethernet) at The Knowledge HouseA. Incident Analysis (The Attack)The Vector: Sabotage of local name resolution intended to redirect or isolate cohort traffic.Observed Effect: Primary "Wire" nodes failed to resolve external domains; manual pathing to /etc/resolv.conf was blocked by OS-level restrictions.Cybersecurity Domain: Network Security / Incident Response (Remediation).B. Bunker Countermeasures: Note 20 Ultra SOCAction: Leveraged the Workbench's independent Spectrum LTE stack (rmnet_data2) for Out-of-Band (OOB) recovery.Method: Redirected terminal pathing to $PREFIX/etc/resolv.conf to bypass Android kernel-level permission denied errors.Result: Successful triage of Google Public DNS (8.8.8.8 / 8.8.4.4).Resilience: The Workbench remained immune to the "Wire" sabotage because it maintains an independent physical and logical gateway.C. Forensic Conclusion & GRC VerificationThe Android Mobile Cybersecurity Workbench proved 100% resilient. While the localized network was compromised, the Workbench utilized its native OOB capabilities to maintain technical integrity and connectivity.Termux Infrastructure CheckBash~ $ ls -la
drwx------ Android-mobile-cybersecurity-workbench
drwx------ CK-Bachoo
drwx------ Foundations_Lab_Final
drwx------ IF-Cyber-Portfolio
NIST CSF Mobile Audit ExecutionBash~/Android-mobile-cybersecurity-workbench $ ./bunker_audit.sh
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
Analyst: C.K. Bachoo | Verified: XO | Date: 23 MAR 2026 ⚓🫡XIX. Threat Intelligence Log: ShinyHunters Canvas Breach & Trap-Door Defense 🚨Threat ActorVectorTargetDeadline / StatusShinyHuntersFree-For-Teacher Exploit / Credential HarvestingCanvas LMS (Student PII)May 6 - May 12, 2026 (ACTIVE EXTORTION)A. Incident Analysis: The Canvas BreachThe Threat: ShinyHunters compromised the Canvas learning management system, exfiltrating 3.65 TB of data (275M records) including Student IDs, assignments, and private messages. The extortion window closes on May 12.The Hypothesis: Exfiltrated PII is being leveraged for high-fidelity social engineering, phishing, and credential stuffing attacks against the fellowship cohort.B. Bunker Countermeasures & ProtectionOperating from the Note 20 Ultra "Bunker," I remained completely protected from the SaaS-layer compromise through strict environmental decoupling:Local Sovereignty: Instead of relying on the compromised Canvas portal, all lab requirements and documentation were served via local Git clones and offline Markdown files.Jump-Host Isolation: Any necessary downloads originating from Canvas were routed through Google Cloud Shell — an ephemeral, sandboxed environment — preventing any direct connection to my physical hardware.PrivacyGuard Agent: Used local Gemma 2B via privacy_guard.py to automatically scrub outgoing logs of Student IDs and names before pushing to GitHub, neutralizing the value of any intercepted PII.C. The "Trap-Door Air-Gap" (Active Defense)If an attacker managed to breach the local Termux environment, the Bunker employs a defense mechanism to limit post-compromise persistence:The Logic: If the automated port sentry (port_harden.py) detects an unauthorized IP binding to Port 8022 (SSH) or Port 8080 (AI Server), it instantly triggers the air_gap_isolate.py protocol.The Execution: Network interfaces are immediately disabled and volatile credentials are cleared to limit post-compromise persistence. The device drops all network interfaces, severing the connection to the outside world.The Result: The attacker session is terminated. Simultaneously, the system flushes volatile memory, wiping ~/.bash_history and ~/.git-credentials. The operator is no longer reachable, leaving an empty, isolated shell.Analyst: C.K. Bachoo | Verified: XO | Date: MAY 2026
