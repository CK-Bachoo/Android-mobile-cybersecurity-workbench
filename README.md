```markdown
# 🛡️ Android Mobile Cybersecurity Workbench (The Bunker) v2.8

**Mobile-first Purple Team automation lab** engineered for ARM64 Android environments (Samsung Galaxy Note 20 Ultra + Termux). 

This repository stands as living proof that enterprise-grade security operations, proactive threat hunting, defensive automation, and zero-trust AI orchestration can execute flawlessly on constrained mobile hardware. Built on the core philosophy that the mission does not wait for better equipment, this workbench bypasses standard x86 hypervisor limitations by leveraging native Linux sub-systems and remote cloud-bridge infrastructure.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-2.8-blue)
![Platform](https://img.shields.io/badge/Platform-Android_Termux-orange)

**Current Role**: Cybersecurity Innovation Fellow — The Knowledge House NY (IF-CS-26)  
**Operator**: C.K. Bachoo | Navy Veteran  

---

## 📋 Table of Contents

- [Executive Summary & Philosophy](#executive-summary--philosophy)
- [Architectural Paradigm: Desktop vs. Mobile](#architectural-paradigm-desktop-vs-mobile)
- [v2.8 Release Highlights & Automation Suite](#v28-release-highlights--automation-suite)
- [Hardware & Deployment Stack](#hardware--deployment-stack)
- [GodMode AI Orchestration & Local Fallback](#godmode-ai-orchestration--local-fallback)
- [Zero Trust & OPSEC Protocols](#zero-trust--opsec-protocols)
- [Quick Start](#-quick-start)

---

## Executive Summary & Philosophy

When standard computing infrastructure fails or is unavailable, security operations must maintain continuity. Following a total system hardware failure, this entire workbench was pivoted to a mobile-native architecture. Operating under a disciplined, stoic framework, the Bunker strips away resource-heavy graphical user interfaces (GUIs) in favor of raw command-line interface (CLI) execution, Python-driven automation, and secure API routing. 

Every script and protocol in this repository is designed to execute with maximum efficiency, zero third-party dependencies where possible, and strict adherence to NIST Cybersecurity Framework compliance.

---

## Architectural Paradigm: Desktop vs. Mobile

Standard cybersecurity curriculum relies heavily on x86 architecture and Type-2 hypervisors (VirtualBox, VMware). To achieve the same learning and operational objectives on an ARM64 mobile device without rooting the kernel (triggering Samsung Knox hardware trips), tactical workarounds are deployed.

| Operational Requirement | Standard Desktop User (x86) | Android Cyber Workbench (Note 20 Ultra) |
| :--- | :--- | :--- |
| **Execution Environment** | Heavy Local VirtualBox VMs | Ephemeral Google Cloud Shell Bridge / Termux PRoot |
| **Network Isolation** | Local VM Subnets | Direct Docker Subnet Routing / VPN Tunneling |
| **Privilege Escalation** | Standard `sudo` binary abuse | Native Headless Binary Exploitation (GTFOBins) |
| **Graphical Rendering** | Native Desktop GUI (GNOME/KDE) | Termux-X11 / VirGL Hardware Acceleration |
| **Artifact Synchronization**| Native Desktop IDE | Termux Git CLI ➔ GitHub |

*Technical Analysis:* By utilizing Google Cloud Shell and GitHub Codespaces as a remote compute layer, enterprise-grade containers are orchestrated directly from the mobile terminal. This Mobile-to-Cloud Bridge offloads thermal strain and compute risks to an isolated sandbox, preserving the integrity of the local mobile device while establishing a secure, encrypted command and control pipeline.

---

## v2.8 Release Highlights & Automation Suite

All Python automation scripts are built with **zero third-party dependencies** (utilizing only the Python Standard Library) to prevent RAM spikes, avoid dependency conflicts, and eliminate Android Signal 9 (Out of Memory) kernel kills on the Exynos 990 processor.

- **`bunker_audit.sh`** — The core NIST-style mobile security audit engine. Verifies root status, ADB daemon state, VPN tunnel interfaces, active listening ports, and ensures the automation script arsenal is fully intact. Outputs severity-sorted, color-coded terminal reports.

### The Python Arsenal (`scripts/` directory)

| Script | Operational Purpose | Technical Mechanism |
| :--- | :--- | :--- |
| **`privacy_guard.py`** | Pre-Commit Data Sanitization | Automatically scrubs PII, secrets, API keys, and public IP addresses from logs before Git pushes. Whitelists safe private ranges (127.x, 10.x). |
| **`port_harden.py`** | Continuous Port Sentry | Polls local network states every 15 seconds. Monitors Port 8022 (SSH) and 8080 (AI Server). Any unauthorized external IP binding triggers immediate isolation. |
| **`air_gap_isolate.py`** | Trap-Door Emergency Isolation | Triggered by the port sentry. Instantly drops `wlan0` and `rmnet_data*` interfaces via `ip link set down`, zeroes out `~/.bash_history`, and flushes volatile memory to lock out intruders. |
| **`osint_agent.py`** | Passive Reconnaissance | Performs DNS resolution, multi-record `dig` enumeration (A/AAAA/MX/TXT/NS), WHOIS lookups, and TCP connect probes without requiring `nmap` or root access. |
| **`threat_hunt_logs.py`**| TTP & IoC Log Analyzer | Scans access logs against 18 specific Indicators of Compromise (IoC) patterns, including SQL injection, directory traversal, and command injection. |

---

## Hardware & Deployment Stack

- **Primary Device**: Samsung Galaxy Note 20 Ultra 5G
- **Compute Specs**: Exynos 990, 12GB LPDDR5 RAM, 256GB Internal Storage + High-Speed MicroSD Vault
- **Operating Environment**: Termux + PRoot-Distro (Kali/Ubuntu) + Termux-X11
- **Cloud Bridge**: Google Cloud Shell, GitHub Codespaces, AWS (us-east-2) for serverless offloading.

---

## GodMode AI Orchestration & Local Fallback

The Bunker integrates advanced AI orchestration while strictly maintaining a Zero Trust security posture. 

1. **GodMode Web Wrapper:** Deploys a unified, lightweight interface for concurrent access to Claude, Gemini, and ChatGPT. By serving the UI locally over a Python HTTP server, it bypasses standard Android browser memory limits and prevents the OS from crashing under heavy NodeJS/npm dependencies.
2. **MCP Security (Model Context Protocol):** To prevent "God-Mode" privilege escalation (e.g., tool poisoning), all agentic MCP tools are strictly sandboxed. Client-Side Validation strips Prompt Injection vectors, and agents are restricted to read-only access for critical log directories.
3. **Local Fallback (Ollama + Gemma 2B):** When operating in highly sensitive environments or during network degradation, the workbench relies on 100% local, offline inference. This allows for the autonomous parsing of sensitive telemetry without leaking proprietary data to cloud providers. *(Note: Ollama requires dedicated RAM allocation and is never run simultaneously with the X11 GUI to maintain thermal safety).*

---

## Zero Trust & OPSEC Protocols

- **Vault Isolation:** Sensitive data (scans, PCAPs, raw logs) is stored in the `Vault/` directory. This directory is strictly excluded via `.gitignore` and is physically mapped to the encrypted MicroSD card.
- **VPN Kill Switch:** Layer 3 traffic isolation is enforced via Android's "Block connections without VPN" kernel setting. The Termux terminal operates as a "Ghost," preventing local network eavesdropping on SSH sessions or payload deliveries.
- **Immutable Ledger:** Every session artifact is staged, committed with descriptive operational messages, and pushed to this repository to create a cryptographically hashed, timestamped forensic ledger of all operations.

---

## 🚀 Quick Start

To deploy the audit engine and verify the integrity of the local environment:

```bash
# Navigate to the workbench root
cd ~/Android-mobile-cybersecurity-workbench

# Grant execution permissions to the Python suite and bash engine
chmod 700 scripts/*.py && chmod +x bunker_audit.sh

# Execute the primary system diagnostic
bash bunker_audit.sh

# Optional: Run a passive OSINT sweep on an authorized domain
python3 scripts/osint_agent.py example.com

```
**"The mission does not wait for better equipment."** — C.K. Bachoo 🫡
*For detailed forensic reports, incident response playbooks, and threat intelligence logs, refer to the THREAT_INTEL_LOG.md file within this repository.*
```

```
