import os

COVERS = {
    # 1. SCR-001 Kraft FSC
    "scr_001_front.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="kraftGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#df9b42"/>
      <stop offset="50%" stop-color="#c67d26"/>
      <stop offset="100%" stop-color="#a66015"/>
    </linearGradient>
    <filter id="emboss" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#451a03" flood-opacity="0.4"/>
    </filter>
  </defs>
  <!-- Book Cover Base Slab -->
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#kraftGrad)" stroke="#78350f" stroke-width="6"/>
  <!-- Decorative Stitched Inset Border -->
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#78350f" stroke-width="3" stroke-dasharray="8 6"/>
  
  <!-- Brass Metal Corner Protectors -->
  <polygon points="15,15 90,15 15,90" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="585,15 510,15 585,90" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="15,585 90,585 15,510" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="585,585 510,585 585,510" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <circle cx="45" cy="45" r="4" fill="#713f12"/>
  <circle cx="555" cy="45" r="4" fill="#713f12"/>
  <circle cx="45" cy="555" r="4" fill="#713f12"/>
  <circle cx="555" cy="555" r="4" fill="#713f12"/>

  <!-- Left Ring Hole Markers -->
  <circle cx="35" cy="100" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="35" cy="200" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="35" cy="300" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="35" cy="400" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="35" cy="500" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>

  <!-- Center Title Plaque -->
  <g filter="url(#emboss)">
    <rect x="120" y="160" width="360" height="260" rx="16" fill="#fef3c7" stroke="#78350f" stroke-width="4"/>
    <rect x="135" y="175" width="330" height="230" rx="10" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="5 4"/>
    
    <text x="300" y="225" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="900" fill="#9a3412" letter-spacing="4" text-anchor="middle">✦ MEMOUR STUDIO ✦</text>
    <text x="300" y="295" font-family="'Patrick Hand', cursive, sans-serif" font-size="44" font-weight="bold" fill="#78350f" text-anchor="middle">Our Memories</text>
    <text x="300" y="340" font-family="'Playfair Display', serif" font-size="15" font-style="italic" fill="#b45309" text-anchor="middle">"Every memory has a story"</text>
    
    <!-- Botanical Motif -->
    <path d="M 270 375 Q 300 360 330 375 Q 300 390 270 375" fill="#ca8a04" opacity="0.8"/>
  </g>

  <!-- Bottom SKU Tag -->
  <rect x="210" y="470" width="180" height="34" rx="8" fill="#78350f"/>
  <text x="300" y="492" font-family="monospace" font-size="13" font-weight="bold" fill="#fef08a" text-anchor="middle">SCR-001 • KRAFT FSC</text>
</svg>""",

    "scr_001_back.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="kraftGradBack" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#df9b42"/>
      <stop offset="50%" stop-color="#c67d26"/>
      <stop offset="100%" stop-color="#a66015"/>
    </linearGradient>
  </defs>
  <!-- Book Cover Base Slab -->
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#kraftGradBack)" stroke="#78350f" stroke-width="6"/>
  <!-- Decorative Stitched Inset Border -->
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#78350f" stroke-width="3" stroke-dasharray="8 6"/>
  
  <!-- Brass Metal Corner Protectors -->
  <polygon points="15,15 90,15 15,90" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="585,15 510,15 585,90" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="15,585 90,585 15,510" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>
  <polygon points="585,585 510,585 585,510" fill="#ca8a04" stroke="#713f12" stroke-width="3"/>

  <!-- Right Ring Hole Markers (Back Cover perspective) -->
  <circle cx="565" cy="100" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="565" cy="200" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="565" cy="300" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="565" cy="400" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="565" cy="500" r="10" fill="#451a03" stroke="#ca8a04" stroke-width="3"/>

  <!-- Center Minimalist Craft Seal -->
  <g transform="translate(300, 270)">
    <circle cx="0" cy="0" r="90" fill="#78350f" stroke="#ca8a04" stroke-width="4"/>
    <circle cx="0" cy="0" r="76" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 3"/>
    
    <text x="0" y="-35" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="900" fill="#fef08a" letter-spacing="3" text-anchor="middle">MEMOUR</text>
    <text x="0" y="-10" font-family="'Patrick Hand', cursive, sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">✦ 2026 ✦</text>
    <text x="0" y="20" font-family="sans-serif" font-size="9" font-weight="bold" fill="#fef08a" letter-spacing="1" text-anchor="middle">EVERY MEMORY</text>
    <text x="0" y="36" font-family="sans-serif" font-size="9" font-weight="bold" fill="#fef08a" letter-spacing="1" text-anchor="middle">HAS A STORY</text>
  </g>

  <!-- Bottom Barcode & FSC Guarantee -->
  <g transform="translate(180, 440)">
    <rect x="0" y="0" width="240" height="75" rx="8" fill="#fef3c7" stroke="#78350f" stroke-width="2"/>
    <!-- Barcode lines -->
    <rect x="25" y="12" width="4" height="36" fill="#1c1917"/>
    <rect x="33" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="39" y="12" width="6" height="36" fill="#1c1917"/>
    <rect x="49" y="12" width="3" height="36" fill="#1c1917"/>
    <rect x="56" y="12" width="5" height="36" fill="#1c1917"/>
    <rect x="65" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="71" y="12" width="4" height="36" fill="#1c1917"/>
    <rect x="79" y="12" width="6" height="36" fill="#1c1917"/>
    <rect x="89" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="95" y="12" width="5" height="36" fill="#1c1917"/>
    
    <text x="60" y="60" font-family="monospace" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">8 938500 001014</text>
    <text x="175" y="32" font-family="sans-serif" font-size="11" font-weight="black" fill="#15803d" text-anchor="middle">100% FSC</text>
    <text x="175" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#78350f" text-anchor="middle">Acid-Free Paper</text>
  </g>
</svg>""",

    # 2. SCR-002 Pastel Hologram
    "scr_002_front.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="pastelHolo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbcfe8"/>
      <stop offset="35%" stop-color="#e9d5ff"/>
      <stop offset="70%" stop-color="#c7d2fe"/>
      <stop offset="100%" stop-color="#a7f3d0"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#pastelHolo)" stroke="#db2777" stroke-width="5"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#ffffff" stroke-width="4"/>
  
  <!-- Silver Corners -->
  <polygon points="15,15 85,15 15,85" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="585,15 515,15 585,85" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="15,585 85,585 15,515" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="585,585 515,585 585,515" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>

  <!-- Left Ring Holes -->
  <circle cx="35" cy="100" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="35" cy="200" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="35" cy="300" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="35" cy="400" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="35" cy="500" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>

  <!-- Center Card -->
  <rect x="120" y="160" width="360" height="260" rx="20" fill="#ffffff" opacity="0.95" stroke="#ec4899" stroke-width="4"/>
  <text x="300" y="225" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="900" fill="#db2777" letter-spacing="4" text-anchor="middle">✦ MEMOUR STUDIO ✦</text>
  <text x="300" y="295" font-family="'Patrick Hand', cursive, sans-serif" font-size="44" font-weight="bold" fill="#831843" text-anchor="middle">Sweet Moments</text>
  <text x="300" y="340" font-family="'Playfair Display', serif" font-size="15" font-style="italic" fill="#db2777" text-anchor="middle">"Every memory has a story"</text>
  
  <rect x="200" y="470" width="200" height="34" rx="8" fill="#db2777"/>
  <text x="300" y="492" font-family="monospace" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SCR-002 • PASTEL HOLO</text>
</svg>""",

    "scr_002_back.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="pastelHoloBack" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbcfe8"/>
      <stop offset="35%" stop-color="#e9d5ff"/>
      <stop offset="70%" stop-color="#c7d2fe"/>
      <stop offset="100%" stop-color="#a7f3d0"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#pastelHoloBack)" stroke="#db2777" stroke-width="5"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#ffffff" stroke-width="4"/>
  
  <!-- Silver Corners -->
  <polygon points="15,15 85,15 15,85" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="585,15 515,15 585,85" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="15,585 85,585 15,515" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="585,585 515,585 585,515" fill="#f1f5f9" stroke="#94a3b8" stroke-width="3"/>

  <!-- Right Ring Holes (Back Cover) -->
  <circle cx="565" cy="100" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="565" cy="200" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="565" cy="300" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="565" cy="400" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>
  <circle cx="565" cy="500" r="10" fill="#334155" stroke="#f1f5f9" stroke-width="3"/>

  <!-- Center Hologram Seal -->
  <g transform="translate(300, 270)">
    <circle cx="0" cy="0" r="90" fill="#ffffff" stroke="#db2777" stroke-width="4"/>
    <circle cx="0" cy="0" r="76" fill="none" stroke="#ec4899" stroke-width="2" stroke-dasharray="4 3"/>
    
    <text x="0" y="-35" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="900" fill="#db2777" letter-spacing="3" text-anchor="middle">MEMOUR</text>
    <text x="0" y="-10" font-family="'Patrick Hand', cursive, sans-serif" font-size="28" font-weight="bold" fill="#831843" text-anchor="middle">💖 Y2K 💖</text>
    <text x="0" y="20" font-family="sans-serif" font-size="9" font-weight="bold" fill="#db2777" letter-spacing="1" text-anchor="middle">EVERY MEMORY</text>
    <text x="0" y="36" font-family="sans-serif" font-size="9" font-weight="bold" fill="#db2777" letter-spacing="1" text-anchor="middle">HAS A STORY</text>
  </g>

  <!-- Bottom Barcode -->
  <g transform="translate(180, 440)">
    <rect x="0" y="0" width="240" height="75" rx="8" fill="#ffffff" stroke="#db2777" stroke-width="2"/>
    <rect x="25" y="12" width="4" height="36" fill="#1c1917"/>
    <rect x="33" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="39" y="12" width="6" height="36" fill="#1c1917"/>
    <rect x="49" y="12" width="3" height="36" fill="#1c1917"/>
    <rect x="56" y="12" width="5" height="36" fill="#1c1917"/>
    <rect x="65" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="71" y="12" width="4" height="36" fill="#1c1917"/>
    <rect x="79" y="12" width="6" height="36" fill="#1c1917"/>
    <rect x="89" y="12" width="2" height="36" fill="#1c1917"/>
    <rect x="95" y="12" width="5" height="36" fill="#1c1917"/>
    
    <text x="60" y="60" font-family="monospace" font-size="10" font-weight="bold" fill="#831843" text-anchor="middle">8 938500 002028</text>
    <text x="175" y="32" font-family="sans-serif" font-size="11" font-weight="black" fill="#db2777" text-anchor="middle">100% FSC</text>
    <text x="175" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#831843" text-anchor="middle">Hologram Edition</text>
  </g>
</svg>""",

    # 3. SCR-003 Velvet Black
    "scr_003_front.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <rect x="15" y="15" width="570" height="570" rx="18" fill="#18181b" stroke="#3f3f46" stroke-width="5"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 4"/>
  
  <!-- Gunmetal / Gold Rivets -->
  <polygon points="15,15 85,15 15,85" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="585,15 515,15 585,85" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="15,585 85,585 15,515" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="585,585 515,585 585,515" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>

  <!-- Left Ring Holes -->
  <circle cx="35" cy="100" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="35" cy="200" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="35" cy="300" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="35" cy="400" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="35" cy="500" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>

  <!-- Center Gold Plaque -->
  <rect x="120" y="160" width="360" height="260" rx="16" fill="#27272a" stroke="#fbbf24" stroke-width="3"/>
  <text x="300" y="225" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="900" fill="#fbbf24" letter-spacing="4" text-anchor="middle">✦ MEMOUR STUDIO ✦</text>
  <text x="300" y="295" font-family="'Playfair Display', serif" font-size="40" font-weight="bold" fill="#fef08a" text-anchor="middle">Timeless Stories</text>
  <text x="300" y="340" font-family="'Patrick Hand', cursive" font-size="18" fill="#a1a1aa" text-anchor="middle">"Every memory has a story"</text>
  
  <rect x="210" y="470" width="180" height="34" rx="8" fill="#fbbf24"/>
  <text x="300" y="492" font-family="monospace" font-size="13" font-weight="bold" fill="#18181b" text-anchor="middle">SCR-003 • VELVET DARK</text>
</svg>""",

    "scr_003_back.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <rect x="15" y="15" width="570" height="570" rx="18" fill="#18181b" stroke="#3f3f46" stroke-width="5"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 4"/>
  
  <!-- Gunmetal Corners -->
  <polygon points="15,15 85,15 15,85" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="585,15 515,15 585,85" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="15,585 85,585 15,515" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>
  <polygon points="585,585 515,585 585,515" fill="#3f3f46" stroke="#fbbf24" stroke-width="2"/>

  <!-- Right Ring Holes (Back Cover) -->
  <circle cx="565" cy="100" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="565" cy="200" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="565" cy="300" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="565" cy="400" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>
  <circle cx="565" cy="500" r="10" fill="#09090b" stroke="#71717a" stroke-width="3"/>

  <!-- Center Gold Seal -->
  <g transform="translate(300, 270)">
    <circle cx="0" cy="0" r="90" fill="#27272a" stroke="#fbbf24" stroke-width="4"/>
    <circle cx="0" cy="0" r="76" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 3"/>
    
    <text x="0" y="-35" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="900" fill="#fbbf24" letter-spacing="3" text-anchor="middle">MEMOUR</text>
    <text x="0" y="-10" font-family="'Playfair Display', serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">NOIR</text>
    <text x="0" y="20" font-family="sans-serif" font-size="9" font-weight="bold" fill="#fbbf24" letter-spacing="1" text-anchor="middle">EVERY MEMORY</text>
    <text x="0" y="36" font-family="sans-serif" font-size="9" font-weight="bold" fill="#fbbf24" letter-spacing="1" text-anchor="middle">HAS A STORY</text>
  </g>

  <!-- Bottom Barcode -->
  <g transform="translate(180, 440)">
    <rect x="0" y="0" width="240" height="75" rx="8" fill="#27272a" stroke="#fbbf24" stroke-width="2"/>
    <rect x="25" y="12" width="4" height="36" fill="#fbbf24"/>
    <rect x="33" y="12" width="2" height="36" fill="#fbbf24"/>
    <rect x="39" y="12" width="6" height="36" fill="#fbbf24"/>
    <rect x="49" y="12" width="3" height="36" fill="#fbbf24"/>
    <rect x="56" y="12" width="5" height="36" fill="#fbbf24"/>
    <rect x="65" y="12" width="2" height="36" fill="#fbbf24"/>
    <rect x="71" y="12" width="4" height="36" fill="#fbbf24"/>
    <rect x="79" y="12" width="6" height="36" fill="#fbbf24"/>
    <rect x="89" y="12" width="2" height="36" fill="#fbbf24"/>
    <rect x="95" y="12" width="5" height="36" fill="#fbbf24"/>
    
    <text x="60" y="60" font-family="monospace" font-size="10" font-weight="bold" fill="#fef08a" text-anchor="middle">8 938500 003032</text>
    <text x="175" y="32" font-family="sans-serif" font-size="11" font-weight="black" fill="#fbbf24" text-anchor="middle">100% FSC</text>
    <text x="175" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#a1a1aa" text-anchor="middle">Dark Edition</text>
  </g>
</svg>""",

    # 4. SCR-004 Vintage Linen
    "scr_004_front.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="linenGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="50%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#linenGrad)" stroke="#064e3b" stroke-width="6"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#d1fae5" stroke-width="3" stroke-dasharray="8 6"/>
  
  <!-- Bronze Corners -->
  <polygon points="15,15 90,15 15,90" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="585,15 510,15 585,90" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="15,585 90,585 15,510" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="585,585 510,585 585,510" fill="#b45309" stroke="#78350f" stroke-width="3"/>

  <!-- Left Ring Holes -->
  <circle cx="35" cy="100" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="35" cy="200" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="35" cy="300" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="35" cy="400" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="35" cy="500" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>

  <!-- Center Plaque -->
  <rect x="120" y="160" width="360" height="260" rx="16" fill="#ecfdf5" stroke="#047857" stroke-width="4"/>
  <text x="300" y="225" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="900" fill="#047857" letter-spacing="4" text-anchor="middle">✦ MEMOUR STUDIO ✦</text>
  <text x="300" y="295" font-family="'Patrick Hand', cursive, sans-serif" font-size="44" font-weight="bold" fill="#064e3b" text-anchor="middle">Botanical Journal</text>
  <text x="300" y="340" font-family="'Playfair Display', serif" font-size="15" font-style="italic" fill="#047857" text-anchor="middle">"Every memory has a story"</text>
  
  <rect x="210" y="470" width="180" height="34" rx="8" fill="#064e3b"/>
  <text x="300" y="492" font-family="monospace" font-size="13" font-weight="bold" fill="#d1fae5" text-anchor="middle">SCR-004 • BOTANICAL</text>
</svg>""",

    "scr_004_back.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="linenGradBack" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="50%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="570" height="570" rx="18" fill="url(#linenGradBack)" stroke="#064e3b" stroke-width="6"/>
  <rect x="35" y="35" width="530" height="530" rx="12" fill="none" stroke="#d1fae5" stroke-width="3" stroke-dasharray="8 6"/>
  
  <!-- Bronze Corners -->
  <polygon points="15,15 90,15 15,90" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="585,15 510,15 585,90" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="15,585 90,585 15,510" fill="#b45309" stroke="#78350f" stroke-width="3"/>
  <polygon points="585,585 510,585 585,510" fill="#b45309" stroke="#78350f" stroke-width="3"/>

  <!-- Right Ring Holes (Back Cover) -->
  <circle cx="565" cy="100" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="565" cy="200" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="565" cy="300" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="565" cy="400" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>
  <circle cx="565" cy="500" r="10" fill="#022c22" stroke="#b45309" stroke-width="3"/>

  <!-- Center Botanical Seal -->
  <g transform="translate(300, 270)">
    <circle cx="0" cy="0" r="90" fill="#064e3b" stroke="#b45309" stroke-width="4"/>
    <circle cx="0" cy="0" r="76" fill="none" stroke="#d1fae5" stroke-width="2" stroke-dasharray="4 3"/>
    
    <text x="0" y="-35" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="900" fill="#d1fae5" letter-spacing="3" text-anchor="middle">MEMOUR</text>
    <text x="0" y="-10" font-family="'Patrick Hand', cursive, sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">🌿 HERBARIUM 🌿</text>
    <text x="0" y="20" font-family="sans-serif" font-size="9" font-weight="bold" fill="#d1fae5" letter-spacing="1" text-anchor="middle">EVERY MEMORY</text>
    <text x="0" y="36" font-family="sans-serif" font-size="9" font-weight="bold" fill="#d1fae5" letter-spacing="1" text-anchor="middle">HAS A STORY</text>
  </g>

  <!-- Bottom Barcode -->
  <g transform="translate(180, 440)">
    <rect x="0" y="0" width="240" height="75" rx="8" fill="#ecfdf5" stroke="#047857" stroke-width="2"/>
    <rect x="25" y="12" width="4" height="36" fill="#064e3b"/>
    <rect x="33" y="12" width="2" height="36" fill="#064e3b"/>
    <rect x="39" y="12" width="6" height="36" fill="#064e3b"/>
    <rect x="49" y="12" width="3" height="36" fill="#064e3b"/>
    <rect x="56" y="12" width="5" height="36" fill="#064e3b"/>
    <rect x="65" y="12" width="2" height="36" fill="#064e3b"/>
    <rect x="71" y="12" width="4" height="36" fill="#064e3b"/>
    <rect x="79" y="12" width="6" height="36" fill="#064e3b"/>
    <rect x="89" y="12" width="2" height="36" fill="#064e3b"/>
    <rect x="95" y="12" width="5" height="36" fill="#064e3b"/>
    
    <text x="60" y="60" font-family="monospace" font-size="10" font-weight="bold" fill="#064e3b" text-anchor="middle">8 938500 004049</text>
    <text x="175" y="32" font-family="sans-serif" font-size="11" font-weight="black" fill="#047857" text-anchor="middle">100% FSC</text>
    <text x="175" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#064e3b" text-anchor="middle">Nature Edition</text>
  </g>
</svg>"""
}

target_dir = os.path.join("static", "assets", "books")
os.makedirs(target_dir, exist_ok=True)

for fname, content in COVERS.items():
    fpath = os.path.join(target_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {fpath}")

# Also update the base scr_001.svg .. scr_004.svg to match the front cover
for i in range(1, 5):
    front_key = f"scr_00{i}_front.svg"
    base_key = f"scr_00{i}.svg"
    if front_key in COVERS:
        fpath = os.path.join(target_dir, base_key)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(COVERS[front_key].strip())
        print(f"Updated base cover: {fpath}")
