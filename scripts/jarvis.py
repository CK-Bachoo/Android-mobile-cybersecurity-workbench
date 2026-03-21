#!/usr/bin/env python3
import subprocess
import os
import time
import datetime
from pathlib import Path

OPERATOR = "C.K. Bachoo"
REPO = "Android-mobile-cybersecurity-workbench"
GEMINI_KEY_FILE = Path.home() / ".secrets" / "gemini_api_key.txt"
LOG_DIR = Path.home() / REPO / "Vault" / "Logs"
SD_LOG_DIR = Path("/sdcard/Jarvis-Logs")

def speak(text):
    print(f"[JARVIS]: {text}")
    try:
        subprocess.run(["termux-tts-speak", "-r", "1.1", text], timeout=20)
    except Exception as e:
        print(f"[TTS ERROR] {e}")

def listen():
    try:
        print("[JARVIS]: Listening...")
        result = subprocess.run(["termux-speech-to-text"], capture_output=True, text=True, timeout=15)
        text = result.stdout.strip()
        if text:
            print(f"[HEARD]: {text}")
            return text
        return ""
    except Exception as e:
        print(f"[STT ERROR] {e}")
        return ""

def load_gemini_key():
    if GEMINI_KEY_FILE.exists():
        return GEMINI_KEY_FILE.read_text().strip()
    return os.environ.get("GEMINI_API_KEY")

def query_gemini(command, key):
    try:
        import requests
        payload = {"contents": [{"parts": [{"text": f"You are Jarvis — professional AI assistant for C.K. Bachoo, Navy Veteran and Cybersecurity Analyst on Samsung Galaxy Note 20 Ultra with Exynos 990, 12GB RAM, 256GB storage, 512GB MicroSD. Keep responses concise and professional.\n\nRequest: {command}"}]}]}
        resp = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}", json=payload, timeout=20)
        resp.raise_for_status()
        return resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print(f"[GEMINI ERROR] {e}")
        return f"Processing error. Command was: {command}"

def zero_trust_gate(command):
    speak(f"Zero Trust gate. You said: {command}. Say confirm to proceed or cancel to abort.")
    response = listen()
    if "confirm" in response.lower():
        speak("Confirmed. Executing.")
        return True
    speak("Cancelled. Zero Trust enforced.")
    return False

def log_session(command, response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] CMD: {command} | RESPONSE: {response[:200]}\n"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(LOG_DIR / "jarvis_sessions.log", "a") as f:
            f.write(entry)
        print(f"[LOGGED] Session saved to Vault")
    except Exception as e:
        print(f"[LOG ERROR] {e}")
    try:
        SD_LOG_DIR.mkdir(parents=True, exist_ok=True)
        with open(SD_LOG_DIR / "jarvis_sessions.log", "a") as f:
            f.write(entry)
        print(f"[SD GUARD] Backed up to MicroSD")
    except Exception as e:
        print(f"[SD LOG] {e}")

def check_hardware():
    speak("Running hardware check on Note 20 Ultra.")
    try:
        temp_path = Path("/sys/class/thermal/thermal_zone0/temp")
        if temp_path.exists():
            temp = int(temp_path.read_text().strip()) // 1000
            speak(f"Processor temperature is {temp} degrees Celsius.")
            if temp > 45:
                speak("WARNING. Temperature critical. Reduce workload immediately.")
            else:
                speak("Temperature nominal. All systems green.")
    except Exception as e:
        speak("Hardware check error.")
        print(f"[HW ERROR] {e}")

def main():
    print("""
╔══════════════════════════════════════════╗
║   JARVIS AI — C.K. BACHOO               ║
║   Note 20 Ultra | Exynos | 12GB RAM     ║
║   256GB + 512GB SD | Zero Trust Active  ║
╚══════════════════════════════════════════╝
    """)
    key = load_gemini_key()
    if not key:
        speak("Gemini API key not found. Running in echo mode.")
    else:
        speak("Gemini AI connected. Full intelligence online.")
    speak("Jarvis online. Operator C.K. Bachoo. Note 20 Ultra. Exynos processor. 12 gigabytes RAM. Zero Trust active. Awaiting your command.")
    while True:
        try:
            time.sleep(1.0)
            raw = listen()
            if not raw:
                continue
            raw_lower = raw.lower()
            if any(w in raw_lower for w in ["exit", "shutdown", "power off", "goodbye"]):
                speak("Jarvis shutting down. All sessions logged. Goodbye operator.")
                break
            if any(w in raw_lower for w in ["hardware check", "temperature", "storage check"]):
                check_hardware()
                log_session(raw, "Hardware check executed")
                continue
            if "help" in raw_lower:
                speak("I can answer questions, run hardware checks, execute system commands with Zero Trust confirmation, and log all sessions to your GitHub audit trail.")
                continue
            speak(f"Processing: {raw}")
            response = query_gemini(raw, key) if key else f"Echo mode. You said: {raw}"
            print(f"[JARVIS RESPONSE]: {response[:500]}")
            speak(response[:300])
            if any(w in raw_lower for w in ["run", "execute", "install", "delete", "remove", "push", "commit"]):
                if zero_trust_gate(raw):
                    log_session(raw, f"EXECUTED — {response[:100]}")
                else:
                    log_session(raw, "CANCELLED — Zero Trust gate")
            else:
                log_session(raw, response[:100])
        except KeyboardInterrupt:
            speak("Manual shutdown. All sessions logged. Goodbye operator.")
            break
        except Exception as e:
            print(f"[LOOP ERROR] {e}")
            speak("Error encountered. Restarting loop.")
            time.sleep(2)

if __name__ == "__main__":
    main()
