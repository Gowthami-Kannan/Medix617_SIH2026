svg_routing_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="100%" height="100%" style="background-color: #0b0f19; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Drop Shadows -->
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <filter id="glow-purple" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#a855f7" flood-opacity="0.6"/>
    </filter>
    <filter id="glow-green" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#10b981" flood-opacity="0.6"/>
    </filter>

    <!-- Arrow Markers -->
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#c084fc"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>

  <!-- ================= HEADER ================= -->
  <g id="header">
    <rect x="40" y="25" width="920" height="70" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="500" y="55" text-anchor="middle" fill="#38bdf8" font-size="22" font-weight="700" letter-spacing="1.5">LORA MESH: ID-BASED DATA TRANSMISSION ROUTING</text>
    <text x="500" y="77" text-anchor="middle" fill="#94a3b8" font-size="13">Patient Node to Rescue Center via Automated Peer Hopping</text>
  </g>

  <!-- ================= MESH NETWORK LINKS ================= -->
  <!-- Patient to Relay 1 -->
  <path d="M 120 300 L 380 200" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="10,8" marker-end="url(#arrow-purple)"/>
  
  <!-- Relay 1 to Relay 2 -->
  <path d="M 380 200 L 640 380" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="10,8" marker-end="url(#arrow-purple)"/>
  
  <!-- Relay 2 to Destination -->
  <path d="M 640 380 L 880 260" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="10,8" marker-end="url(#arrow-green)"/>

  <!-- Packet visual markers on lines -->
  <rect x="230" y="235" width="40" height="24" rx="4" fill="#a855f7" transform="rotate(-22, 250, 247)"/>
  <text x="250" y="251" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" transform="rotate(-22, 250, 247)">DATA</text>

  <rect x="490" y="275" width="40" height="24" rx="4" fill="#a855f7" transform="rotate(35, 510, 287)"/>
  <text x="510" y="291" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" transform="rotate(35, 510, 287)">DATA</text>

  <rect x="740" y="305" width="40" height="24" rx="4" fill="#10b981" transform="rotate(-26, 760, 317)"/>
  <text x="760" y="321" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" transform="rotate(-26, 760, 317)">DATA</text>


  <!-- ================= NETWORK NODES ================= -->

  <!-- NODE 1: Patient Wearable (Originating) -->
  <g filter="url(#shadow)" transform="translate(120, 300)">
    <circle cx="0" cy="0" r="45" fill="#1e293b" stroke="#f43f5e" stroke-width="3"/>
    <circle cx="0" cy="0" r="35" fill="#f43f5e" opacity="0.2"/>
    <path d="M -12 -6 L -6 12 L 6 -12 L 12 6" fill="none" stroke="#f43f5e" stroke-width="2.5"/> 
    
    <rect x="-80" y="60" width="160" height="45" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="0" y="78" text-anchor="middle" fill="#fb7185" font-size="12" font-weight="700">Originating Node</text>
    <text x="0" y="94" text-anchor="middle" fill="#cbd5e1" font-size="10">Patient Wearable</text>
  </g>

  <!-- NODE 2: Relay Node 1 -->
  <g filter="url(#glow-purple)" transform="translate(380, 200)">
    <circle cx="0" cy="0" r="45" fill="#1e293b" stroke="#a855f7" stroke-width="3"/>
    <circle cx="0" cy="0" r="12" fill="#a855f7"/>
    <path d="M -22 -22 A 32 32 0 0 1 22 -22" fill="none" stroke="#a855f7" stroke-width="2.5"/>
    
    <rect x="-70" y="60" width="140" height="30" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="0" y="80" text-anchor="middle" fill="#d8b4fe" font-size="12" font-weight="700">Peer Node A</text>

    <!-- Logic Callout Box -->
    <g transform="translate(0, -90)">
      <rect x="-85" y="-35" width="170" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M -10 30 L 0 40 L 10 30 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="0" y="-15" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">if (Node_ID == Dest_ID)</text>
      <text x="0" y="5" text-anchor="middle" fill="#f59e0b" font-size="12" font-weight="700">FALSE</text>
      <text x="0" y="20" text-anchor="middle" fill="#94a3b8" font-size="10">Action: Auto-Hop Next</text>
    </g>
  </g>

  <!-- NODE 3: Relay Node 2 -->
  <g filter="url(#glow-purple)" transform="translate(640, 380)">
    <circle cx="0" cy="0" r="45" fill="#1e293b" stroke="#a855f7" stroke-width="3"/>
    <circle cx="0" cy="0" r="12" fill="#a855f7"/>
    <path d="M -22 -22 A 32 32 0 0 1 22 -22" fill="none" stroke="#a855f7" stroke-width="2.5"/>
    
    <rect x="-70" y="60" width="140" height="30" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="0" y="80" text-anchor="middle" fill="#d8b4fe" font-size="12" font-weight="700">Peer Node B</text>

    <!-- Logic Callout Box -->
    <g transform="translate(0, 105)">
      <rect x="-85" y="-30" width="170" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M -10 -30 L 0 -40 L 10 -30 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="0" y="-10" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">if (Node_ID == Dest_ID)</text>
      <text x="0" y="10" text-anchor="middle" fill="#f59e0b" font-size="12" font-weight="700">FALSE</text>
      <text x="0" y="25" text-anchor="middle" fill="#94a3b8" font-size="10">Action: Auto-Hop Next</text>
    </g>
  </g>

  <!-- NODE 4: Destination Sink (Hospital / Rescue) -->
  <g filter="url(#glow-green)" transform="translate(880, 260)">
    <circle cx="0" cy="0" r="55" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
    <circle cx="0" cy="0" r="42" fill="#10b981" opacity="0.2"/>
    <path d="M -12 -4 L -4 -4 L -4 -12 L 4 -12 L 4 -4 L 12 -4 L 12 4 L 4 4 L 4 12 L -4 12 L -4 4 L -12 4 Z" fill="#10b981"/> 
    
    <rect x="-85" y="70" width="170" height="45" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="0" y="88" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">Target Destination</text>
    <text x="0" y="104" text-anchor="middle" fill="#cbd5e1" font-size="10">Rescue Center / Hospital</text>

    <!-- Logic Callout Box -->
    <g transform="translate(0, -100)">
      <rect x="-85" y="-35" width="170" height="65" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <path d="M -10 30 L 0 40 L 10 30 Z" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="0" y="-15" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">if (Node_ID == Dest_ID)</text>
      <text x="0" y="5" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">TRUE (Match)</text>
      <text x="0" y="20" text-anchor="middle" fill="#94a3b8" font-size="10">Action: Receive Data &amp; Alert</text>
    </g>
  </g>


  <!-- ================= DETAILED EXPLANATION STEPS (Bottom) ================= -->
  <g transform="translate(40, 550)">
    
    <!-- Step 1 -->
    <g filter="url(#shadow)">
      <rect x="0" y="0" width="220" height="110" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
      <text x="110" y="25" text-anchor="middle" fill="#fb7185" font-size="13" font-weight="700">1. Origination</text>
      <text x="110" y="45" text-anchor="middle" fill="#f8fafc" font-size="11">Data originates from the</text>
      <text x="110" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">Patient Node. It creates a</text>
      <text x="110" y="75" text-anchor="middle" fill="#f8fafc" font-size="11">LoRa packet containing the</text>
      <text x="110" y="90" text-anchor="middle" fill="#f8fafc" font-size="11">Target Destination ID.</text>
    </g>

    <!-- Step 2 -->
    <g filter="url(#shadow)" transform="translate(233, 0)">
      <rect x="0" y="0" width="220" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="110" y="25" text-anchor="middle" fill="#c084fc" font-size="13" font-weight="700">2. Transmission</text>
      <text x="110" y="45" text-anchor="middle" fill="#f8fafc" font-size="11">The packet travels through</text>
      <text x="110" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">the airwaves to the nearest</text>
      <text x="110" y="75" text-anchor="middle" fill="#f8fafc" font-size="11">available peer nodes in the</text>
      <text x="110" y="90" text-anchor="middle" fill="#f8fafc" font-size="11">decentralized mesh network.</text>
    </g>

    <!-- Step 3 -->
    <g filter="url(#shadow)" transform="translate(466, 0)">
      <rect x="0" y="0" width="220" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="110" y="25" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700">3. ID Verification Hop</text>
      <text x="110" y="45" text-anchor="middle" fill="#f8fafc" font-size="11">The receiving node checks if</text>
      <text x="110" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">its Node ID = Destination ID.</text>
      <text x="110" y="75" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="600">If NOT equal,</text>
      <text x="110" y="90" text-anchor="middle" fill="#f8fafc" font-size="11">it automatically hops to next.</text>
    </g>

    <!-- Step 4 -->
    <g filter="url(#shadow)" transform="translate(700, 0)">
      <rect x="0" y="0" width="220" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="110" y="25" text-anchor="middle" fill="#34d399" font-size="13" font-weight="700">4. Target Reached</text>
      <text x="110" y="45" text-anchor="middle" fill="#f8fafc" font-size="11">When the ID finally matches,</text>
      <text x="110" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">the hopping stops. The</text>
      <text x="110" y="75" text-anchor="middle" fill="#f8fafc" font-size="11">Destination (Hospital/Rescue)</text>
      <text x="110" y="90" text-anchor="middle" fill="#f8fafc" font-size="11">processes the vital data alert.</text>
    </g>

  </g>
</svg>"""

with open("omnicare_lora_routing.svg", "w", encoding="utf-8") as f:
    f.write(svg_routing_content)
    
print("Successfully generated omnicare_lora_routing.svg")