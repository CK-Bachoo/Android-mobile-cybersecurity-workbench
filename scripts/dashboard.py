#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import subprocess
from datetime import datetime, timezone

PORT = 8080
LOG_FILE = os.path.expanduser("~/Project-Dreadnought/vault/logs/threat_radar.json")

class DreadnoughtGodModeHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        if self.path == "/api/command":
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode('utf-8'))
                cmd = payload.get("command", "").strip().lower()
                
                response_payload = {"output": ""}
                
                if cmd == "ping":
                    try:
                        res = subprocess.run(["ping", "-c", "2", "127.0.0.1"], capture_output=True, text=True, timeout=5)
                        response_payload["output"] = res.stdout if res.returncode == 0 else res.stderr
                    except Exception as e:
                        response_payload["output"] = f"Execution error: {str(e)}"
                elif cmd:
                    response_payload["output"] = f"[SYSTEM] Directive '{cmd}' received. Command validation matrix active. Restricted environment."
                else:
                    response_payload["output"] = "Empty directive."
                    
                self.wfile.write(json.dumps(response_payload).encode('utf-8'))
            except Exception as e:
                self.wfile.write(json.dumps({"output": f"Fatal processing loop anomaly: {str(e)}"}).encode('utf-8'))
                
        elif self.path == "/api/telemetry":
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode('utf-8'))
                if "timestamp" not in payload:
                    payload["timestamp"] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
                with open(LOG_FILE, "a") as f:
                    f.write(json.dumps(payload) + "\n")
                self.wfile.write(b'{"status":"success"}')
            except Exception:
                pass

    def do_GET(self):
        if self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            data = []
            if os.path.exists(LOG_FILE):
                try:
                    with open(LOG_FILE, "r") as f:
                        lines = f.readlines()[-40:]
                        for line in lines:
                            if line.strip():
                                data.append(json.loads(line.strip()))
                except Exception:
                    pass
            self.wfile.write(json.dumps(data[::-1]).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>G0DM0D3 COCKPIT</title>
                <style>
                    body { background-color: #030303; color: #00ff66; font-family: monospace; padding: 12px; margin: 0; }
                    .header { border: 1px solid #00ff66; padding: 10px; margin-bottom: 15px; text-align: center; background: #090909; }
                    .grid-main { display: flex; flex-direction: column; gap: 15px; }
                    @media (min-width: 768px) {
                        .grid-main { display: grid; grid-template-columns: repeat(12, 1fr); }
                        .col-left { grid-column: span 4; display: flex; flex-direction: column; gap: 15px; }
                        .col-right { grid-column: span 8; display: flex; flex-direction: column; gap: 15px; }
                    }
                    .card { border: 1px solid #00ff66; padding: 12px; background: #070707; }
                    .card h3 { margin-top: 0; color: #ffffff; border-bottom: 1px dashed #00ff66; padding-bottom: 4px; font-size: 14px; text-transform: uppercase; }
                    .metric-box { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #003311; }
                    .metric-val { font-weight: bold; transition: all 0.3s ease; }
                    .agent-tag { color: #ffcc00; font-weight: bold; }
                    .terminal-view { background: #010101; border: 1px solid #004411; padding: 10px; overflow-y: auto; font-size: 11px; }
                    .log-entry { margin-bottom: 6px; border-left: 2px solid #00ff66; padding-left: 6px; }
                    .ANOMALY, .NETWORK_DOWN { color: #ff3333; border-color: #ff3333; }
                    .changed { color: #ffffff !important; text-shadow: 0 0 10px #ffffff; transform: scale(1.1); }
                    input[type="text"] { background: #000; color: #00ff66; border: 1px solid #00ff66; padding: 8px; width: 100%; font-family: monospace; box-sizing: border-box; outline: none; margin-top: 5px; }
                    input[type="text"]:focus { border-color: #ffffff; }
                    button { background: #00ff66; color: #000; border: none; padding: 8px 15px; font-weight: bold; cursor: pointer; font-family: monospace; width: 100%; margin-top: 10px; }
                    button:hover { background: #ffffff; }
                </style>
            </head>
            <body>
                <div class="header">
                    <div style="font-size: 16px; font-weight: bold;">PROJECT DREADNOUGHT // G0DM0D3 COCKPIT</div>
                    <div style="font-size: 10px; color: #888;">MOBILE-FIRST SOC TELEMETRY & COGNITIVE INTERFACE</div>
                </div>
                <div class="grid-main">
                    <div class="col-left">
                        <div class="card">
                            <h3>SYSTEM MATRIX</h3>
                            <div class="metric-box"><span>WATCHDOG</span><span class="metric-val" id="watchdog-status" style="color:#ff3333;">OFFLINE</span></div>
                            <div class="metric-box"><span>ACTIVE_INTERFACE</span><span class="metric-val" id="active-iface">SCANNING</span></div>
                            <div class="metric-box"><span>SOCKETS_MONITORED</span><span class="metric-val" id="socket-vol">0</span></div>
                        </div>
                        <div class="card">
                            <h3>ARCHITECT'S LEDGER</h3>
                            <div class="metric-box"><span style="color:#ffcc00;">GLASSWING: CLASSIFIED</span></div>
                            <div style="font-size: 10px; color: #888; margin-top: 10px;">Zero-Trust DevSecOps pipeline active.</div>
                        </div>
                        <div class="card">
                            <h3>INTELLIGENCE CORE</h3>
                            <div class="metric-box"><span>PRIMARY_XO</span><span class="agent-tag">GEMINI_ULTRA</span></div>
                            <div class="metric-box"><span>LAB_MENTOR</span><span class="agent-tag">CLAUDE_3.5</span></div>
                        </div>
                        <div class="card">
                            <h3>COMMAND UPLINK</h3>
                            <input type="text" id="ai-input" placeholder="> AWAITING DIRECTIVE..." onkeypress="if(event.key === 'Enter') submitPrompt()">
                            <button onclick="submitPrompt()">TRANSMIT</button>
                        </div>
                    </div>
                    <div class="col-right">
                        <div class="card">
                            <h3>TACTICAL RADAR</h3>
                            <div class="terminal-view" id="radar-feed" style="height: 320px;"></div>
                        </div>
                        <div class="card">
                            <h3>COGNITIVE OUTPUT</h3>
                            <div class="terminal-view" id="ai-output" style="height: 200px; color: #ffcc00;">[SYSTEM] Local Ollama / Remote API targets standing by. Awaiting input.</div>
                        </div>
                    </div>
                </div>
                <script>
                    function animateValue(id, newValue) {
                        const el = document.getElementById(id);
                        if (el.innerText !== newValue) {
                            el.innerText = newValue;
                            el.classList.add('changed');
                            setTimeout(() => el.classList.remove('changed'), 400);
                        }
                    }
                    async function updateGrid() {
                        try {
                            const res = await fetch('/api/telemetry');
                            const data = await res.json();
                            const radarFeed = document.getElementById('radar-feed');
                            radarFeed.innerHTML = '';

                            const now = new Date();
                            let watchdogActive = false;

                            if (data.length > 0) {
                                const top = data[0];
                                const logTime = new Date(top.timestamp);
                                if ((now - logTime) < 45000) {
                                    watchdogActive = true;
                                }

                                const cMatch = top.message.match(/Connections:\\s*(\\d+)/);
                                if(cMatch) animateValue('socket-vol', cMatch[1]);

                                const iMatch = top.message.match(/interface:\\s*([^|\\n]+)/);
                                if(iMatch) animateValue('active-iface', iMatch[1].trim());
                            }

                            const wdStatus = document.getElementById('watchdog-status');
                            if (watchdogActive) {
                                wdStatus.innerText = "ONLINE";
                                wdStatus.style.color = "#00ff66";
                                wdStatus.style.textShadow = "0 0 4px #00ff66";
                            } else {
                                wdStatus.innerText = "OFFLINE";
                                wdStatus.style.color = "#ff3333";
                                wdStatus.style.textShadow = "none";
                            }

                            data.forEach(entry => {
                                const d = document.createElement('div');
                                d.className = `log-entry ${entry.event}`;
                                d.innerText = `[${entry.timestamp.split('T')[1].substring(0,8)}] [${entry.event}] ${entry.message}`;
                                radarFeed.appendChild(d);
                            });
                        } catch(e) {}
                    }

                    async function submitPrompt() {
                        const inputField = document.getElementById('ai-input');
                        const outputBox = document.getElementById('ai-output');
                        const prompt = inputField.value.trim();
                        if (!prompt) return;

                        outputBox.innerHTML += `<br><br><span style="color:#ffffff;">> TRANSMITTED: ${prompt}</span>`;
                        inputField.value = '';
                        outputBox.scrollTop = outputBox.scrollHeight;

                        try {
                            const response = await fetch('/api/command', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ command: prompt })
                            });
                            const result = await response.json();
                            outputBox.innerHTML += `<br><span style="color:#00bcff;">[COCKPIT_KERNEL]</span><br><span style="color:#ffffff;">${result.output.replace(/\\n/g, '<br>')}</span>`;
                        } catch (error) {
                            outputBox.innerHTML += `<br><span style="color:#ff3333;">[COMMS_ERROR] Failed to communicate with local kernel subsystem.</span>`;
                        }
                        outputBox.scrollTop = outputBox.scrollHeight;
                    }

                    setInterval(updateGrid, 5000);
                    updateGrid();
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), DreadnoughtGodModeHandler) as httpd:
        httpd.allow_reuse_address = True
        httpd.serve_forever()
