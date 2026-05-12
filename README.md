# 🛡️ Android Mobile Cybersecurity Workbench

Mobile-first cybersecurity lab built on Android + Termux for defensive automation, log analysis, and hands-on learning in DevSecOps and incident response.

This repository documents how I build and test practical security workflows on constrained hardware. I am actively developing my skills toward DevSecOps, incident response, security operations, and technical documentation, and I use AI-assisted analysis responsibly to support learning, triage, and workflow organization.

**Current Deployment:** The Knowledge House NY Innovation Fellowship (IF-CS-26)  
**Operator:** C.K. Bachoo | Navy Veteran  
**Full Portfolio:** [IF-Cyber-Portfolio](https://github.com/CK-Bachoo/IF-Cyber-Portfolio)

---

## Overview

This project shows how a cybersecurity workflow can be built from a mobile-first environment when a traditional desktop lab is not available. It combines Linux utilities, Python automation, Git, SSH, cloud-assisted workflows, and local AI support to create a practical learning environment.

The goal is to stay organized, document work clearly, and build habits that support real-world security operations.

---

## Professional Focus

I am building practical skills toward roles in:

- DevSecOps and infrastructure automation.
- Incident response and threat triage.
- Security operations and Purple Team workflows.
- Defensive scripting and log analysis.
- GRC and technical documentation.

---

## What This Repo Demonstrates

- Mobile-to-cloud security workflows.
- Defensive automation with Python and shell scripting.
- Log parsing, triage, and basic threat hunting.
- Zero Trust habits in constrained environments.
- AI-assisted analysis for note-taking, summarization, and workflow support.

---

## Environment

- Samsung Galaxy Note 20 Ultra.
- Android + Termux.
- Linux command-line utilities.
- Python 3, Git, SSH, and cloud-assisted lab tools.
- Optional local AI support for offline analysis.

---

## Automation Suite

The `scripts/` directory contains lightweight tools designed to support security workflows without heavy dependencies.

| Script | Purpose |
| :--- | :--- |
| `bunker_audit.sh` | Checks the local lab environment and confirms key services and settings. |
| `privacy_guard.py` | Helps sanitize logs and redact sensitive data before sharing. |
| `port_harden.py` | Monitors local network exposure and flags unexpected changes. |
| `air_gap_isolate.py` | Supports emergency isolation workflows for safety and containment. |
| `threat_hunt_logs.py` | Scans logs for suspicious patterns and indicators of compromise. |

---

## AI-Assisted Workflow

I use AI as a support tool, not a replacement for judgment. It helps with:

- Summarizing logs and notes.
- Drafting documentation.
- Organizing observations.
- Supporting triage and review.

When handling sensitive material, I prefer local or controlled workflows whenever possible.

---

## Zero Trust Habits

- Sensitive files stay in excluded vault locations.
- Secrets and tokens are never committed to the repo.
- Logs and notes are reviewed before publishing.
- The environment is designed to support safe, controlled learning.

---

## Why This Exists

This repository is my technical proving ground. It reflects my progression as a cybersecurity learner who is serious about defensive work, documentation, and continuous improvement.

I am honest about my current level, but I am committed to learning, taking on challenges responsibly, and building the skills needed for future work in DevSecOps and incident response.

---

## Quick Start

```bash
cd ~/Android-mobile-cybersecurity-workbench
chmod 700 scripts/*.py
chmod +x bunker_audit.sh
bash bunker_audit.sh
Connect
Open to connecting on mobile security, DevSecOps, automation, Purple Team topics, and practical cybersecurity learning.