# 🛡️ ARM64 Mobile-to-Cloud Security Workbench (The Bunker)

**Operator:** C.K. Bachoo | Navy Veteran | Armed Forces Service Medal
**Credentials:** CompTIA A+ | Google IT Support Professional
**Fellowship:** TKH Cybersecurity Innovation Fellow | NY-IF-CS-26 | March 2026
**Platform:** Samsung Galaxy Note 20 Ultra | Termux | Mobile-Only Architecture
**Mission:** Scale enterprise-level cybersecurity workflows on constrained mobile hardware. No laptop required.

> "The mission does not wait for better equipment." — C.K. Bachoo ⚓

---

## 📋 Table of Contents
1. [Hardware Matrix](#i-hardware-matrix)
2. [Pre-Flight Checklist](#ii-pre-flight-checklist)
3. [Base Initialization](#iii-base-initialization)
4. [OPSEC Data Isolation](#iv-opsec-data-isolation)
5. [SSH Keys for GitHub](#v-ssh-keys-for-github)
6. [X11 Graphical Interface](#vi-x11-graphical-interface)
7. [Kali Linux Virtualization](#vii-kali-linux-virtualization)
8. [AI Stack Deployment](#viii-ai-stack-deployment)
9. [GitHub PAT Cloud Sync](#ix-github-pat-cloud-sync)
10. [Operational Commands](#x-operational-commands)
11. [Wake and Close Commands](#xi-wake-and-close-commands)
12. [Thermal Safety Protocol](#xii-thermal-safety-protocol)
13. [Full Troubleshooting Guide](#xiii-full-troubleshooting-guide)
14. [Business Integration Guide](#xiv-business-integration-guide)
15. [Professional Verification](#xv-professional-verification)

---

## ⚙️ I. Hardware Matrix

| Device | RAM | Status |
|---|---|---|
| Samsung Galaxy Note 20 Ultra 5G | 12GB | Primary — Fully Verified |
| Samsung S21 Ultra | 12GB | Verified |
| Samsung S22/S23/S24/S25/S26 Ultra | 12GB | Verified |
| Samsung Z-Fold 3/4/5/6/Trifold | 12GB | Verified |
| Google Pixel 6/7/8/9 Pro/Fold | 8-12GB | Verified |
| iPhone (iOS) | Any | Codespaces + iSH/UTM Pivot |

**Minimum Requirements:**
- Android 10 or higher
- 8GB RAM minimum (12GB recommended)
- 5G or Fiber Wi-Fi for GitHub sync and cloud AI
- 256GB internal storage or 1TB MicroSD for Vault and PCAPs
- S-Pen recommended for Wireshark packet precision on Note devices

---

## ✅ II. Pre-Flight Checklist

Before starting run through this list:

- [ ] Termux installed from F-Droid (not Play Store)
- [ ] Termux-API installed from F-Droid
- [ ] Termux-X11 companion app installed
- [ ] Battery above 50 percent
- [ ] Connected to Wi-Fi
- [ ] Storage permission granted to Termux
- [ ] Battery optimization DISABLED for Termux in Android Settings
- [ ] GitHub account created at github.com
- [ ] At least 4GB free storage

**How to disable battery optimization:**
1. Android Settings → Apps → Termux
2. Battery → Unrestricted
3. Do the same for Termux-API and Termux-X11

---

## 🚀 III. Base Initialization

Open Termux. Run each command one at a time. Wait for each to finish before running the next.

**Step 1 — Grant storage access:**
```bash
termux-setup-storage
```
A popup will appear. Tap Allow.

**Step 2 — Update package lists:**
```bash
pkg update -y
```

**Step 3 — Upgrade existing packages:**
```bash
pkg upgrade -y
```

**Step 4 — Install all required tools:**
```bash
pkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y
```

**Step 5 — Install Python security packages:**
```bash
pip install requests scapy paramiko
```

**Step 6 — Verify everything installed correctly:**
```bash
python --version
git --version
nmap --version
ssh -V
```
All four should return version numbers. If any fail see Troubleshooting Section XIII.

**Step 7 — Clone this repository:**
```bash
cd ~
git clone --depth 1 https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git
cd Android-mobile-cybersecurity-workbench
```
Replace YOUR-GITHUB-USERNAME with your actual GitHub username.

---

## 🛡️ IV. OPSEC Data Isolation

All sensitive scan results, packet captures, and logs stay in the Vault folder. Vault is never committed to GitHub.

**Create Vault structure:**
```bash
mkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence
```

**Add Vault to gitignore:**
```bash
echo "Vault/" >> .gitignore
echo "*.pcap" >> .gitignore
echo "*.cap" >> .gitignore
echo ".secrets/" >> .gitignore
git config --local core.excludesfile .gitignore
```

**Verify Vault is protected:**
```bash
cat .gitignore
git status
```
Vault folder should NOT appear in git status output.

---

## 🔑 V. SSH Keys for GitHub

SSH keys give you passwordless GitHub access that never expires.

**Step 1 — Generate your key:**
```bash
ssh-keygen -t ed25519 -C "YOUR-GITHUB-USERNAME"
```
Replace YOUR-GITHUB-USERNAME with your GitHub username.
Press ENTER three times to accept all defaults.

**Step 2 — Display your public key:**
```bash
cat ~/.ssh/id_ed25519.pub
```
This prints YOUR unique public key to the screen.
It will look similar to this format — yours will be different:
```
ssh-ed25519 AAAA[LONG-UNIQUE-STRING-UNIQUE-TO-YOU] YOUR-GITHUB-USERNAME
```

**Step 3 — Copy YOUR output from the terminal.**
Never share this key publicly. Never paste it into any document.

**Step 4 — Add to GitHub:**
1. Open github.com in browser
2. Profile photo → Settings
3. SSH and GPG keys → New SSH key
4. Title: Note20Ultra-Termux
5. Paste YOUR key
6. Tap Add SSH key

**Step 5 — Verify connection:**
```bash
ssh -T git@github.com
```
Should return: `Hi YOUR-GITHUB-USERNAME! You've successfully authenticated.`

**Troubleshooting SSH:**
- If `Permission denied`: Make sure you copied the `.pub` file not the private key
- If `Connection refused`: Run `eval $(ssh-agent -s)` then `ssh-add ~/.ssh/id_ed25519`
- If `ssh not found`: Run `pkg install openssh` first

---

## 🖥️ VI. X11 Graphical Interface

X11 gives you a full Linux desktop GUI on your phone screen. Required for Wireshark visual interface.

**Step 1 — Install X11 and desktop environment:**
```bash
pkg install xfce4 xfce4-goodies -y
```
This takes several minutes. Let it run.

**Step 2 — Install X11 utilities:**
```bash
pkg install x11-repo -y
pkg install xorg-xrandr -y
```

### HOW TO WAKE X11 (Launch the GUI)

Run these commands in this exact order every time you want to start the GUI:

**Command 1 — Start the X11 server:**
```bash
termux-x11 :1 &
```

**Command 2 — Start the desktop:**
```bash
DISPLAY=:1 xfce4-session &
```

**Command 3 — Switch to the Termux-X11 app on your phone.**
You will see the full XFCE desktop.

**Command 4 — To launch Wireshark inside the GUI:**
```bash
DISPLAY=:1 wireshark &
```

**Command 5 — To launch any other GUI app:**
```bash
DISPLAY=:1 [appname] &
```

### HOW TO CLOSE X11 (Shut down the GUI)

**Option 1 — Clean shutdown from inside the GUI:**
Tap the XFCE menu → Log Out → Log Out

**Option 2 — Force close from Termux:**
```bash
pkill xfce4-session
pkill termux-x11
```

**Option 3 — Nuclear option if frozen:**
```bash
pkill -9 -u $(whoami)
```
WARNING: This kills ALL processes including Termux itself. Reopen Termux after.

### X11 Wake Lock (CRITICAL for stability)

Without this Android will kill X11 in the background:

1. Swipe down notification bar
2. Find Termux notification
3. Tap **Acquire Wakelock**
4. You will see a new notification: "Termux is running"

Do this EVERY TIME you start X11 or it will freeze within minutes.

**X11 Troubleshooting:**
- If screen is black: Close Termux-X11 app completely. Reopen it. Run `termux-x11 :1 &` again
- If GUI freezes: Acquire wakelock first then restart with `pkill xfce4-session && DISPLAY=:1 xfce4-session &`
- If `command not found xfce4-session`: Run `pkg install xfce4 -y` again
- If Termux-X11 app crashes: Reinstall from F-Droid
- If display variable error: Run `export DISPLAY=:1` before your command

---

## 🧪 VII. Kali Linux Virtualization

Kali runs as a full Linux environment inside Termux using proot. No root required.

**Step 1 — Install Kali:**
```bash
proot-distro install kali
```
This downloads about 500MB. Takes several minutes on Wi-Fi.

**Step 2 — Enter Kali:**
```bash
proot-distro login kali
```
Your prompt changes to `root@localhost`. You are now inside Kali.

**Step 3 — Update Kali:**
```bash
apt update -y
apt upgrade -y
```

**Step 4 — Install security tools:**
```bash
apt install nmap wireshark-cli tshark metasploit-framework sqlmap nikto -y
```

**Step 5 — Verify tools:**
```bash
nmap --version
tshark --version
sqlmap --version
```

**Step 6 — How to exit Kali back to Termux:**
```bash
exit
```
Your prompt returns to the Termux prompt.

**How to re-enter Kali any time:**
```bash
proot-distro login kali
```

**How to run a single Kali command without entering Kali:**
```bash
proot-distro login kali -- nmap -sn 192.168.1.0/24
```

**Kali Troubleshooting:**
- If install hangs at 0 percent: CTRL+C then run `proot-distro remove kali` then reinstall
- If `apt not found`: Make sure you ran `proot-distro login kali` first
- If storage error during install: Run `termux-setup-storage` in regular Termux first
- If Kali environment corrupted: `proot-distro remove kali` then `proot-distro install kali`
- If tools not found after install: Run `apt update && apt install [tool] -y` again inside Kali

---

## 🤖 VIII. AI Stack Deployment

### Local AI — Ollama (Runs on your phone. No internet required.)

**Step 1 — Install Ollama:**
```bash
pkg install ollama -y
```

**Step 2 — Start Ollama server:**
```bash
ollama serve &
```
The `&` runs it in the background. You will see a process ID number.

**Step 3 — Download a model:**
```bash
ollama pull llama3
```
Downloads about 4GB. Run on Wi-Fi.

**Step 4 — Talk to the AI:**
```bash
ollama run llama3
```
Type your question. Press ENTER. Type `/bye` to exit.

**How to stop Ollama:**
```bash
pkill ollama
```

**Ollama Troubleshooting:**
- If server hangs: `pkill ollama` then `ollama serve &` again
- If model download fails: Check Wi-Fi connection then retry `ollama pull llama3`
- If out of memory error: Use a smaller model: `ollama pull phi3`

### Cloud AI — Gemini and Claude

**Step 1 — Open your bashrc:**
```bash
nano ~/.bashrc
```

**Step 2 — Add YOUR API keys at the bottom:**
```bash
export GEMINI_API_KEY="PASTE-YOUR-GEMINI-API-KEY-HERE"
export CLAUDE_API_KEY="PASTE-YOUR-CLAUDE-API-KEY-HERE"
```
Get your Gemini key at: aistudio.google.com
Get your Claude key at: console.anthropic.com
Never share these keys publicly.

**Step 3 — Save and close:**
Press CTRL+X then Y then ENTER

**Step 4 — Load the keys into current session:**
```bash
source ~/.bashrc
```

**Step 5 — Verify keys loaded:**
```bash
echo $GEMINI_API_KEY
echo $CLAUDE_API_KEY
```
Should print your key values.

**IMPORTANT:** Run `source ~/.bashrc` at the start of every new Termux session or the keys will not be available.

---

## 🔐 IX. GitHub PAT Cloud Sync

PAT (Personal Access Token) lets Termux push directly to GitHub without a browser.

**Step 1 — Generate PAT on GitHub:**
1. github.com → Profile photo → Settings
2. Scroll to bottom → Developer settings
3. Personal access tokens → Tokens classic
4. Generate new token classic
5. Note: Termux-Workbench-Push
6. Expiration: 90 days
7. Check the box next to `repo`
8. Tap Generate token
9. COPY IT IMMEDIATELY — you cannot see it again
10. It starts with `github_pat_` — keep it private like a password

**Step 2 — Store PAT securely on your device:**
```bash
mkdir -p ~/.secrets
chmod 700 ~/.secrets
echo "PASTE-YOUR-PAT-HERE" > ~/.secrets/github_pat.txt
chmod 600 ~/.secrets/github_pat.txt
```
Replace PASTE-YOUR-PAT-HERE with your actual token.
The `.secrets` folder is protected by `.gitignore` and never pushed to GitHub.

**Step 3 — Load PAT into session:**
```bash
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
```

**Step 4 — Set remote URL:**
```bash
git remote set-url origin https://YOUR-GITHUB-USERNAME:${GITHUB_PAT}@github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git
```
Replace YOUR-GITHUB-USERNAME with your actual GitHub username.
The `${GITHUB_PAT}` variable loads your token automatically. Never paste the actual token into this command.

**Step 5 — Push your work:**
```bash
git add .
git commit -m "Sync Audit — YOUR-GITHUB-USERNAME"
git push origin master
```

**Step 6 — Verify push worked:**
```bash
git status
```
Should show: `nothing to commit, working tree clean`

**PAT Troubleshooting:**
- If authentication failed: Regenerate PAT on GitHub and run Step 2-4 again
- If push rejected: Run `git pull origin master` first then push
- If fatal not a git repository: `cd ~/Android-mobile-cybersecurity-workbench` first
- If remote already exists: `git remote remove origin` then run Step 4 again
- PAT expired: Generate new 90 day token and repeat Steps 2-4

---

## 🛰️ X. Operational Commands

**Network Discovery:**
```bash
nmap -sn 192.168.1.0/24
```

**Full Port Scan with OS Detection:**
```bash
nmap -A 192.168.1.1
```

**Save Scan to Vault:**
```bash
nmap -oN Vault/Scans/audit_$(date +%Y%m%d).txt 192.168.1.1
```

**Packet Capture to Vault:**
```bash
tshark -i 1 -w Vault/PCAPs/capture_$(date +%Y%m%d).pcap
```

**Read a Capture File:**
```bash
tshark -r Vault/PCAPs/capture_$(date +%Y%m%d).pcap
```

**Run Python Audit Script:**
```bash
python auto_audit.py
```

**Quick Sync Everything to GitHub:**
```bash
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
git add .
git commit -m "Audit sync $(date +%Y-%m-%d) — YOUR-GITHUB-USERNAME"
git push origin master
```

---

## ⚡ XI. Wake and Close Commands

### WAKE COMMANDS — Start everything from scratch

**Wake Termux environment:**
```bash
source ~/.bashrc
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
cd ~/Android-mobile-cybersecurity-workbench
```

**Wake X11 GUI:**
```bash
termux-x11 :1 &
DISPLAY=:1 xfce4-session &
```
Then open Termux-X11 app. Then acquire wakelock from notification bar.

**Wake Kali:**
```bash
proot-distro login kali
```

**Wake Ollama AI:**
```bash
ollama serve &
```

**Wake Wireshark in GUI:**
```bash
DISPLAY=:1 wireshark &
```

**Wake full environment in one command:**
```bash
source ~/.bashrc && export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt) && cd ~/Android-mobile-cybersecurity-workbench && echo "Bunker Online"
```

### CLOSE COMMANDS — Shut everything down cleanly

**Close Kali (from inside Kali):**
```bash
exit
```

**Close X11 desktop cleanly:**
```bash
pkill xfce4-session
pkill termux-x11
```

**Close Ollama:**
```bash
pkill ollama
```

**Close specific app in X11:**
```bash
pkill wireshark
pkill firefox
```

**Close everything — nuclear option:**
```bash
pkill -9 -u $(whoami)
```
WARNING: This kills ALL processes. Reopen Termux after.

**Safe full shutdown sequence:**
```bash
# 1. Exit Kali if open
exit
# 2. Stop Ollama
pkill ollama
# 3. Stop X11
pkill xfce4-session && pkill termux-x11
# 4. Final sync to GitHub
git add . && git commit -m "End of session — YOUR-GITHUB-USERNAME" && git push origin master
```

---

## 🌡️ XII. Thermal Safety Protocol

The Note 20 Ultra runs hot under heavy loads. Monitor and protect it.

**Check current temperature:**
```bash
cat /sys/class/thermal/thermal_zone0/temp
```
Divide by 1000 for Celsius. Example: `45000` = 45C.

**Safe range:** Below 40C
**Caution range:** 40C to 45C — reduce workload
**Danger range:** Above 45C — execute kill switch immediately

**Thermal kill switch:**
```bash
pkill -9 -u $(whoami)
```

**Thermal monitoring loop (auto-warns every 30 seconds):**
```bash
while true; do
  TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
  echo "Temp: $((TEMP/1000))C"
  sleep 30
done
```
Press CTRL+C to stop monitoring.

**Thermal best practices:**
- Never run Kali plus X11 plus Ollama simultaneously while charging
- Use a fan or keep phone on a cool surface during long scans
- Disable 5G and use Wi-Fi during heavy processing to reduce heat
- If phone feels hot to touch — run kill switch immediately

---

## 🔧 XIII. Full Troubleshooting Guide

### Termux Issues

| Problem | Fix |
|---|---|
| pkg update fails | Run `termux-change-repo` and select a different mirror |
| Package not found | Run `pkg update` first then retry install |
| Storage permission denied | Run `termux-setup-storage` and tap Allow |
| Termux killed by Android | Disable battery optimization for Termux in Settings |
| Command not found after install | Close and reopen Termux. Run `source ~/.bashrc` |

### Git Issues

| Problem | Fix |
|---|---|
| Fatal not a git repository | `cd ~/Android-mobile-cybersecurity-workbench` |
| Authentication failed | Regenerate PAT and run `git remote set-url` again |
| Push rejected | Run `git pull origin master` first then push |
| Merge conflict | Run `git status` to see conflicted files. Edit them. Then `git add .` and commit |
| Accidental commit of secrets | Immediately revoke PAT on GitHub. Generate new one. |

### X11 Issues

| Problem | Fix |
|---|---|
| Black screen | Close Termux-X11 app. Reopen. Run `termux-x11 :1 &` again |
| GUI freezes immediately | Acquire wakelock from notification bar first |
| Process killed | Battery optimization must be disabled for Termux |
| Display error | Run `export DISPLAY=:1` before any GUI command |
| Cannot find xfce4 | `pkg install xfce4 -y` |

### Kali Issues

| Problem | Fix |
|---|---|
| Install hangs | CTRL+C then `proot-distro remove kali` then reinstall |
| apt command not found | You are not inside Kali. Run `proot-distro login kali` |
| Tool not found | `apt update && apt install [toolname] -y` inside Kali |
| Kali environment broken | `proot-distro remove kali` then `proot-distro install kali` |

### Network Issues

| Problem | Fix |
|---|---|
| Nmap permission denied | Some scan types require root. Use `-sn` for ping scan without root |
| No hosts found | Verify you are on the same network. Check your subnet |
| tshark no interfaces | Run `termux-setup-storage` and grant permissions |

---

## 💼 XIV. Business Integration Guide

This repository demonstrates that enterprise-level cybersecurity workflows can run on a $400 mobile device. For businesses and organizations looking to integrate this architecture:

**Use Cases:**
- Field security audits with no laptop required
- Rapid deployment in resource-constrained environments
- Mobile SOC (Security Operations Center) operations
- Training environments that run on any Android device
- Disaster recovery — rebuild entire lab from one GitHub clone

**What this architecture proves:**
- Zero Trust security enforced from a mobile device
- Full packet capture and network analysis via tshark
- Vulnerability scanning via Nmap and Metasploit
- AI-assisted security operations via Ollama local LLM
- Cloud synchronization with immutable audit trail on GitHub
- Reproducible environment — any team member can clone and deploy in under 30 minutes

**Integration contact:**
github.com/CK-Bachoo

---

## 🎖️ XV. Professional Verification

| Field | Details |
|---|---|
| Operator | C.K. Bachoo |
| Service | United States Navy Veteran |
| Award | Armed Forces Service Medal |
| Target Role | Junior Cybersecurity Analyst — SOC / NOC / GRC |
| Fellowship | TKH Cybersecurity Innovation Fellow — NY-IF-CS-26 — Jan 2026 to Aug 2026 |
| Institution | The Knowledge House — New York |
| Education | Per Scholas — CompTIA A+ Program — Feb 2025 to May 2025 |
| Certification | CompTIA A+ ce — Issued May 2025 — Expires May 2028 |
| Certification | Google IT Support Professional Certificate — Coursera |
| Certification | Google CompTIA Dual Credential — Coursera — Apr 2025 |
| Certification | Google AI Essentials Specialization — Google — Feb 2026 |
| Certification | Junior Cybersecurity Analyst Career Path — Cisco Networking Academy — Mar 2025 |
| Certification | Network Defense — Cisco Networking Academy — Jan 2025 |
| Certification | Endpoint Security — Cisco Networking Academy — Jan 2025 |
| Certification | Introduction to Cybersecurity — Cisco — Dec 2024 |
| Certification | Operating Systems Basics — Cisco — Dec 2024 |
| Certification | Computer Hardware Basics — Cisco — Dec 2024 |
| Certification | Governance Risk and Compliance GRC and Data Privacy — Udemy — Apr 2025 |
| Certification | Identify and Prevent Phishing Attacks — Udemy — Apr 2025 |
| Certification | Micro-Certification Welcome to ServiceNow — ServiceNow — Apr 2025 |
| Team Alignment | Red Team Offense — Blue Team Defense — Purple Team Collaboration — Gold Team GRC |
| AI Integration | AI-Orchestrated Security Operations — Gemini — Claude — Ollama Local LLM — Voice-Sec-Terminal Architect |
| Platform | Samsung Galaxy Note 20 Ultra — Termux — Mobile Only |
| GitHub | github.com/CK-Bachoo |
| LinkedIn | linkedin.com/in/ckbachoo |
| Status | Mission Ready — March 2026 |

---

**"The mission does not wait for better equipment."**
— C.K. Bachoo, 2026 ⚓🫡