#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8081

class DreadnoughtHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html_content = """<!DOCTYPE html>
            <html>
            <head>
                <title>GODMOD3 // CONSOLE</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { background-color: #000000; color: #00ff66; font-family: 'Courier New', monospace; margin: 20px; font-size: 13px; }
                    .header { border: 1px solid #00ff66; padding: 15px; margin-bottom: 15px; background: #050b07; }
                    .panel { border: 1px solid #00ff66; padding: 15px; margin-bottom: 15px; background: #0a0a0a; }
                    .btn { background-color: #00ff66; color: #000000; border: none; padding: 10px 20px; font-family: monospace; font-weight: bold; font-size: 14px; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; }
                    .btn:hover { background-color: #00cc55; }
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🚀 G0DM0D3 // PROJECT DREADNOUGHT // ARM64 MOBILE SOC</h1>
                    <h2>✅ WATCHDOG: RUNNING | HEARTBEAT: ACTIVE | ZERO-TRUST: ENFORCED</h2>
                </div>
                
                <div class="panel">
                    <h3>🔥 UPGRADED ARSENAL SLOTS</h3>
                    <ul>
                        <li><strong>[DEPLOYED]</strong> Debian Hazmat Tent (Frida & Objection)</li>
                        <li><strong>[STAGED]</strong> S32: Suricata IDS Tripwires</li>
                        <li><strong>[STAGED]</strong> S33: Sysmon Endpoint Cameras</li>
                    </ul>
                </div>

                <div class="panel">
                    <h3>☁️ GOOGLE CLOUD SHELL // TERMINAL UPLINK</h3>
                    <p>Cross-Origin frames are restricted by GCP security headers. Use the secure gateway below.</p>
                    <a href="https://shell.cloud.google.com" target="_blank" class="btn">🚀 LAUNCH CLOUD SHELL</a>
                </div>
                
                <div style='color: #00ff41; font-family: monospace; font-weight: bold; font-size: 12px; border-top: 1px solid #00ff41; padding-top: 10px; margin-top: 20px; text-align: center;'>
                    GODMOD3 v2.0 // PROJECT DREADNOUGHT // PURPLE TEAM COMMAND CENTER // MOBILE-FIRST ZERO-TRUST ARCHITECTURE<br>
                    C.K. BACHOO // NAVY VETERAN // THE KNOWLEDGE HOUSE IF-CS-26 NY // ALL SYSTEMS OPERATIONAL
                </div>
            </body>
            </html>"""
            
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), DreadnoughtHandler) as httpd:
    print(f"[🛡️ ONLINE] GODMOD3 Dashboard Core running natively on port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down workbench loop cleanly.")
        httpd.server_close()
