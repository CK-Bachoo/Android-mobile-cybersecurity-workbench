import { useState } from 'react';
​function App() {
const [command, setCommand] = useState('');
const [output, setOutput] = useState('> System ready. Awaiting input...');
​const handleTransmit = () => {
if (!command) return;
setOutput(> Transmitting: ${command}\n> [WARNING]: Local AI Agent offline. Ordnance integration pending.);
setCommand('');
};
​return (
<div style={{ backgroundColor: '#0a0a0a', color: '#00ff00', minHeight: '100vh', padding: '20px', fontFamily: 'monospace' }}>
<h1 style={{ borderBottom: '1px solid #00ff00', paddingBottom: '10px' }}>G0DM0D3 COCKPIT</h1>
<p>System Status: <span style={{ color: '#00ff00', fontWeight: 'bold' }}>ONLINE</span></p>
​<div style={{ marginTop: '20px', border: '1px solid #004400', padding: '15px' }}>
<h2 style={{ margin: '0 0 10px 0' }}>Command Uplink</h2>
<div style={{ display: 'flex', gap: '10px' }}>
<input
type="text"
value={command}
onChange={(e) => setCommand(e.target.value)}
placeholder="Enter command or query..."
style={{ flex: 1, backgroundColor: '#001100', color: '#00ff00', border: '1px solid #00ff00', padding: '10px', outline: 'none' }}
/>
<button
onClick={handleTransmit}
style={{ backgroundColor: '#003300', color: '#00ff00', border: '1px solid #00ff00', padding: '10px 20px', cursor: 'pointer', fontWeight: 'bold' }}
>
TRANSMIT
</button>
</div>
</div>
​<div style={{ marginTop: '20px', border: '1px solid #004400', padding: '15px' }}>
<h2 style={{ margin: '0 0 10px 0', color: '#ffff00' }}>Cognitive Output</h2>
<div style={{ backgroundColor: '#000000', color: '#ffff00', padding: '15px', height: '200px', overflowY: 'auto', whiteSpace: 'pre-wrap', border: '1px solid #333' }}>
{output}
</div>
</div>
</div>
);
}
​export default App;
