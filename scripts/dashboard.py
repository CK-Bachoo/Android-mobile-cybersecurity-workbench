from flask import Flask, request, jsonify
import subprocess
import threading
import os
from datetime import datetime

app = Flask(__name__)

# Security: Only allow safe commands
SAFE_COMMANDS = {
    'ping', 'traceroute', 'ip', 'ifconfig', 'route', 'netstat', 
    'ss', 'curl -I', 'whoami', 'uptime', 'df -h', 'free -h'
}

@app.route('/api/execute', methods=['POST'])
def execute_command():
    data = request.json
    command = data.get('command', '').strip()
    
    if not command:
        return jsonify({"output": "Error: No command provided"}), 400
    
    # Basic security check
    if not any(cmd in command.lower() for cmd in SAFE_COMMANDS):
        return jsonify({"output": "Command blocked for safety. Use: ping, ip, traceroute, etc."}), 403
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout + result.stderr
        return jsonify({
            "output": output.strip() or "Command executed (no output)",
            "timestamp": datetime.now().isoformat()
        })
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Command timed out (10s limit)"}), 408
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"}), 500

@app.route('/')
def index():
    return '''
    <html>
    <head><title>G0DM0D3 COCKPIT</title>
    <style>
        body { background:#0a0a0a; color:#00ff00; font-family:monospace; padding:20px; }
        .uplink { border:1px solid #00ff00; padding:15px; margin:20px 0; }
        input { background:#001100; color:#00ff00; border:1px solid #00ff00; padding:10px; width:70%; }
        button { background:#003300; color:#00ff00; border:1px solid #00ff00; padding:10px 20px; cursor:pointer; }
        #output { background:#000; border:1px solid #004400; padding:15px; height:250px; overflow:auto; white-space:pre-wrap; }
    </style>
    </head>
    <body>
        <h1>G0DM0D3 COCKPIT // LIVE</h1>
        
        <div class="uplink">
            <h2>COMMAND UPLINK</h2>
            <input type="text" id="cmd" placeholder="ping 8.8.8.8 or ip addr show">
            <button onclick="transmit()">TRANSMIT</button>
        </div>
        
        <div>
            <h2 style="color:#ffff00">COGNITIVE OUTPUT</h2>
            <div id="output">System online. Awaiting uplink...</div>
        </div>

        <script>
        function transmit() {
            const cmd = document.getElementById('cmd').value;
            if (!cmd) return;
            
            fetch('/api/execute', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({command: cmd})
            })
            .then(r => r.json())
            .then(data => {
                document.getElementById('output').innerHTML += 
                    '\\n> ' + cmd + '\\n' + data.output + '\\n';
                document.getElementById('cmd').value = '';
            });
        }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("[+] G0DM0D3 // Real command execution backend active on http://127.0.0.1:8080")
    app.run(host='127.0.0.1', port=8080, debug=False)
