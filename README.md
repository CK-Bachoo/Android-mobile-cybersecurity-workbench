# 🛡️ ARM64 Mobile-to-Cloud Security Workbench (The Bunker)

**Operator:** C.K. Bachoo | Navy Veteran | Armed Forces Service Medal
**Credentials:** CompTIA A+ | Google IT Support Professional
**Fellowship:** TKH Innovation Fellow | NY-IF-CS-26 | March 2026
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

**Hardware Troubleshooting:**

| Problem | Fix |
|---|---|
| Phone overheats during setup | Stop all processes. Cool device. Restart one tool at a time. |
| Not enough storage | Move Vault to MicroSD. `ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/Vault` |
| Android version too old | Codespaces browser fallback works on any Android version |
| MicroSD not detected | Settings → Device Care → Storage → check SD card mount status |

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
- [ ] MicroSD card inserted and mounted (recommended)
- [ ] Gemini API key saved at ~/.secrets/gemini_api_key.txt

**How to disable battery optimization:**
1. Android Settings → Apps → Termux
2. Battery → Unrestricted
3. Do the same for Termux-API and Termux-X11

**Pre-Flight Troubleshooting:**

| Problem | Fix |
|---|---|
| Termux from Play Store installed | Uninstall it. Install from F-Droid only. Play Store version is outdated. |
| Battery optimization keeps re-enabling | Samsung One UI resets this. Check after every phone restart. |
| No F-Droid on phone | Go to f-droid.org in browser. Download and install APK directly. |
| MicroSD not showing in Termux | Run `termux-setup-storage` and tap Allow |

---

## 🚀 III. Base Initialization

Open Termux. Run each command one at a time. Wait for each to finish.

**Step 1 — Grant storage access:**
```bash
termux-setup-storage
```
A popup will appear. Tap Allow.

**Step 2 — Update and upgrade:**
```bash
pkg update -y && pkg upgrade -y
```

**Step 3 — Install all required tools:**
```bash
pkg install git python nmap openssh proot-distro termux-api termux-x11-repo x11-repo -y
```

**Step 4 — Install Python security packages:**
```bash
pip install requests scapy paramiko
```

**Step 5 — Verify everything installed correctly:**
```bash
python --version && git --version && nmap --version && ssh -V
```
All four should return version numbers.

**Step 6 — Clone this repository:**
```bash
cd ~ && git clone --depth 1 https://github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git && cd Android-mobile-cybersecurity-workbench
```
Replace YOUR-GITHUB-USERNAME with your actual GitHub username.

**Step 7 — Set your wake word:**
```bash
bash scripts/set_wakeword.sh
```
Choose any word. That word launches X11 and Jarvis together.

**Base Initialization Troubleshooting:**

| Problem | Fix |
|---|---|
| pkg update fails | Run `termux-change-repo` and select a different mirror |
| Package not found | Run `pkg update` first then retry install |
| Storage permission denied | Run `termux-setup-storage` and tap Allow |
| pip install fails | Run `pip install --upgrade pip` first |
| git clone fails | Check Wi-Fi. Verify GitHub username is correct. |
| Python not found after install | Close and reopen Termux. Run `source ~/.bashrc` |

---

## 🛡️ IV. OPSEC Data Isolation

All sensitive scan results, packet captures, and logs stay in the Vault.
Vault is never committed to GitHub.

**Create Vault structure:**
```bash
mkdir -p Vault/Scans Vault/PCAPs Vault/Logs Vault/Evidence
```

**Add Vault to gitignore:**
```bash
echo "Vault/" >> .gitignore && echo "*.pcap" >> .gitignore && echo "*.cap" >> .gitignore && echo ".secrets/" >> .gitignore && git config --local core.excludesfile .gitignore
```

**Verify Vault is protected:**
```bash
cat .gitignore && git status
```
Vault folder should NOT appear in git status output.

**Move Vault to MicroSD for physical isolation:**
```bash
mkdir -p /sdcard/Vault && ln -s /sdcard/Vault ~/Android-mobile-cybersecurity-workbench/Vault
```

**OPSEC Rules:**
- Never commit real IP addresses to GitHub
- Never commit API keys or PAT tokens
- Never commit pcap files — keep in Vault only
- Always use YOUR-GITHUB-USERNAME placeholder in public docs
- Revoke PAT immediately if accidentally exposed

**OPSEC Troubleshooting:**

| Problem | Fix |
|---|---|
| Vault appearing in git status | Run `git rm -r --cached Vault/` then commit |
| Secrets accidentally committed | Immediately revoke PAT on GitHub. Rotate all keys. |
| gitignore not working | Run `git config --local core.excludesfile .gitignore` |
| Vault files too large for phone | Move Vault to MicroSD using symlink above |
| .secrets folder exposed | Run `chmod 700 ~/.secrets && chmod 600 ~/.secrets/*` |

---

## 🔑 V. SSH Keys for GitHub

SSH keys give you passwordless GitHub access that never expires.

**Step 1 — Generate your key:**
```bash
ssh-keygen -t ed25519 -C "YOUR-GITHUB-USERNAME"
```
Press ENTER three times to accept all defaults.

**Step 2 — Display your public key:**
```bash
cat ~/.ssh/id_ed25519.pub
```
It will look similar to this — yours will be different:
```
ssh-ed25519 AAAA[LONG-UNIQUE-STRING-UNIQUE-TO-YOU] YOUR-GITHUB-USERNAME
```

**Step 3 — Copy YOUR output. Never share it publicly.**

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

**SSH Troubleshooting:**

| Problem | Fix |
|---|---|
| Permission denied | Make sure you copied the `.pub` file not the private key |
| Connection refused | Run `eval $(ssh-agent -s)` then `ssh-add ~/.ssh/id_ed25519` |
| ssh not found | Run `pkg install openssh` first |
| Key not accepted by GitHub | Delete the key on GitHub and re-add it |
| Authentication keeps failing | Generate a new key pair and start fresh |

---

## 🖥️ VI. X11 Graphical Interface

X11 gives you a full Linux desktop GUI on your phone screen.
Required for Wireshark, VS Code visual editing, and multi-window operations.

**Install X11:**
```bash
pkg install xfce4 xfce4-goodies x11-repo xorg-xrandr -y
```

### 🎯 Choose Your Operating Mode

**Mode 1 — Full Automation (Recommended):**
Set your wake word once. Type it. Everything launches.
Jarvis AI online. X11 desktop open. Zero Trust active.
```bash
bash scripts/set_wakeword.sh
```
Then type your wake word every session. Example: `bunker`

**Mode 2 — Manual Control:**
Skip the wake word. Run each tool individually.
Use the manual commands below. No AI. No automation.

**Mode 3 — Terminal Only:**
Skip X11 entirely. Run everything in Termux terminal.
Lightweight. Fast. Best for low battery or quick operations.

### HOW TO WAKE X11

**Automatic — wake word:**
```bash
bunker
```
Replace `bunker` with your personal wake word.

**Manual — step by step:**
```bash
termux-x11 :1 &
DISPLAY=:1 xfce4-session &
```
Then open Termux-X11 app. Acquire wakelock from notification bar.

### HOW TO LAUNCH APPS IN X11

```bash
DISPLAY=:1 wireshark &
DISPLAY=:1 thunar &
DISPLAY=:1 xterm &
DISPLAY=:1 [appname] &
```

### HOW TO CLOSE X11

```bash
pkill xfce4-session && pkill termux-x11
```

Nuclear option if frozen:
```bash
pkill -9 -u $(whoami)
```

### X11 Wake Lock — CRITICAL

1. Swipe down notification bar
2. Find Termux notification
3. Tap Acquire Wakelock

Do this EVERY TIME or X11 freezes within minutes.

**X11 Troubleshooting:**

| Problem | Fix |
|---|---|
| Black screen | Close Termux-X11 app. Reopen. Run `termux-x11 :1 &` again |
| GUI freezes immediately | Acquire wakelock from notification bar first |
| Process killed by Android | Disable battery optimization for Termux in Settings |
| Display variable error | Run `export DISPLAY=:1` before any GUI command |
| xfce4-session not found | Run `pkg install xfce4 -y` again |
| Termux-X11 app crashes | Reinstall from F-Droid |
| Wake word not working | Run `source ~/.bashrc` then try again |
| X11 and Jarvis not starting together | Run `bash scripts/bunker_wake.sh` directly |

---

## 🧪 VII. Kali Linux Virtualization

Kali runs as a full Linux environment inside Termux using proot. No root required.

**Install Kali:**
```bash
proot-distro install kali
```
Downloads about 500MB. Takes several minutes on Wi-Fi.

**Enter Kali:**
```bash
proot-distro login kali
```
Your prompt changes to `root@localhost`.

**Update and install security tools:**
```bash
apt update -y && apt install nmap wireshark-cli tshark metasploit-framework sqlmap nikto -y
```

**Verify tools:**
```bash
nmap --version && tshark --version && msfconsole --version
```

**Exit Kali:**
```bash
exit
```

**Run single command without entering Kali:**
```bash
proot-distro login kali -- nmap -sn 192.168.1.0/24
```

**Kali Troubleshooting:**

| Problem | Fix |
|---|---|
| Install hangs at 0 percent | CTRL+C then `proot-distro remove kali` then reinstall |
| apt not found | You are not inside Kali. Run `proot-distro login kali` |
| Tool not found | `apt update && apt install [toolname] -y` inside Kali |
| Kali environment corrupted | `proot-distro remove kali` then `proot-distro install kali` |
| Cannot push from inside Kali | Exit Kali first. Push from Termux. |
| Metasploit takes too long | Normal. First launch downloads dependencies. Wait 5 minutes. |
| No internet inside Kali | Exit Kali. Check Wi-Fi. Re-enter Kali. |

---

## 🤖 VIII. AI Stack Deployment & Security Tooling

### Resource Management — Note 20 Ultra 12GB RAM

| Tool | RAM Usage | Type | Safe to Run Together? |
|---|---|---|---|
| Jarvis Voice AI | ~50MB | Local Python + Cloud | YES — Primary |
| Gemini API | ~0MB local | Cloud Only | YES — Built into Jarvis |
| Claude AI | ~0MB local | Cloud Only | YES — Built into Jarvis |
| X11 Desktop | ~400MB | Local GUI | YES — With Jarvis |
| VS Code Codespaces | ~200MB browser | Cloud IDE | YES — With Jarvis |
| Wireshark X11 | ~300MB | Local GUI | YES — With X11 active |
| Nmap | ~50MB | Local Scanner | YES — Lightweight |
| Ollama Llama 3 | 4-6GB | Local LLM | NO — Run separately |

**Golden Rule:** Never run Ollama with anything else.
Exynos 990 will overheat and 12GB RAM will max out.

---

### 🎙️ Jarvis Voice AI — Primary Command Interface

Voice-activated AI built natively on the Note 20 Ultra.
Zero Trust gate on all execute commands.
All sessions logged to Vault and 512GB MicroSD and GitHub.

**Hardware this was built for:**
- Device: Samsung Galaxy Note 20 Ultra
- Processor: Exynos 990
- RAM: 12GB
- Storage: 256GB Internal + 512GB MicroSD

**Install Jarvis:**
```bash
pkg install termux-api -y && pip install requests
```

**Wake Jarvis manually:**
```bash
cd ~/Android-mobile-cybersecurity-workbench
python3 scripts/jarvis.py
```

**Wake Jarvis automatically with X11:**
```bash
bunker
```

**Jarvis voice commands:**
- Say anything — Jarvis processes via Gemini and responds
- Say "hardware check" — thermal and storage diagnostics
- Say "scan my network" — suggests nmap command with Zero Trust gate
- Say "start packet capture" — suggests tshark command
- Say "help" — lists all capabilities
- Say "exit" or "shutdown" — clean shutdown with session log

**Stop Jarvis:**
```bash
pkill -f jarvis.py
```

**Jarvis Troubleshooting:**

| Problem | Fix |
|---|---|
| No voice input detected | Check termux-api permissions — Microphone must be allowed |
| TTS not speaking | Run `termux-tts-speak "test"` to verify audio |
| Gemini not responding | Run `echo $GEMINI_API_KEY` — if blank run `source ~/.bashrc` |
| Phone gets hot | Stop Jarvis. Never run with Ollama simultaneously |
| Jarvis loop crashes | Run `source ~/.bashrc` then restart jarvis.py |
| Zero Trust gate not hearing confirm | Speak clearly. Move closer to mic. |
| Wake word not launching Jarvis | Run `source ~/.bashrc` then try wake word again |

---

### 🔑 Bunker Wake System — One Word Launches Everything

**First time setup:**
```bash
bash scripts/set_wakeword.sh
```

**Wake word examples:**

| Wake Word | Operator Style |
|---|---|
| bunker | C.K. Bachoo — Original |
| sentinel | Defensive posture |
| nighthawk | Stealth ops |
| fortress | Maximum defense |
| shadow | Low profile |
| jarvis | Classic AI reference |
| ops | Short and tactical |

**After setup — type your word and hit ENTER:**
```bash
bunker
```

**What happens automatically:**
1. Environment and PAT load
2. X11 server starts
3. XFCE blue desktop launches
4. Termux-X11 app opens
5. Jarvis speaks and goes online

**Change wake word anytime:**
```bash
bash scripts/set_wakeword.sh
```

**Wake Word Troubleshooting:**

| Problem | Fix |
|---|---|
| Wake word not recognized | Run `source ~/.bashrc` then try again |
| Wake word launches but X11 is black | Acquire wakelock from notification bar |
| Jarvis does not speak on wake | Check termux-api mic permissions |
| Want to change wake word | Run `set_wakeword.sh` again |
| Wake word disappeared after restart | Run `source ~/.bashrc` — alias reloads |

---

### 🛰️ Nmap — Network Intelligence

**Install:**
```bash
pkg install nmap -y
```

**Essential commands:**
```bash
nmap -sn 192.168.1.0/24
nmap -sV 192.168.1.1
nmap -A 192.168.1.1
nmap -p 22,80,443,8080 192.168.1.1
nmap -F 192.168.1.1
nmap -oN Vault/Scans/scan_$(date +%Y%m%d_%H%M%S).txt 192.168.1.1
nmap -oA Vault/Scans/scan_$(date +%Y%m%d) 192.168.1.1
```

**Nmap + Wireshark workflow:**
```bash
tshark -i wlan0 -w Vault/PCAPs/nmap_capture.pcap &
nmap -sV 192.168.1.1
pkill tshark
DISPLAY=:1 wireshark Vault/PCAPs/nmap_capture.pcap &
```

**Nmap Troubleshooting:**

| Problem | Fix |
|---|---|
| Permission denied | Use `-sn` ping scan — no root needed |
| No hosts found | Verify same network. Check subnet. |
| Scan too slow | Add `-T4` flag for faster timing |
| nmap not found | `pkg install nmap -y` |
| Results not saving | `mkdir -p Vault/Scans` |
| SYN scan requires root | Enter Kali proot for root-level scans |

---

### 🦈 Wireshark — Packet Analysis

**Install CLI in Kali:**
```bash
proot-distro login kali && apt install wireshark-cli tshark -y
```

**Essential commands:**
```bash
tshark -D
tshark -i wlan0
tshark -i wlan0 -w Vault/PCAPs/capture_$(date +%Y%m%d_%H%M%S).pcap
tshark -i wlan0 -c 100 -w Vault/PCAPs/capture.pcap
tshark -r Vault/PCAPs/capture.pcap
tshark -i wlan0 -Y "http"
tshark -i wlan0 -Y "dns"
tshark -i wlan0 -Y "ip.addr == 192.168.1.1"
DISPLAY=:1 wireshark Vault/PCAPs/capture.pcap &
```

**Wireshark Troubleshooting:**

| Problem | Fix |
|---|---|
| No interfaces found | Run `termux-setup-storage` and grant permissions |
| Permission denied on capture | Enter Kali proot for root access |
| tshark not found | `apt install tshark -y` inside Kali |
| Wireshark GUI not opening | Make sure X11 is running and `DISPLAY=:1` is set |
| Capture file too large | Add `-c 500` to limit packet count |
| Cannot read pcap file | Run `ls Vault/PCAPs/` to verify path |

---

### 💻 VS Code — Development Environment

**Wake VS Code via Codespaces:**
```bash
# Open Kiwi browser
# Go to github.com/CK-Bachoo/Android-mobile-cybersecurity-workbench
# Tap Code → Codespaces → Create codespace on master
```

**VS Code Troubleshooting:**

| Problem | Fix |
|---|---|
| Codespace takes too long | Close and reopen. Free tier has limits. |
| Changes not saving | Commit and push before closing |
| Terminal not responding | Refresh the browser tab |
| Codespace expired | Create a new one — repo is safe on GitHub |

---

### 🖥️ Local AI — Ollama

Offline AI. No internet required.
Heavy RAM usage. Run ALONE. Never with other tools.

**Wake Ollama — close everything else first:**
```bash
pkill -f jarvis.py && pkill xfce4-session && pkill termux-x11
ollama serve &
ollama run llama3
```

**Stop Ollama:**
```bash
pkill ollama
```

**Ollama Troubleshooting:**

| Problem | Fix |
|---|---|
| Server hangs | `pkill ollama` then `ollama serve &` again |
| Out of memory | Close everything else first |
| Model download fails | Check Wi-Fi. Retry `ollama pull llama3` |
| Phone overheating | Stop immediately. `pkill ollama` |
| Response too slow | Use smaller model `ollama pull phi3` |
| Cannot run with Jarvis | By design. Close Jarvis first. Ollama needs all 12GB. |

---

### ☁️ Cloud AI — Gemini and Claude

Built into Jarvis automatically. Zero local RAM.

**Setup:**
```bash
nano ~/.bashrc
```

Add at bottom:
```bash
export GEMINI_API_KEY="PASTE-YOUR-GEMINI-API-KEY-HERE"
export CLAUDE_API_KEY="PASTE-YOUR-CLAUDE-API-KEY-HERE"
```

Save with CTRL+X then Y then ENTER. Then:
```bash
source ~/.bashrc
```

**Cloud AI Troubleshooting:**

| Problem | Fix |
|---|---|
| Gemini not responding in Jarvis | Run `echo $GEMINI_API_KEY` — if blank run `source ~/.bashrc` |
| API key expired | Generate new key at aistudio.google.com |
| Rate limit hit | Wait 60 seconds. Free tier has limits. |
| Claude not responding | Verify key at console.anthropic.com |
| Keys disappear after restart | Run `source ~/.bashrc` at start of every session |

---

## 🔐 IX. GitHub PAT Cloud Sync

**Step 1 — Generate PAT:**
1. github.com → Profile → Settings → Developer settings
2. Personal access tokens → Tokens classic
3. Generate new token — Note: Termux-Workbench-Push
4. Expiration: 90 days — Check `repo`
5. Generate — COPY IMMEDIATELY

**Step 2 — Store securely:**
```bash
mkdir -p ~/.secrets && chmod 700 ~/.secrets
echo "PASTE-YOUR-PAT-HERE" > ~/.secrets/github_pat.txt
chmod 600 ~/.secrets/github_pat.txt
```

**Step 3 — Load PAT:**
```bash
export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)
```

**Step 4 — Set remote URL:**
```bash
git remote set-url origin https://YOUR-GITHUB-USERNAME:${GITHUB_PAT}@github.com/YOUR-GITHUB-USERNAME/Android-mobile-cybersecurity-workbench.git
```

**Step 5 — Push:**
```bash
git add . && git commit -m "Sync — YOUR-GITHUB-USERNAME" && git push origin master
```

**PAT Troubleshooting:**

| Problem | Fix |
|---|---|
| Authentication failed | Regenerate PAT and run Steps 2-4 again |
| Push rejected | Run `git pull origin master` first then push |
| Fatal not a git repository | `cd ~/Android-mobile-cybersecurity-workbench` |
| Remote already exists | `git remote remove origin` then run Step 4 |
| PAT expired | Generate new 90 day token and repeat Steps 2-4 |
| PAT accidentally committed | Immediately revoke on GitHub. Generate new one. |
| Divergent branches | `git config pull.rebase false && git pull origin master --no-edit && git push origin master` |

---

## 🛰️ X. Operational Commands

```bash
# Network Discovery
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
```

**Operational Commands Troubleshooting:**

| Problem | Fix |
|---|---|
| nmap not found | `pkg install nmap -y` |
| tshark not found | Enter Kali. `apt install tshark -y` |
| git push fails | `export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt)` |
| Vault directory missing | `mkdir -p Vault/Scans Vault/PCAPs Vault/Logs` |
| Wireshark not opening in X11 | Make sure X11 is running first |

---

## ⚡ XI. Wake and Close Commands

### 🎯 Choose Your Operating Mode

**Mode 1 — Full Automation (Recommended):**
```bash
bash scripts/set_wakeword.sh
```
Then type your wake word every session. Example: `bunker`

**Mode 2 — Manual Control:**
Run each tool individually from commands below.

**Mode 3 — Terminal Only:**
Skip X11 entirely. Lightweight. Best for low battery.

---

### 🔑 Wake Word Setup

```bash
bash scripts/set_wakeword.sh
```

| Wake Word | Operator Style |
|---|---|
| bunker | C.K. Bachoo — Original |
| sentinel | Defensive posture |
| nighthawk | Stealth ops |
| fortress | Maximum defense |
| shadow | Low profile |
| jarvis | Classic AI reference |
| ops | Short and tactical |

---

### WAKE COMMANDS

```bash
# Wake environment
source ~/.bashrc && export GITHUB_PAT=$(cat ~/.secrets/github_pat.txt) && cd ~/Android-mobile-cybersecurity-workbench

# Wake X11
termux-x11 :1 & && DISPLAY=:1 xfce4-session &

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
```

### CLOSE COMMANDS

```bash
# Close Jarvis
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
```

**Wake and Close Troubleshooting:**

| Problem | Fix |
|---|---|
| Wake word not recognized | Run `source ~/.bashrc` then try again |
| X11 black after wake | Acquire wakelock from notification bar |
| Jarvis silent after wake | Check termux-api mic permissions |
| Cannot close frozen X11 | Run `pkill -9 -u $(whoami)` nuclear option |
| Wake word gone after restart | Run `source ~/.bashrc` to reload aliases |
| Everything running too slow | Close Ollama first. It consumes all RAM. |

---

## 🌡️ XII. Thermal Safety Protocol

**Check temperature:**
```bash
cat /sys/class/thermal/thermal_zone0/temp
```
Divide by 1000 for Celsius. 45000 = 45C.

**Safe:** Below 40C
**Caution:** 40C to 45C — reduce workload
**Danger:** Above 45C — kill switch immediately

**Thermal kill switch:**
```bash
pkill -9 -u $(whoami)
```

**Monitor every 30 seconds:**
```bash
while true; do
  TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
  echo "Temp: $((TEMP/1000))C"
  sleep 30
done
```
Press CTRL+C to stop.

**Thermal Troubleshooting:**

| Problem | Fix |
|---|---|
| Phone hot during Nmap scan | Normal for intensive scans. Monitor temp. Stop above 45C. |
| Phone hot with Ollama | Expected. Stop immediately above 45C. |
| Phone hot with X11 plus Jarvis | Disable 5G. Use Wi-Fi only during sessions. |
| Thermal sensor not found | Try `cat /sys/class/thermal/thermal_zone1/temp` |
| Phone restarts from heat | Cool 10 minutes. Enable airplane mode during heavy ops. |
| Battery drains fast | Acquire wakelock AND plug in during long sessions. |

---

## 🔧 XIII. Full Troubleshooting Guide

### Termux Issues

| Problem | Fix |
|---|---|
| pkg update fails | Run `termux-change-repo` and select different mirror |
| Package not found | Run `pkg update` first then retry |
| Storage permission denied | Run `termux-setup-storage` and tap Allow |
| Termux killed by Android | Disable battery optimization in Settings |
| Command not found after install | Close and reopen Termux. Run `source ~/.bashrc` |
| Termux crashes on open | Clear app cache in Android Settings → Apps → Termux |

### Git Issues

| Problem | Fix |
|---|---|
| Fatal not a git repository | `cd ~/Android-mobile-cybersecurity-workbench` |
| Authentication failed | Regenerate PAT and run `git remote set-url` again |
| Push rejected | Run `git pull origin master` first then push |
| Divergent branches | `git config pull.rebase false && git pull origin master --no-edit && git push origin master` |
| Merge conflict | Run `git status`. Edit conflicted files. `git add .` then commit. |
| Accidental commit of secrets | Immediately revoke PAT. Generate new one. |

### X11 Issues

| Problem | Fix |
|---|---|
| Black screen | Close Termux-X11 app. Reopen. Run `termux-x11 :1 &` |
| GUI freezes immediately | Acquire wakelock from notification bar first |
| Process killed | Battery optimization must be disabled |
| Display error | Run `export DISPLAY=:1` before any GUI command |
| Cannot find xfce4 | `pkg install xfce4 -y` |
| X11 and Jarvis conflict | Run `bash scripts/bunker_wake.sh` — it sequences them correctly |

### Kali Issues

| Problem | Fix |
|---|---|
| Install hangs | CTRL+C then `proot-distro remove kali` then reinstall |
| apt not found | You are not inside Kali. Run `proot-distro login kali` |
| Tool not found | `apt update && apt install [toolname] -y` inside Kali |
| Kali environment broken | `proot-distro remove kali` then `proot-distro install kali` |

### Network Issues

| Problem | Fix |
|---|---|
| Nmap permission denied | Use `-sn` for ping scan without root |
| No hosts found | Verify same network. Check subnet. |
| tshark no interfaces | Run `termux-setup-storage` and grant permissions |
| Cannot reach GitHub | Check Wi-Fi. Try `ping github.com` |

### Jarvis and AI Issues

| Problem | Fix |
|---|---|
| Jarvis not hearing voice | Check Android mic permissions for Termux-API |
| Gemini API rate limit | Wait 60 seconds. Free tier has limits. |
| Ollama out of memory | Close all other apps. Ollama needs full 12GB. |
| Wake word not working | Run `source ~/.bashrc` then try again |
| API keys not loading | Run `source ~/.bashrc` at start of every session |

---

## 💼 XIV. Business Integration Guide

This repository proves enterprise-level cybersecurity runs on a $400 mobile device.

**Use Cases:**
- Field security audits — no laptop required
- Rapid deployment in resource-constrained environments
- Mobile SOC operations with voice AI command interface
- AI-assisted threat analysis via Jarvis plus Gemini plus Claude
- Voice-commanded network scanning via Jarvis plus Nmap
- Training environments on any Android device
- Disaster recovery — rebuild entire lab from one GitHub clone

**What this architecture proves:**
- Zero Trust security enforced from a mobile device
- Voice AI command interface with confirmation gates
- Full packet capture and analysis via Wireshark and tshark
- Vulnerability scanning via Nmap and Metasploit
- AI-assisted operations via Jarvis, Gemini, Claude, Ollama
- Cloud synchronization with immutable audit trail on GitHub
- Reproducible — any team member clones and deploys in 30 minutes

**Business Integration Troubleshooting:**

| Problem | Fix |
|---|---|
| Team member cannot clone | Verify repo is Public on GitHub |
| Wake word conflicts with team | Each operator runs set_wakeword.sh independently |
| Vault data needs sharing | Copy specific files from Vault manually. Never git add Vault. |
| Jarvis API costs | Gemini free tier handles most operations. Monitor at aistudio.google.com |

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
| AI Integration | AI-Orchestrated Security Operations — Gemini — Claude — Ollama — Jarvis Voice AI Architect |
| Platform | Samsung Galaxy Note 20 Ultra — Exynos 990 — 12GB RAM — 256GB + 512GB MicroSD |
| GitHub | github.com/CK-Bachoo |
| LinkedIn | linkedin.com/in/ckbachoo |
| Status | Mission Ready — March 2026 |

---

**"The mission does not wait for better equipment."**
— C.K. Bachoo, 2026 ⚓🫡
```

---

