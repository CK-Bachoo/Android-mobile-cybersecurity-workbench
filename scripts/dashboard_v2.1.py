#!/usr/bin/env python3
import http.server, socketserver, json, os
from pathlib import Path
from datetime import datetime

PORT = int(os.getenv("GODMOD3_PORT", "8080"))

class DreadnoughtHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

    def do_GET(self):
        routes = {"/": self._dashboard, "/index.html": self._dashboard, "/health": self._health, "/audit": self._audit}
        if self.path in routes:
            routes[self.path]()
        else:
            super().do_GET()

    def _json(self, data):
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _health(self):
        self._json({"status":"ONLINE","service":"GODMOD3","port":PORT,"time":datetime.now().isoformat()})

    def _audit(self):
        log = Path(__file__).parent.parent / "logs" / "audit_chain.jsonl"
        records = []
        if log.exists():
            for line in log.read_text().split("\n"):
                if line.strip():
                    try: records.append(json.loads(line))
                    except: pass
        self._json({"total": len(records), "latest": records[-10:]})

    def _dashboard(self):
        html = b"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>G0DM0D3 // DREADNOUGHT v5.0</title><style>*{box-sizing:border-box;margin:0;padding:0}body{background:#000;color:#00ff66;font-family:'Courier New',monospace;font-size:13px;padding:15px}.hdr{border:1px solid #00ff66;padding:15px;margin-bottom:12px;background:#050b07;text-align:center}.hdr h1{font-size:18px;letter-spacing:2px;margin-bottom:5px}.hdr p{color:#00cc55;font-size:11px;margin:2px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-bottom:12px}.panel{border:1px solid #00ff66;padding:12px;background:#020603}.panel h3{margin-bottom:8px;color:#00ff88;font-size:12px;letter-spacing:1px}.panel p{color:#00cc55;margin:3px 0;font-size:11px}.ok{color:#00ff66}.btn{display:block;background:#00ff66;color:#000;text-align:center;padding:10px;font-family:'Courier New',monospace;font-weight:bold;font-size:13px;text-decoration:none;border-radius:3px;margin:5px 0}.btn:hover{background:#00cc55}.cloud{border:1px solid #00ff66;padding:15px;background:#020603;text-align:center;margin-bottom:12px}.audit-box{border:1px solid #003311;padding:8px;background:#010401;font-size:10px;color:#009933;max-height:120px;overflow-y:auto;margin-top:8px}</style></head><body><div class="hdr"><h1>G0DM0D3 v2.0 // PROJECT DREADNOUGHT v5.0</h1><p>PURPLE TEAM SOC // ZERO-TRUST // ARM64 MOBILE</p><p>OPERATOR: C.K. BACHOO // NAVY VETERAN // NY IF-CS-26</p><p id="clk"></p></div><div class="grid"><div class="panel"><h3>INTELLIGENCE CORE</h3><p>GEMMA 2B LOCAL <span class="ok">[ACTIVE]</span></p><p>CLAUDE ARCHITECT <span class="ok">[ACTIVE]</span></p><p>SIMULATION CRITIC <span class="ok">[ARMED]</span></p><p>MERKLE CHAIN <span class="ok">[SEALED]</span></p><p>SOS 2-PUSH <span class="ok">[READY]</span></p><p>SAAS SENTINEL <span class="ok">[ARMED]</span></p></div><div class="panel"><h3>HARDWARE MATRIX</h3><p>PROC: EXYNOS 990 ARM64</p><p>RAM: 12GB LPDDR5</p><p>STORAGE: 256GB UFS + 512GB SD</p><p>OS: ANDROID + TERMUX NON-ROOT</p></div><div class="panel"><h3>SECURITY POSTURE</h3><p>SIEM <span class="ok">ONLINE :8080</span></p><p>HITL GATES <span class="ok">ENABLED</span></p><p>ZERO TRUST <span class="ok">ACTIVE</span></p><p>PROMPT INJECT <span class="ok">DEFENDED</span></p><p>BASH INJECT <span class="ok">PATCHED</span></p><p>THERMAL <span class="ok">5s/30s</span></p></div><div class="panel"><h3>GRC COMPLIANCE</h3><p>NIST CSF 2.0 <span class="ok">MAPPED</span></p><p>FEDRAMP HIGH <span class="ok">MAPPED</span></p><p>ISO 27001:2022 <span class="ok">MAPPED</span></p><p>CIS CONTROLS V8 <span class="ok">MAPPED</span></p></div></div><div class="cloud"><h3>CLOUD TERMINAL UPLINKS</h3><p style="color:#009933;font-size:11px;margin:6px 0">Cross-origin frames blocked. Use secure gateways.</p><a href="https://shell.cloud.google.com" target="_blank" class="btn">GCP CLOUD SHELL</a><a href="https://console.aws.amazon.com/cloudshell" target="_blank" class="btn">AWS CLOUDSHELL</a><a href="https://portal.azure.com" target="_blank" class="btn">AZURE TERMINAL</a></div><div class="panel"><h3>LIVE AUDIT CHAIN</h3><div class="audit-box" id="audit">Loading...</div></div><script>function clk(){document.getElementById('clk').textContent=new Date().toUTCString()}clk();setInterval(clk,5000);function loadAudit(){fetch('/audit').then(r=>r.json()).then(d=>{const b=document.getElementById('audit');if(!d.latest||!d.latest.length){b.textContent='No records. System pristine.';return;}b.innerHTML=d.latest.map(r=>'['+r.timestamp_iso+'] '+r.agent+' -> '+r.action+' | '+r.current_hash.substring(0,12)+'...').join('<br>');}).catch(()=>{document.getElementById('audit').textContent='Audit unavailable.';});}loadAudit();setInterval(loadAudit,30000);</script></body></html>"""
        self.send_response(200)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(html)))
        self.end_headers()
        self.wfile.write(html)

socketserver.TCPServer.allow_reuse_address = True
print(f"[✓] G0DM0D3 v2.0 -> http://127.0.0.1:{PORT}")
print(f"[✓] Health -> http://127.0.0.1:{PORT}/health")
print(f"[✓] Audit  -> http://127.0.0.1:{PORT}/audit")
print(f"[*] Thermal: clock=5s | audit=30s")
print("[*] Ctrl+C to stop")
with socketserver.TCPServer(("",PORT),DreadnoughtHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] G0DM0D3 shutdown clean.")
        httpd.server_close()
