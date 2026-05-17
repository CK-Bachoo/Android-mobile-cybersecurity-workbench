import React from "react";
import { trpc } from "./lib/trpc";

export default function App() {
  const health = trpc.system.health.useQuery();
  return (
    <div style={{ backgroundColor: "#030303", color: "#00ff66", height: "100vh", padding: "2rem", fontFamily: "monospace" }}>
      <h1>G0DM0D3 COCKPIT</h1>
      <p>System Status: {health.data?.status || "AWAITING CONNECTION..."}</p>
    </div>
  );
}
