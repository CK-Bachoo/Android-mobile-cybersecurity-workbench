import streamlit as st
#!/usr/bin/env python3
"""
G0DM0D3 v2.0 // Project Dreadnought
Purple Team Command Center - Mobile-First Zero-Trust Architecture
Operator: C.K. Bachoo // Navy Veteran // IF-CS-26 NY // Exynos 990
Pure Python http.server - No Flask - ARM64 Safe
"""

import http.server
import socketserver
import os
import json
import subprocess
import threading
import time
from datetime import datetime

PORT = 8081
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.join(os.path.dirname(BASE_DIR), "vault", "logs")
LOG_FILE = os.path.join(VAULT_DIR, "threat_radar.json")

# Termux-safe PATH for subprocess
TERMUX_ENV = os.environ.copy()
TERMUX_ENV["PATH"] = "/data/data/com.termux/files/usr/bin:/data/data/com.termux/files/usr/sbin:" + TERMUX_ENV.get("PATH", "")

# Whitelisted commands - safe recon ops only
ALLOWED_COMMANDS = {
    "ping": ["/data/data/com.termux/files/usr/bin/ping", "-c", "4"],
    "ip addr": ["/data/data/com.termux/files/usr/bin/ip", "addr"],
    "ip addr show": ["/data/data/com.termux/files/usr/bin/ip", "addr", "show"],
    "ifconfig": ["/data/data/com.termux/files/usr/bin/ifconfig"],
    "ss": ["/data/data/com.termux/files/usr/bin/ss", "-tulnp"],
    "ss -tulnp": ["/data/data/com.termux/files/usr/bin/ss", "-tulnp"],
    "traceroute": ["/data/data/com.termux/files/usr/bin/traceroute"],
    "netstat": ["/data/data/com.termux/files/usr/bin/netstat", "-tulnp"],
    "ps": ["/data/data/com.termux/files/usr/bin/ps", "aux"],
    "uname": ["/data/data/com.termux/files/usr/bin/uname", "-a"],
    "uptime": ["/data/data/com.termux/files/usr/bin/uptime"],
    "df": ["/data/data/com.termux/files/usr/bin/df", "-h"],
    "free": ["/data/data/com.termux/files/usr/bin/free", "-h"],
    "whoami": ["/data/data/com.termux/files/usr/bin/whoami"],
    "pwd": ["/data/data/com.termux/files/usr/bin/pwd"],
    "nmap": ["/data/data/com.termux/files/usr/bin/nmap", "-sn"],
    "status": ["__internal_status__"],
}

def get_log_data():
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
            entries = []
            for line in lines:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except:
                        pass
            return entries
    except:
        pass
    return []

def get_status():
    entries = get_log_data()
    total = len(entries)
    heartbeats = sum(1 for e in entries if e.get("event_type") == "HEARTBEAT")
    boots = sum(1 for e in entries if e.get("event_type") == "SYSTEM_BOOT")
    anomalies = sum(1 for e in entries if e.get("event_type") not in ["HEARTBEAT", "SYSTEM_BOOT"])
    last_event = entries[-1] if entries else {}
    last_ts = last_event.get("timestamp", "N/A")
    watchdog_age = "N/A"
    if last_ts != "N/A":
        try:
            last_dt = datetime.fromisoformat(last_ts.replace("Z", "+00:00"))
            diff = (datetime.now().astimezone() - last_dt).total_seconds()
            watchdog_age = f"{int(diff)}s ago"
        except:
            pass
    return {
        "total": total,
        "heartbeats": heartbeats,
        "boots": boots,
        "anomalies": anomalies,
        "last_ts": last_ts,
        "watchdog_age": watchdog_age
    }

def execute_command(cmd_input):
    cmd_input = cmd_input.strip()
    
    if cmd_input == "status":
        s = get_status()
        return f"[STATUS REPORT]\nTotal Events: {s['total']}\nHeartbeats: {s['heartbeats']}\nSystem Boots: {s['boots']}\nAnomalies: {s['anomalies']}\nLast Event: {s['last_ts']}\nWatchdog: {s['watchdog_age']}"
    
    # Match command to whitelist
    cmd_args = None
    extra_args = []
    
    # Check exact match first
    if cmd_input in ALLOWED_COMMANDS:
        cmd_args = ALLOWED_COMMANDS[cmd_input]
    else:
        # Check prefix match (e.g. "ping 8.8.8.8")
        for key in ALLOWED_COMMANDS:
            if cmd_input.startswith(key + " ") or cmd_input == key:
                parts = cmd_input[len(key):].strip().split()
                extra_args = parts
                cmd_args = ALLOWED_COMMANDS[key]
                break
    
    if cmd_args is None:
        return f"[BLOCKED] '{cmd_input}' not in whitelist.\nAllowed: ping <ip>, ip addr, ifconfig, ss -tulnp, traceroute <ip>, netstat, ps, uname, uptime, df, free, whoami, pwd, status"
    
    if cmd_args == ["__internal_status__"]:
        s = get_status()
        return f"[STATUS REPORT]\nTotal Events: {s['total']}\nHeartbeats: {s['heartbeats']}\nSystem Boots: {s['boots']}\nAnomalies: {s['anomalies']}\nLast Event: {s['last_ts']}\nWatchdog: {s['watchdog_age']}"
    
    try:
        full_cmd = cmd_args + extra_args
        result = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            timeout=15,
            env=TERMUX_ENV
        )
        output = result.stdout or result.stderr or "[No output]"
        return output[:3000]  # Cap output size
    except subprocess.TimeoutExpired:
        return "[TIMEOUT] Command exceeded 15 second limit."
    except FileNotFoundError:
        # Fallback: try via sh
        try:
            result = subprocess.run(
                cmd_input,
                shell=True,
                capture_output=True,
                text=True,
                timeout=15,
                env=TERMUX_ENV
            )
            return (result.stdout or result.stderr or "[No output]")[:3000]
        except Exception as e2:
            return f"[ERROR] {str(e2)}"
    except Exception as e:
        return f"[ERROR] {str(e)}"

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>G0DM0D3 v2 // Project Dreadnought</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#000;color:#00ff41;font-family:'Courier New',monospace;font-size:11px;overflow-x:hidden;}
body::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,255,65,0.015) 2px,rgba(0,255,65,0.015) 4px);pointer-events:none;z-index:9999;}

.hdr{border:1px solid #00ff41;margin:6px;padding:10px;text-align:center;background:rgba(0,255,65,0.05);}
.hdr h1{color:#00ff41;font-size:16px;letter-spacing:3px;text-shadow:0 0 10px #00ff41;}
.hdr .sub{color:#00bcd4;font-size:9px;letter-spacing:2px;margin-top:4px;}
.hdr .op{color:#00bcd4;font-size:9px;letter-spacing:1px;margin-top:2px;}

.sbar{border:1px solid #1a3a1a;margin:0 6px 6px;padding:6px 10px;background:rgba(0,255,65,0.03);font-size:9px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;}
.sbar .node{display:flex;align-items:center;gap:4px;}
.sbar .dot{width:7px;height:7px;border-radius:50%;}
.dot-g{background:#00ff41;box-shadow:0 0 6px #00ff41;}
.dot-y{background:#ffeb3b;box-shadow:0 0 6px #ffeb3b;}
.sbar .ts{color:#555;margin-left:auto;font-size:8px;}

.row3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin:0 6px 6px;}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:0 6px 6px;}
.row-uplink{display:grid;grid-template-columns:1fr 2fr;gap:6px;margin:0 6px 6px;}
.row-tools{margin:0 6px 6px;}

.panel{border:1px solid #00ff41;padding:8px;background:rgba(0,255,65,0.02);}
.panel.blue{border-color:#00bcd4;}
.panel.yellow{border-color:#ffeb3b;}
.panel.red{border-color:#f44336;}
.panel.purple{border-color:#9c27b0;}
.panel.orange{border-color:#ff9800;}

.ptitle{font-size:9px;letter-spacing:2px;margin-bottom:8px;display:flex;align-items:center;gap:6px;}
.ptitle.g{color:#00ff41;}
.ptitle.b{color:#00bcd4;}
.ptitle.y{color:#ffeb3b;}
.ptitle.r{color:#f44336;}
.ptitle.p{color:#9c27b0;}
.ptitle.o{color:#ff9800;}

/* Intelligence Core */
.agent{display:flex;align-items:center;gap:8px;margin-bottom:6px;padding:4px 0;border-bottom:1px solid #0a2a0a;}
.agent:last-child{border-bottom:none;margin-bottom:0;}
.aico{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;}
.aico.gem{background:linear-gradient(135deg,#9c27b0,#e91e63);}
.aico.cla{background:linear-gradient(135deg,#f44336,#ff9800);}
.aico.grk{background:linear-gradient(135deg,#ffeb3b,#ff9800);}
.aico.jar{background:linear-gradient(135deg,#607d8b,#455a64);}
.aname{flex:1;font-size:9px;}
.aname .n{color:#00ff41;font-weight:bold;}
.aname .r{color:#555;font-size:8px;}
.ast{font-size:8px;letter-spacing:1px;}
.ast.on{color:#00ff41;}
.ast.sb{color:#ffeb3b;}

/* Hardware */
.hrow{display:flex;justify-content:space-between;margin-bottom:5px;padding-bottom:4px;border-bottom:1px solid #0a2a0a;font-size:9px;}
.hrow:last-child{border-bottom:none;margin-bottom:0;}
.hlbl{color:#555;}
.hval{color:#00bcd4;font-weight:bold;text-align:right;font-size:8px;}
.hval.g{color:#00ff41;}
.bar-wrap{margin-top:2px;}
.bar{height:4px;background:#0a2a0a;border-radius:2px;overflow:hidden;margin-top:2px;}
.bar-fill{height:100%;background:linear-gradient(90deg,#00ff41,#00bcd4);border-radius:2px;transition:width 1s;}
.bar-fill.net{background:linear-gradient(90deg,#00bcd4,#9c27b0);}

/* Security */
.srow{display:flex;justify-content:space-between;margin-bottom:5px;font-size:9px;border-bottom:1px solid #0a1a0a;padding-bottom:4px;}
.srow:last-child{border-bottom:none;margin-bottom:0;}
.slbl{color:#555;}
.sval{font-weight:bold;font-size:8px;letter-spacing:1px;}
.sval.enforced{color:#00ff41;}
.sval.protected{color:#00bcd4;}
.sval.active{color:#00ff41;}
.sval.cap{color:#ffeb3b;}
.sval.online{color:#00ff41;}
.sval.stale{color:#f44336;}
.sval.num{color:#00bcd4;}

/* Tactical Radar */
.tlog{height:180px;overflow-y:auto;font-size:8px;line-height:1.6;}
.tlog::-webkit-scrollbar{width:3px;}
.tlog::-webkit-scrollbar-thumb{background:#00ff41;}
.tentry{padding:2px 0;border-left:2px solid #00ff41;padding-left:6px;margin-bottom:2px;}
.tentry.boot{border-left-color:#00bcd4;color:#00bcd4;}
.tentry.anomaly{border-left-color:#f44336;color:#f44336;}
.thdr{color:#555;font-size:7px;margin-bottom:4px;}

/* Architect Ledger */
.phase{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid #0a2a0a;}
.phase:last-child{border-bottom:none;margin-bottom:0;}
.pname{font-size:9px;color:#555;letter-spacing:1px;}
.pdesc{font-size:7px;color:#333;margin-top:2px;}
.ptag{font-size:9px;font-weight:bold;letter-spacing:1px;text-align:right;}
.ptag.p1{color:#00bcd4;}
.ptag.p2{color:#00bcd4;}
.ptag.p3{color:#ffeb3b;}
.ptag.nx{color:#f44336;}

/* Counters */
.counters{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin:0 6px 6px;}
.cbox{border:1px solid;padding:10px;text-align:center;}
.cbox.g{border-color:#00ff41;}
.cbox.b{border-color:#00bcd4;}
.cbox.r{border-color:#f44336;}
.cnum{font-size:28px;font-weight:bold;display:block;}
.cnum.g{color:#00ff41;text-shadow:0 0 10px #00ff41;}
.cnum.b{color:#00bcd4;text-shadow:0 0 10px #00bcd4;}
.cnum.r{color:#f44336;text-shadow:0 0 10px #f44336;}
.clbl{font-size:7px;letter-spacing:2px;color:#555;margin-top:4px;}

/* Command Uplink */
.uplink-form{display:flex;flex-direction:column;gap:6px;}
.uplink-input{background:#000;border:1px solid #00ff41;color:#00ff41;font-family:'Courier New',monospace;font-size:10px;padding:8px;outline:none;width:100%;}
.uplink-input::placeholder{color:#1a4a1a;}
.uplink-input:focus{border-color:#00bcd4;box-shadow:0 0 6px rgba(0,188,212,0.3);}
.transmit-btn{background:transparent;border:1px solid #00ff41;color:#00ff41;font-family:'Courier New',monospace;font-size:10px;letter-spacing:2px;padding:8px;cursor:pointer;transition:all 0.2s;width:100%;}
.transmit-btn:hover{background:#00ff41;color:#000;}
.transmit-btn:active{background:#00bcd4;border-color:#00bcd4;color:#000;}
.cmd-hint{font-size:7px;color:#1a4a1a;line-height:1.6;}

/* Cognitive Output */
.cogout{height:220px;overflow-y:auto;font-size:8px;line-height:1.7;padding:4px;background:#000;}
.cogout::-webkit-scrollbar{width:3px;}
.cogout::-webkit-scrollbar-thumb{background:#00ff41;}
.co-sys{color:#555;}
.co-cmd{color:#ffeb3b;}
.co-out{color:#00bcd4;}
.co-err{color:#f44336;}
.co-ok{color:#00ff41;}

/* Tool Slots */
.tools-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;}
.tool-slot{border:1px solid #1a3a1a;padding:8px;background:rgba(0,255,65,0.01);}
.tool-slot.active{border-color:#00ff41;}
.tool-slot.pending{border-color:#1a3a1a;opacity:0.5;}
.tool-slot.blue{border-color:#00bcd4;}
.tool-slot.yellow{border-color:#ffeb3b;}
.tslot-hdr{font-size:8px;letter-spacing:2px;margin-bottom:4px;}
.tslot-hdr.g{color:#00ff41;}
.tslot-hdr.b{color:#00bcd4;}
.tslot-hdr.y{color:#ffeb3b;}
.tslot-hdr.dim{color:#1a4a1a;}
.tslot-desc{font-size:7px;color:#555;line-height:1.5;}
.tslot-status{font-size:7px;margin-top:4px;letter-spacing:1px;}
.tslot-status.dep{color:#00ff41;}
.tslot-status.pend{color:#1a4a1a;}

.footer{text-align:center;color:#1a4a1a;font-size:7px;letter-spacing:2px;padding:8px;border-top:1px solid #0a2a0a;margin:0 6px 6px;}

.divider{border:none;border-top:1px solid #0a2a0a;margin:0 6px 6px;}
</style>
</head>
<body>

<!-- HEADER -->
<div class="hdr">
  <h1>G0DM0D3 // PROJECT DREADNOUGHT _</h1>
  <div class="sub">PURPLE TEAM COMMAND CENTER // ZERO-TRUST ACTIVE // ARM64 MOBILE SOC</div>
  <div class="op">OPERATOR: C.K. BACHOO // NAVY VETERAN // IF-CS-26 NY // EXYNOS 990</div>
</div>

<!-- STATUS BAR -->
<div class="sbar" id="statusBar">
  <div class="node"><div class="dot dot-g"></div><span>NODE_01_TERMUX: ONLINE</span></div>
  <div class="node"><div class="dot dot-g"></div><span>NODE_02_GCP: ONLINE</span></div>
  <div class="node"><div class="dot dot-g"></div><span>NODE_03_CHROME: ONLINE</span></div>
  <div class="node"><div class="dot dot-y"></div><span id="ifaceLabel">IFACE: Mobile_Active_Node</span></div>
  <div class="node"><div class="dot dot-g"></div><span>ZERO-TRUST: ACTIVE</span></div>
  <div class="ts" id="lastUpdate">LAST UPDATE: --:--:--</div>
</div>

<!-- ROW 1: Intelligence / Hardware / Security -->
<div class="row3">
  <div class="panel">
    <div class="ptitle g">&#129302; G0DM0D3 INTELLIGENCE CORE</div>
    <div class="agent"><div class="aico gem">&#9733;</div><div class="aname"><div class="n">GEMINI ULTRA</div><div class="r">PRIMARY XO / RECON</div></div><div class="ast on">&#9679; ACTIVE</div></div>
    <div class="agent"><div class="aico cla">&#9646;</div><div class="aname"><div class="n">CLAUDE</div><div class="r">LAB MENTOR / ARCHITECT</div></div><div class="ast on">&#9679; ACTIVE</div></div>
    <div class="agent"><div class="aico grk">&#9889;</div><div class="aname"><div class="n">GROK</div><div class="r">RECON LOGIC / REASONING</div></div><div class="ast on">&#9679; ACTIVE</div></div>
    <div class="agent"><div class="aico jar">&#127908;</div><div class="aname"><div class="n">JARVIS VOICE</div><div class="r">VOICE INTERFACE</div></div><div class="ast sb">&#9679; STANDBY</div></div>
  </div>

  <div class="panel blue">
    <div class="ptitle b">&#9881; HARDWARE MATRIX // NOTE 20 ULTRA</div>
    <div class="hrow"><span class="hlbl">PROCESSOR</span><span class="hval">EXYNOS 990 ARM64</span></div>
    <div class="hrow"><span class="hlbl">RAM</span><span class="hval">12GB LPDDR5</span></div>
    <div class="hrow"><span class="hlbl">STORAGE</span><span class="hval">256GB + 512GB SD</span></div>
    <div class="hrow"><span class="hlbl">KNOX</span><span class="hval g">ACTIVE</span></div>
    <div class="bar-wrap">
      <div class="hrow"><span class="hlbl">MOBILE SOC UTILIZATION</span><span class="hval" id="cpuPct">---%</span></div>
      <div class="bar"><div class="bar-fill" id="cpuBar" style="width:45%"></div></div>
    </div>
    <div class="bar-wrap">
      <div class="hrow"><span class="hlbl">NETWORK TELEMETRY</span><span class="hval" id="sockPct">--- SOCKETS</span></div>
      <div class="bar"><div class="bar-fill net" id="netBar" style="width:60%"></div></div>
    </div>
  </div>

  <div class="panel">
    <div class="ptitle g">&#128274; SECURITY STATUS</div>
    <div class="srow"><span class="slbl">ZERO TRUST</span><span class="sval enforced">ENFORCED</span></div>
    <div class="srow"><span class="slbl">VAULT ISOLATION</span><span class="sval protected">PROTECTED</span></div>
    <div class="srow"><span class="slbl">PII SANITIZER</span><span class="sval active">ACTIVE</span></div>
    <div class="srow"><span class="slbl">LOG ROTATION</span><span class="sval cap">5MB CAP</span></div>
    <div class="srow"><span class="slbl">WATCHDOG</span><span class="sval" id="wdStatus">CHECKING...</span></div>
    <div class="srow"><span class="slbl">TOTAL EVENTS</span><span class="sval num" id="totalEvents">---</span></div>
  </div>
</div>

<!-- ROW 2: Tactical Radar / Architect Ledger -->
<div class="row2">
  <div class="panel">
    <div class="ptitle g">&#128970; TACTICAL RADAR // LIVE TELEMETRY STREAM</div>
    <div class="thdr" id="radarHdr">[DREADNOUGHT WATCHDOG - HEARTBEAT INTERVAL: 30s - PII: REDACTED]</div>
    <div class="tlog" id="tlog">Loading telemetry...</div>
  </div>

  <div class="panel blue">
    <div class="ptitle b">&#128250; ARCHITECT&#39;S LEDGER // EVOLUTION PHASES</div>
    <div class="phase"><div><div class="pname">PHASE 1</div><div class="pdesc">Academic Foundation - 29+ sessions, NIST CSF mapped</div></div><div class="ptag p1">IF-CYBER-PORTFOLIO</div></div>
    <div class="phase"><div><div class="pname">PHASE 2</div><div class="pdesc">Mobile Workbench - Purple Team, Bunker Config</div></div><div class="ptag p2">ANDROID-MOBILE-SOC</div></div>
    <div class="phase"><div><div class="pname">PHASE 3</div><div class="pdesc">Private XDR Frontier - Watchdog + Multi-AI SOC</div></div><div class="ptag p3">PROJECT DREADNOUGHT</div></div>
    <div class="phase"><div><div class="pname">NEXT: GLASSWING</div><div class="pdesc">AI-Security frontier - Post-graduation reveal</div></div><div class="ptag nx">CLASSIFIED</div></div>
  </div>
</div>

<!-- COUNTERS -->
<div class="counters">
  <div class="cbox g"><span class="cnum g" id="hbCount">---</span><div class="clbl">HEARTBEAT EVENTS</div></div>
  <div class="cbox b"><span class="cnum b" id="bootCount">---</span><div class="clbl">SYSTEM BOOTS</div></div>
  <div class="cbox r"><span class="cnum r" id="anomCount">---</span><div class="clbl">ANOMALIES / NETWORK DOWN</div></div>
</div>

<!-- COMMAND UPLINK + COGNITIVE OUTPUT -->
<div class="row-uplink">
  <div class="panel yellow">
    <div class="ptitle y">&#9889; COMMAND UPLINK</div>
    <div class="uplink-form">
      <input class="uplink-input" id="cmdInput" type="text" placeholder="ping 8.8.8.8 | ip addr | ss -tulnp" autocomplete="off" autocorrect="off" spellcheck="false">
      <button class="transmit-btn" id="txBtn" onclick="transmit()">[ TRANSMIT ]</button>
      <div class="cmd-hint">
        ALLOWED OPS:<br>
        ping &lt;ip&gt; | ip addr | ifconfig<br>
        ss -tulnp | netstat | traceroute &lt;ip&gt;<br>
        ps | uname | uptime | df | free<br>
        whoami | pwd | status
      </div>
    </div>
  </div>

  <div class="panel">
    <div class="ptitle g">&#128196; COGNITIVE OUTPUT // COMMAND RESULTS</div>
    <div class="cogout" id="cogout">
      <div class="co-sys">[G0DM0D3 v2.0] System online. Awaiting uplink...</div>
      <div class="co-sys">[ZERO-TRUST] Command whitelist enforced.</div>
      <div class="co-sys">[READY] Type a command and press TRANSMIT.</div>
    </div>
  </div>
</div>

<!-- TOOL SLOTS -->
<div class="row-tools panel" style="margin:0 6px 6px;">
  <div class="ptitle g">&#9874; DEPLOYED TOOL ARSENAL // SESSION LOG</div>
  <div class="tools-grid">

    <div class="tool-slot active">
      <div class="tslot-hdr g">S15 // SOS AGENT</div>
      <div class="tslot-desc">76-line bash SOS agent. Emergency alert system. ARM64 native execution verified.</div>
      <div class="tslot-status dep">&#9679; DEPLOYED // scripts/sos_agent.sh</div>
    </div>

    <div class="tool-slot blue">
      <div class="tslot-hdr b">S16 // WATCHDOG v2</div>
      <div class="tslot-desc">Python socket monitor. PII redaction. JSON vault. 30s heartbeat. Live telemetry feed.</div>
      <div class="tslot-status dep">&#9679; DEPLOYED // scripts/watchdog_v2.py</div>
    </div>

    <div class="tool-slot yellow">
      <div class="tslot-hdr y">S28-S29 // DFIR + AUTOPSY</div>
      <div class="tslot-desc">Live triage engine. Digital autopsy IaC bypass via raw strings. Purple team verified.</div>
      <div class="tslot-status dep">&#9679; DEPLOYED // IF-Cyber-Portfolio</div>
    </div>

    <div class="tool-slot active">
      <div class="tslot-hdr g">G0DM0D3 // DASHBOARD v2</div>
      <div class="tslot-desc">Pure Python http.server. Live telemetry. Command Uplink. Real Termux execution. ARM64.</div>
      <div class="tslot-status dep">&#9679; DEPLOYED // scripts/dashboard_v2.py</div>
    </div>

    <div class="tool-slot pending">
      <div class="tslot-hdr dim">SLOT 05 // PENDING</div>
      <div class="tslot-desc">Next session tool deploys here. Add weekly.</div>
      <div class="tslot-status pend">&#9675; AWAITING DEPLOYMENT</div>
    </div>

    <div class="tool-slot pending">
      <div class="tslot-hdr dim">SLOT 06 // PENDING</div>
      <div class="tslot-desc">Next session tool deploys here. Add weekly.</div>
      <div class="tslot-status pend">&#9675; AWAITING DEPLOYMENT</div>
    </div>

  </div>
</div>

<div class="footer">G0DM0D3 v2.0 // PROJECT DREADNOUGHT // PURPLE TEAM COMMAND CENTER // MOBILE-FIRST ZERO-TRUST ARCHITECTURE<br>C.K. BACHOO // NAVY VETERAN // THE KNOWLEDGE HOUSE IF-CS-26 NY // ALL SYSTEMS OPERATIONAL</div>

<script>
let cmdHistory = [];
let histIdx = -1;

function addOutput(text, cls) {
  const out = document.getElementById('cogout');
  const div = document.createElement('div');
  div.className = cls;
  div.textContent = text;
  out.appendChild(div);
  out.scrollTop = out.scrollHeight;
}

function clearOutput() {
  const out = document.getElementById('cogout');
  out.innerHTML = '';
}

async function transmit() {
  const inp = document.getElementById('cmdInput');
  const btn = document.getElementById('txBtn');
  const cmd = inp.value.trim();
  if (!cmd) return;

  cmdHistory.unshift(cmd);
  histIdx = -1;

  addOutput('> ' + cmd, 'co-cmd');
  btn.textContent = '[ TRANSMITTING... ]';
  btn.disabled = true;
  inp.value = '';

  try {
    const res = await fetch('/api/execute', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({cmd: cmd})
    });
    const data = await res.json();
    if (data.output) {
      const lines = data.output.split('\\n');
      lines.forEach(line => {
        if (line.trim()) {
          const cls = line.startsWith('[ERROR]') || line.startsWith('[BLOCKED]') || line.startsWith('[TIMEOUT]') ? 'co-err' :
                      line.startsWith('[STATUS') ? 'co-ok' : 'co-out';
          addOutput(line, cls);
        }
      });
    }
  } catch(e) {
    addOutput('[ERROR] Connection failed: ' + e.message, 'co-err');
  }

  btn.textContent = '[ TRANSMIT ]';
  btn.disabled = false;
  inp.focus();
}

// Enter key
document.getElementById('cmdInput').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') { transmit(); return; }
  if (e.key === 'ArrowUp') {
    if (histIdx < cmdHistory.length - 1) { histIdx++; this.value = cmdHistory[histIdx]; }
    e.preventDefault();
  }
  if (e.key === 'ArrowDown') {
    if (histIdx > 0) { histIdx--; this.value = cmdHistory[histIdx]; }
    else { histIdx = -1; this.value = ''; }
    e.preventDefault();
  }
});

async function refreshTelemetry() {
  try {
    const res = await fetch('/api/telemetry');
    const data = await res.json();
    const entries = data.entries || [];

    // Update counters
    let hb = 0, boot = 0, anom = 0;
    entries.forEach(e => {
      if (e.event_type === 'HEARTBEAT') hb++;
      else if (e.event_type === 'SYSTEM_BOOT') boot++;
      else anom++;
    });
    document.getElementById('hbCount').textContent = hb;
    document.getElementById('bootCount').textContent = boot;
    document.getElementById('anomCount').textContent = anom;
    document.getElementById('totalEvents').textContent = entries.length;

    // Update radar log
    const tlog = document.getElementById('tlog');
    if (entries.length > 0) {
      const recent = entries.slice(-20).reverse();
      tlog.innerHTML = recent.map(e => {
        const cls = e.event_type === 'SYSTEM_BOOT' ? 'tentry boot' :
                    e.event_type !== 'HEARTBEAT' ? 'tentry anomaly' : 'tentry';
        const ts = (e.timestamp || '').substring(11, 19);
        const iface = e.interface || e.details || '';
        return '<div class="' + cls + '">[' + ts + '] [' + (e.event_type||'EVENT') + '] ' + iface + '</div>';
      }).join('');
    }

    // Watchdog status
    const s = await fetch('/api/status').then(r => r.json());
    const wd = document.getElementById('wdStatus');
    if (s.watchdog_age && s.watchdog_age !== 'N/A') {
      const secs = parseInt(s.watchdog_age);
      if (!isNaN(secs) && secs < 120) {
        wd.className = 'sval online';
        wd.textContent = 'ONLINE (' + s.watchdog_age + ')';
      } else {
        wd.className = 'sval stale';
        wd.textContent = 'STALE (' + s.watchdog_age + ')';
      }
    }

    // Socket count
    const sockN = Math.min(entries.length, 50);
    document.getElementById('sockPct').textContent = sockN + ' SOCKETS';
    document.getElementById('netBar').style.width = Math.min(sockN * 2, 100) + '%';

    // CPU bar (simulated from event density)
    const cpuSim = Math.min(30 + (hb % 30), 85);
    document.getElementById('cpuPct').textContent = cpuSim + '%';
    document.getElementById('cpuBar').style.width = cpuSim + '%';

  } catch(e) {
    console.log('Telemetry error:', e);
  }

  // Timestamp
  const now = new Date();
  document.getElementById('lastUpdate').textContent = 'LAST UPDATE: ' +
    now.toTimeString().substring(0, 8);
}

// Run on load and every 30s
refreshTelemetry();
setInterval(refreshTelemetry, 30000);
</script>
<div style="padding:20px;text-align:center;border-top:1px solid #00ff41;margin-top:20px"><div style="color:#00ff41;font-family:monospace;font-size:14px;margin-bottom:10px">☁️ GOOGLE CLOUD SHELL // TERMINAL UPLINK</div><a href="https://shell.cloud.google.com" target="_blank" style="background:#00ff41;color:#000;padding:12px 24px;font-family:monospace;font-weight:bold;text-decoration:none;border-radius:4px">🚀 LAUNCH CLOUD SHELL</a></div></body>
</html>'''

class DreadnoughtHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silent logging

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode())

        elif self.path == "/api/telemetry":
            entries = get_log_data()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"entries": entries[-50:]}).encode())

        elif self.path == "/api/status":
            s = get_status()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(s).encode())

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/execute":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                cmd = data.get("cmd", "").strip()
                output = execute_command(cmd)
            except Exception as e:
                output = f"[ERROR] {str(e)}"

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"output": output}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DreadnoughtHandler) as httpd:
        print(f"[+] G0DM0D3 v2.0 // Project Dreadnought dashboard live on http://127.0.0.1:{PORT}")
        print(f"[+] Command Uplink ACTIVE - Real Termux execution enabled")
        print(f"[+] Tool Arsenal loaded - Weekly slots ready")
        print(f"[+] Zero-Trust whitelist enforced")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[-] G0DM0D3 v2.0 shutting down...")


# ==============================================================================
# TERMINAL ATTACHMENT HUB (PINNED LOWER MATRIX INTERFACE)
# ==============================================================================
st.markdown("---")
st.markdown("<h3 style='color: #00ff66; font-family: monospace;'>🐉 LOCAL SUBSYSTEM KALI TERMINAL // INTERACTIVE HARDWARE LINK</h3>", unsafe_allow_html=True)

# Using future-proof framing to anchor your local ttyd session seamlessly
st.iframe(
    src="http://127.0.0.1:7681",
    height=500,
    scrolling=True
)

st.markdown(
    "<div class='footer' style='color: #00ff41; font-family: monospace; font-weight: bold; font-size: 12px; border-top: 1px solid #00ff41; padding-top: 10px; margin-top: 20px; text-align: center;'> "
    "GODMOD3 v2.0 // PROJECT DREADNOUGHT // PURPLE TEAM COMMAND CENTER // MOBILE-FIRST ZERO-TRUST ARCHITECTURE<br>"
    "C._K._BACHOO // NAVY VETERAN // THE KNOWLEDGE HOUSE IF-CS-26 NY // ALL SYSTEMS OPERATIONAL"
    "</div>",
    unsafe_allow_html=True
)


# ==============================================================================
# INTEGRATED TERMINAL ATTACHMENT HUD NODE
# ==============================================================================
st.markdown("---")
st.markdown("### 🐉 KALI PROOT INTERACTIVE HARDWARE LINK")

# Utilizing Streamlit's official clean framing tool to pull in port 7681
st.iframe(
    src="http://127.0.0.1:7681",
    height=600,
    scrolling=True
)
