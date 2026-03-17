# Android Mobile Cybersecurity Workbench: Setup and Deployment Guide
Identity: Veteran-Built Security Node / C.K. Bachoo

> "The mission doesn't stop because we don't have a laptop or a desktop. We get mobile."

## Setup Instructions
1. **Initialize:** `pkg update && pkg upgrade -y`
2. **Tools:** `pkg install git gh nano nodejs -y`
3. **AI Engine:** `curl -fsSL https://ollama.com/install.sh | sh`
4. **Pull Models:** `ollama serve &` then `ollama pull deepseek-coder:1.3b-instruct`

## Verified Hardware Compatibility
- Samsung Note Series: Note 10, Note 10+, Note 10 Lite, Note 20, Note 20 Ultra 5G
- Samsung S-Series: S21 Ultra through S26 Ultra
- Samsung Z-Fold Series: Z Fold 4 through Z Fold 8
- Google Pixel Series: 6 Pro through 10 Pro

## Architecture: Multi-Model AI Bridge
- Cloud Layer: Currently utilizing Gemini 3 Flash
- Local Engine: Ollama v0.17.7
- Local Models: DeepSeek-Coder 1.3B, Llama 3.2 1B, Bunker
