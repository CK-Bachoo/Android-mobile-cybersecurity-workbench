#!/usr/bin/env python3
import http.server
import socketserver
import os
import json

PORT = 8080
LOG_FILE = os.path.expanduser("~/Project-Dreadnought/vault/logs/threat_radar.json")

class DreadnoughtHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

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
                        lines = f.readlines()[-50:]
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
            html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>G0DM0D3 // PROJECT DREADNOUGHT</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    background: #030303;
    color: #00ff66;
    font-family: 'Courier New', monospace;
    padding: 12px;
    overflow-x: hidden;
  }

  /* HEADER */
  .header {
    border: 1px solid #00ff66;
    padding: 12px;
    text-align: center;
    background: #060606;
    box-shadow: 0 0 20px rgba(0,255,102,0.15);
    margin-bottom: 12px;
  }
  .header-title {
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 4px;
    text-shadow: 0 0 10px #00ff66;
  }
  .header-sub {
    font-size: 10px;
    color: #666;
    margin-top: 4px;
    letter-spacing: 2px;
  }
  .header-operator {
    font-size: 11px;
    color: #00ccff;
    margin-top: 6px;
  }

  /* BLINK */
  .blink { animation: blink 1.2s step-end infinite; }
  @keyframes blink { 50% { opacity: 0; } }

  /* STATUS BAR */
  .status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #003311;
    background: #040404;
    padding: 6px 12px;
    margin-bottom: 12px;
    font-size: 11px;
    flex-wrap: wrap;
    gap: 6px;
  }
  .status-item { display: flex; align-items: center; gap: 6px; }
  .dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00ff66;
    box-shadow: 0 0 6px #00ff66;
    animation: pulse 2s infinite;
  }
  .dot.red { background: #ff3333; box-shadow: 0 0 6px #ff3333; }
  .dot.yellow { background: #ffcc00; box-shadow: 0 0 6px #ffcc00; }
  @keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:0.4;} }

  /* GRID */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }

  /* CARDS */
  .card {
    border: 1px solid #00ff66;
    background: #070707;
    padding: 12px;
    border-radius: 2px;
  }
  .card-red { border-color: #ff3333; }
  .card-blue { border-color: #00ccff; }
  .card-yellow { border-color: #ffcc00; }

  .card h3 {
    font-size: 11px;
    letter-spacing: 2px;
    color: #fff;
    border-bottom: 1px dashed #00ff66;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }
  .card-red h3 { border-color: #ff3333; }
  .card-blue h3 { border-color: #00ccff; color: #00ccff; }
  .card-yellow h3 { border-color: #ffcc00; color: #ffcc00; }

  /* METRICS */
  .metric {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px solid #0a1a0a;
    font-size: 11px;
  }
  .metric:last-child { border-bottom: none; }
  .metric-label { color: #888; }
  .metric-val {
    font-weight: bold;
    color: #00ff66;
    text-shadow: 0 0 4px #00ff66;
  }
  .metric-val.red { color: #ff3333; text-shadow: 0 0 4px #ff3333; }
  .metric-val.blue { color: #00ccff; text-shadow: 0 0 4px #00ccff; }
  .metric-val.yellow { color: #ffcc00; text-shadow: 0 0 4px #ffcc00; }

  /* AI AGENTS */
  .agent-row {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 0;
    border-bottom: 1px solid #0a1a0a;
    font-size: 11px;
  }
  .agent-row:last-child { border-bottom: none; }
  .agent-icon {
    width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    flex-shrink: 0;
  }
  .agent-name { font-weight: bold; color: #ffcc00; }
  .agent-role { color: #666; font-size: 10px; }
  .agent-status { margin-left: auto; font-size: 10px; color: #00ff66; }

  /* TERMINAL */
  .terminal {
    background: #010101;
    border: 1px solid #003311;
    padding: 10px;
    height: 200px;
    overflow-y: auto;
    font-size: 11px;
    line-height: 1.5;
    border-radius: 2px;
  }
  .terminal::-webkit-scrollbar { width: 4px; }
  .terminal::-webkit-scrollbar-track { background: #010101; }
  .terminal::-webkit-scrollbar-thumb { background: #003311; }

  .log-line {
    padding: 2px 0 2px 8px;
    border-left: 2px solid #00ff66;
    margin-bottom: 4px;
    word-break: break-all;
  }
  .log-HEARTBEAT { color: #00ff66; border-color: #00ff66; }
  .log-SYSTEM_BOOT { color: #00ccff; border-color: #00ccff; }
  .log-NETWORK_DOWN { color: #ff3333; border-color: #ff3333; animation: alarm 1.5s infinite; }
  .log-ANOMALY { color: #ff3333; border-color: #ff3333; animation: alarm 1.5s infinite; }
  @keyframes alarm { 0%,100%{opacity:1;} 50%{opacity:0.3;} }

  .terminal-label {
    font-size: 10px;
    color: #444;
    margin-bottom: 6px;
    letter-spacing: 1px;
  }

  /* HARDWARE BAR */
  .hw-bar-wrap { margin: 6px 0; }
  .hw-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    color: #666;
    margin-bottom: 3px;
  }
  .hw-bar {
    height: 6px;
    background: #0a1a0a;
    border-radius: 3px;
    overflow: hidden;
  }
  .hw-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #00ff66, #00cc44);
    border-radius: 3px;
    transition: width 1s ease;
    box-shadow: 0 0 6px #00ff66;
  }

  /* FOOTER */
  .footer {
    text-align: center;
    padding: 10px;
    font-size: 10px;
    color: #333;
    border-top: 1px solid #0a1a0a;
    margin-top: 10px;
    letter-spacing: 1px;
  }

  /* SCAN LINE EFFECT */
  body::after {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,255,102,0.01) 2px,
      rgba(0,255,102,0.01) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="header-title">G0DM0D3 // PROJECT DREADNOUGHT <span class="blink">_</span></div>
  <div class="header-sub">PURPLE TEAM COMMAND CENTER // ZERO-TRUST ACTIVE // ARM64 MOBILE SOC</div>
  <div class="header-operator">OPERATOR: C.K. BACHOO // NAVY VETERAN // IF-CS-26 NY // EXYNOS 990</div>
</div>

<!-- STATUS BAR -->
<div class="status-bar">
  <div class="status-item"><div class="dot"></div><span>NODE_01_TERMUX: ONLINE</span></div>
  <div class="status-item"><div class="dot"></div><span>NODE_02_GCP: ONLINE</span></div>
  <div class="status-item"><div class="dot"></div><span>NODE_03_CHROME: ONLINE</span></div>
  <div class="status-item"><div class="dot yellow"></div><span>IFACE: <span id="active-iface">SCANNING...</span></span></div>
  <div class="status-item"><div class="dot"></div><span>ZERO-TRUST: ACTIVE</span></div>
  <div class="status-item"><span style="color:#666;">LAST UPDATE: <span id="last-update">--:--:--</span></span></div>
</div>

<!-- ROW 1: AI AGENTS + HARDWARE + SECURITY -->
<div class="grid-3">

  <!-- AI ORCHESTRATION -->
  <div class="card card-yellow">
    <h3>🤖 G0DM0D3 INTELLIGENCE CORE</h3>
    <div class="agent-row">
      <div class="agent-icon" style="background:#1a1a00;">🔮</div>
      <div><div class="agent-name">GEMINI ULTRA</div><div class="agent-role">PRIMARY XO / RECON</div></div>
      <div class="agent-status">● ACTIVE</div>
    </div>
    <div class="agent-row">
      <div class="agent-icon" style="background:#001a0a;">🛡️</div>
      <div><div class="agent-name">CLAUDE</div><div class="agent-role">LAB MENTOR / ARCHITECT</div></div>
      <div class="agent-status">● ACTIVE</div>
    </div>
    <div class="agent-row">
      <div class="agent-icon" style="background:#001a1a;">⚡</div>
      <div><div class="agent-name">GROK</div><div class="agent-role">RECON LOGIC / REASONING</div></div>
      <div class="agent-status">● ACTIVE</div>
    </div>
    <div class="agent-row">
      <div class="agent-icon" style="background:#1a0000;">🎙️</div>
      <div><div class="agent-name">JARVIS VOICE</div><div class="agent-role">VOICE INTERFACE</div></div>
      <div class="agent-status" style="color:#ffcc00;">● STANDBY</div>
    </div>
  </div>

  <!-- HARDWARE -->
  <div class="card card-blue">
    <h3>⚙️ HARDWARE MATRIX // NOTE 20 ULTRA</h3>
    <div class="metric">
      <span class="metric-label">PROCESSOR</span>
      <span class="metric-val blue">EXYNOS 990 ARM64</span>
    </div>
    <div class="metric">
      <span class="metric-label">RAM</span>
      <span class="metric-val blue">12GB LPDDR5</span>
    </div>
    <div class="metric">
      <span class="metric-label">STORAGE</span>
      <span class="metric-val blue">256GB + 512GB SD</span>
    </div>
    <div class="metric">
      <span class="metric-label">KNOX</span>
      <span class="metric-val blue">ACTIVE</span>
    </div>
    <div class="hw-bar-wrap">
      <div class="hw-bar-label"><span>MOBILE SOC UTILIZATION</span><span id="soc-pct">ARM64</span></div>
      <div class="hw-bar"><div class="hw-bar-fill" id="soc-bar" style="width:42%"></div></div>
    </div>
    <div class="hw-bar-wrap">
      <div class="hw-bar-label"><span>NETWORK TELEMETRY</span><span id="net-pct"><span id="socket-vol">0</span> SOCKETS</span></div>
      <div class="hw-bar"><div class="hw-bar-fill" id="net-bar" style="width:20%;background:linear-gradient(90deg,#00ccff,#0099cc);box-shadow:0 0 6px #00ccff;"></div></div>
    </div>
  </div>

  <!-- SECURITY STATUS -->
  <div class="card">
    <h3>🔒 SECURITY STATUS</h3>
    <div class="metric">
      <span class="metric-label">ZERO TRUST</span>
      <span class="metric-val">ENFORCED</span>
    </div>
    <div class="metric">
      <span class="metric-label">VAULT ISOLATION</span>
      <span class="metric-val">PROTECTED</span>
    </div>
    <div class="metric">
      <span class="metric-label">PII SANITIZER</span>
      <span class="metric-val">ACTIVE</span>
    </div>
    <div class="metric">
      <span class="metric-label">LOG ROTATION</span>
      <span class="metric-val">5MB CAP</span>
    </div>
    <div class="metric">
      <span class="metric-label">WATCHDOG</span>
      <span class="metric-val" id="watchdog-status">SCANNING...</span>
    </div>
    <div class="metric">
      <span class="metric-label">TOTAL EVENTS</span>
      <span class="metric-val" id="total-events">0</span>
    </div>
  </div>

</div>

<!-- ROW 2: TACTICAL RADAR + PHASE MAP -->
<div class="grid">

  <!-- TACTICAL RADAR FEED -->
  <div class="card">
    <h3>📡 TACTICAL RADAR // LIVE TELEMETRY STREAM</h3>
    <div class="terminal-label">[DREADNOUGHT WATCHDOG — HEARTBEAT INTERVAL: 30s — PII: REDACTED]</div>
    <div class="terminal" id="radar-feed">
      <div style="color:#333;">[ AWAITING TELEMETRY... ]</div>
    </div>
  </div>

  <!-- ARCHITECT'S LEDGER / PHASE MAP -->
  <div class="card card-blue">
    <h3>🗺️ ARCHITECT'S LEDGER // EVOLUTION PHASES</h3>
    <div class="metric">
      <span class="metric-label">PHASE 1</span>
      <span class="metric-val blue">IF-CYBER-PORTFOLIO</span>
    </div>
    <div style="font-size:10px;color:#444;padding:2px 0 6px 0;">Academic Foundation — 29+ sessions, NIST CSF mapped</div>
    <div class="metric">
      <span class="metric-label">PHASE 2</span>
      <span class="metric-val blue">ANDROID-MOBILE-SOC</span>
    </div>
    <div style="font-size:10px;color:#444;padding:2px 0 6px 0;">Mobile Workbench — Purple Team, Bunker Config</div>
    <div class="metric">
      <span class="metric-label">PHASE 3</span>
      <span class="metric-val yellow">PROJECT DREADNOUGHT</span>
    </div>
    <div style="font-size:10px;color:#444;padding:2px 0 6px 0;">Private XDR Frontier — Watchdog + Multi-AI SOC</div>
    <div class="metric" style="margin-top:8px;">
      <span class="metric-label">NEXT: GLASSWING</span>
      <span class="metric-val red">CLASSIFIED</span>
    </div>
    <div style="font-size:10px;color:#444;padding:2px 0 0 0;">AI-Security frontier — Post-graduation reveal</div>
  </div>

</div>

<!-- ROW 3: EVENT COUNTERS -->
<div class="grid-3">
  <div class="card" style="text-align:center;padding:16px;">
    <div style="font-size:28px;font-weight:bold;text-shadow:0 0 10px #00ff66;" id="count-heartbeat">0</div>
    <div style="font-size:10px;color:#666;margin-top:4px;letter-spacing:2px;">HEARTBEAT EVENTS</div>
  </div>
  <div class="card card-blue" style="text-align:center;padding:16px;">
    <div style="font-size:28px;font-weight:bold;color:#00ccff;text-shadow:0 0 10px #00ccff;" id="count-boot">0</div>
    <div style="font-size:10px;color:#666;margin-top:4px;letter-spacing:2px;">SYSTEM BOOTS</div>
  </div>
  <div class="card card-red" style="text-align:center;padding:16px;">
    <div style="font-size:28px;font-weight:bold;color:#ff3333;text-shadow:0 0 10px #ff3333;" id="count-anomaly">0</div>
    <div style="font-size:10px;color:#666;margin-top:4px;letter-spacing:2px;">ANOMALIES / NETWORK DOWN</div>
  </div>
</div>

<!-- FOOTER -->
<div class="footer">
  G0DM0D3 v2.0 // PROJECT DREADNOUGHT // PURPLE TEAM COMMAND CENTER // MOBILE-FIRST ZERO-TRUST ARCHITECTURE
  <br>C.K. BACHOO // NAVY VETERAN // THE KNOWLEDGE HOUSE IF-CS-26 NY // ALL SYSTEMS OPERATIONAL
</div>

<script>
async function updateDashboard() {
  try {
    const res = await fetch('/api/telemetry');
    const data = await res.json();

    if (data.length === 0) return;

    // Update last update time
    const now = new Date();
    document.getElementById('last-update').innerText =
      now.toTimeString().substring(0,8);

    // Update active interface from latest heartbeat
    const latest = data[0];
    const ifaceMatch = latest.message.match(/interface:\\s*(.+)/);
    if (ifaceMatch) {
      document.getElementById('active-iface').innerText = ifaceMatch[1].trim();
    }

    // Count events
    let heartbeats = 0, boots = 0, anomalies = 0;
    data.forEach(e => {
      if (e.event === 'HEARTBEAT') heartbeats++;
      else if (e.event === 'SYSTEM_BOOT') boots++;
      else if (e.event === 'NETWORK_DOWN' || e.event === 'ANOMALY') anomalies++;
    });

    document.getElementById('count-heartbeat').innerText = heartbeats;
    document.getElementById('count-boot').innerText = boots;
    document.getElementById('count-anomaly').innerText = anomalies;
    document.getElementById('total-events').innerText = data.length;
    document.getElementById('socket-vol').innerText = heartbeats;

    // Network bar scales with heartbeat count (max 50)
    const netPct = Math.min((heartbeats / 50) * 100, 100);
    document.getElementById('net-bar').style.width = netPct + '%';

    // Watchdog status
    const lastEvent = data[0];
    const lastTs = new Date(lastEvent.timestamp);
    const secAgo = Math.floor((Date.now() - lastTs) / 1000);
    const wdEl = document.getElementById('watchdog-status');
    if (secAgo < 120) {
      wdEl.innerText = 'ONLINE (' + secAgo + 's ago)';
      wdEl.className = 'metric-val';
    } else {
      wdEl.innerText = 'STALE (' + secAgo + 's ago)';
      wdEl.className = 'metric-val red';
    }

    // Render radar feed
    const feed = document.getElementById('radar-feed');
    feed.innerHTML = '';
    data.slice(0, 30).forEach(entry => {
      const d = document.createElement('div');
      d.className = 'log-line log-' + entry.event;
      const ts = entry.timestamp.split('T')[1].substring(0,8);
      d.innerText = '[' + ts + '] [' + entry.event + '] ' + entry.message;
      feed.appendChild(d);
    });

  } catch(e) {
    document.getElementById('watchdog-status').innerText = 'OFFLINE';
    document.getElementById('watchdog-status').className = 'metric-val red';
  }
}

// Animate SOC bar on load
setTimeout(() => {
  const bar = document.getElementById('soc-bar');
  const pct = 35 + Math.floor(Math.random() * 20);
  bar.style.width = pct + '%';
  document.getElementById('soc-pct').innerText = pct + '%';
}, 500);

setInterval(updateDashboard, 5000);
updateDashboard();
</script>
</body>
</html>"""
            self.wfile.write(html.encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), DreadnoughtHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"[+] G0DM0D3 // Project Dreadnought dashboard live on http://127.0.0.1:{PORT}")
        httpd.serve_forever()
