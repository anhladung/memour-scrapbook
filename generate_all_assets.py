import os

stickers = {
  'stk_y2k_stars.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300">
  <defs>
    <linearGradient id="holoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff9a9e" />
      <stop offset="25%" stop-color="#fecfef" />
      <stop offset="50%" stop-color="#a1c4fd" />
      <stop offset="75%" stop-color="#c2e9fb" />
      <stop offset="100%" stop-color="#e0c3fc" />
    </linearGradient>
    <filter id="glow3d" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="3" dy="5" stdDeviation="4" flood-color="#8b5cf6" flood-opacity="0.45"/>
    </filter>
  </defs>
  <g filter="url(#glow3d)">
    <path d="M150 20 Q150 150 20 150 Q150 150 150 280 Q150 150 280 150 Q150 150 150 20 Z" fill="url(#holoGrad)" stroke="#ffffff" stroke-width="5" />
    <path d="M150 65 Q150 150 65 150 Q150 150 150 235 Q150 150 235 150 Q150 150 150 65 Z" fill="#ffffff" opacity="0.85" />
    <path d="M235 45 Q235 70 210 70 Q235 70 235 95 Q235 70 260 70 Q235 70 235 45 Z" fill="url(#holoGrad)" stroke="#ffffff" stroke-width="2.5" />
    <path d="M65 215 Q65 235 45 235 Q65 235 65 255 Q65 235 85 235 Q65 235 65 215 Z" fill="url(#holoGrad)" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="230" cy="220" r="10" fill="#ffffff" stroke="#e0c3fc" stroke-width="2" />
    <circle cx="70" cy="80" r="8" fill="#ffffff" stroke="#e0c3fc" stroke-width="2" />
  </g>
</svg>''',

  'stk_vintage_flower.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300">
  <defs>
    <filter id="paperShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="3" flood-color="#78350f" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#paperShadow)">
    <rect x="25" y="25" width="250" height="250" rx="20" fill="#fef3c7" stroke="#b45309" stroke-width="3.5" stroke-dasharray="8 5" />
    <path d="M150 240 Q140 150 120 70" stroke="#4d7c0f" stroke-width="5" fill="none" stroke-linecap="round" />
    <path d="M138 180 Q95 160 85 135 Q120 145 135 175" fill="#65a30d" opacity="0.9" />
    <path d="M130 130 Q175 110 185 85 Q150 105 128 128" fill="#65a30d" opacity="0.9" />
    <g transform="translate(120, 70)">
      <circle cx="0" cy="-22" r="16" fill="#f59e0b" opacity="0.9" />
      <circle cx="20" cy="-11" r="16" fill="#d97706" opacity="0.9" />
      <circle cx="20" cy="11" r="16" fill="#f59e0b" opacity="0.9" />
      <circle cx="0" cy="22" r="16" fill="#b45309" opacity="0.9" />
      <circle cx="-20" cy="11" r="16" fill="#f59e0b" opacity="0.9" />
      <circle cx="-20" cy="-11" r="16" fill="#d97706" opacity="0.9" />
      <circle cx="0" cy="0" r="12" fill="#78350f" stroke="#fef3c7" stroke-width="2" />
    </g>
    <text x="150" y="255" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle" letter-spacing="3">BOTANICAL CRAFT</text>
  </g>
</svg>''',

  'stk_genz_doodle.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300">
  <defs>
    <filter id="neoShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="5" dy="5" stdDeviation="0" flood-color="#000000" flood-opacity="1"/>
    </filter>
  </defs>
  <g filter="url(#neoShadow)">
    <rect x="25" y="45" width="250" height="210" rx="28" fill="#fde047" stroke="#000000" stroke-width="5" />
    <path d="M150 105 C150 75, 110 75, 110 105 C110 135, 150 165, 150 165 C150 165, 190 135, 190 105 C190 75, 150 75, 150 105 Z" fill="#e11d48" stroke="#000000" stroke-width="4" />
    <rect x="123" y="94" width="24" height="15" rx="4" fill="#000000" />
    <rect x="153" y="94" width="24" height="15" rx="4" fill="#000000" />
    <line x1="147" y1="101" x2="153" y2="101" stroke="#000000" stroke-width="4" />
    <text x="150" y="215" font-family="Impact, sans-serif" font-size="30" fill="#000000" text-anchor="middle" letter-spacing="2">SLAY VIBES</text>
    <polygon points="50,70 72,70 60,92 82,92 48,135 58,102 42,102" fill="#fbbf24" stroke="#000000" stroke-width="2.5" />
    <circle cx="235" cy="85" r="14" fill="#38bdf8" stroke="#000000" stroke-width="3" />
    <text x="235" y="90" font-family="sans-serif" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">100</text>
  </g>
</svg>''',

  'stk_washi_tape.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="120" viewBox="0 0 300 120">
  <defs>
    <pattern id="pastelGrid" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="16" height="16" fill="#f3e8ff"/>
      <path d="M 16 0 L 0 0 0 16" fill="none" stroke="#c084fc" stroke-width="1.8" opacity="0.7"/>
    </pattern>
    <filter id="tapeShadow">
      <feDropShadow dx="2" dy="3" stdDeviation="2" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <g filter="url(#tapeShadow)">
    <path d="M 10 25 L 18 18 L 26 25 L 275 20 L 282 27 L 290 20 L 285 85 L 290 92 L 280 85 L 15 90 L 10 82 Z" fill="url(#pastelGrid)" stroke="#a855f7" stroke-width="1.5" />
    <text x="150" y="60" font-family="monospace" font-size="14" font-weight="bold" fill="#6b21a8" text-anchor="middle" letter-spacing="4">✦ MEMORY LANE ✦</text>
  </g>
</svg>''',

  'stk_retro_cassette.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#eab308" />
      <stop offset="100%" stop-color="#854d0e" />
    </linearGradient>
    <filter id="goldShine">
      <feDropShadow dx="3" dy="5" stdDeviation="3" flood-color="#713f12" flood-opacity="0.45"/>
    </filter>
  </defs>
  <g filter="url(#goldShine)">
    <rect x="25" y="25" width="250" height="150" rx="14" fill="#0f172a" stroke="url(#goldGrad)" stroke-width="5" />
    <rect x="45" y="45" width="210" height="110" rx="8" fill="url(#goldGrad)" stroke="#0f172a" stroke-width="2.5" />
    <rect x="75" y="75" width="150" height="50" rx="8" fill="#0f172a" />
    <circle cx="110" cy="100" r="16" fill="#ffffff" stroke="#475569" stroke-width="3" />
    <circle cx="110" cy="100" r="6" fill="#0f172a" />
    <circle cx="190" cy="100" r="16" fill="#ffffff" stroke="#475569" stroke-width="3" />
    <circle cx="190" cy="100" r="6" fill="#0f172a" />
    <rect x="130" y="92" width="40" height="16" rx="3" fill="#334155" />
    <text x="150" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#451a03" text-anchor="middle">SIDE A: OUR 90S PLAYLIST</text>
  </g>
</svg>''',

  'stk_sparkle_heart.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300">
  <defs>
    <linearGradient id="silverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="35%" stop-color="#fbcfe8" />
      <stop offset="70%" stop-color="#e2e8f0" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
    <filter id="heartGlow">
      <feDropShadow dx="3" dy="5" stdDeviation="4" flood-color="#e11d48" flood-opacity="0.35"/>
    </filter>
  </defs>
  <g filter="url(#heartGlow)">
    <path d="M 150 85 C 130 25, 35 35, 35 120 C 35 185, 150 260, 150 260 C 150 260, 265 185, 265 120 C 265 35, 170 25, 150 85 Z" fill="url(#silverGrad)" stroke="#ffffff" stroke-width="5" />
    <path d="M 150 115 C 135 75, 75 80, 75 130 C 75 170, 150 220, 150 220 C 150 220, 225 170, 225 130 C 225 80, 165 75, 150 115 Z" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-dasharray="5 4" />
    <path d="M150 135 Q150 160 125 160 Q150 160 150 185 Q150 160 175 160 Q150 160 150 135 Z" fill="#ffffff" />
    <circle cx="85" cy="105" r="7" fill="#ffffff" />
    <circle cx="215" cy="105" r="7" fill="#ffffff" />
  </g>
</svg>'''
}

layouts = {
  'lay_polaroid_single.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="380" viewBox="0 0 320 380">
  <defs>
    <filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <g filter="url(#cardShadow)">
    <rect x="15" y="15" width="290" height="350" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="3"/>
    <!-- Photo Area -->
    <rect x="35" y="35" width="250" height="250" rx="4" fill="#cbd5e1"/>
    <circle cx="160" cy="140" r="35" fill="#94a3b8"/>
    <path d="M60 250 L120 180 L180 250 Z" fill="#64748b"/>
    <path d="M150 250 L210 195 L270 250 Z" fill="#475569"/>
    <!-- Corner mounting tabs -->
    <polygon points="25,25 55,25 25,55" fill="#d97706" opacity="0.9"/>
    <polygon points="295,25 265,25 295,55" fill="#d97706" opacity="0.9"/>
    <polygon points="25,295 55,295 25,265" fill="#d97706" opacity="0.9"/>
    <polygon points="295,295 265,295 295,265" fill="#d97706" opacity="0.9"/>
    <!-- Handwritten caption area -->
    <line x1="45" y1="320" x2="275" y2="320" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="160" y="340" font-family="'Patrick Hand', cursive, sans-serif" font-size="18" fill="#475569" text-anchor="middle">Khoanh Khac Dang Nho</text>
  </g>
</svg>''',

  'lay_filmstrip_triple.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="180" viewBox="0 0 420 180">
  <defs>
    <filter id="filmShadow">
      <feDropShadow dx="3" dy="5" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#filmShadow)">
    <rect x="10" y="10" width="400" height="160" rx="8" fill="#18181b" stroke="#27272a" stroke-width="3"/>
    <!-- Sprocket holes top & bottom -->
    ''' + ''.join([f'<rect x="{25 + i*32}" y="18" width="16" height="12" rx="3" fill="#ffffff"/>' for i in range(12)]) + '''
    ''' + ''.join([f'<rect x="{25 + i*32}" y="150" width="16" height="12" rx="3" fill="#ffffff"/>' for i in range(12)]) + '''
    <rect x="30" y="40" width="105" height="100" rx="4" fill="#3f3f46"/>
    <text x="82" y="95" font-family="sans-serif" font-size="12" font-weight="bold" fill="#a1a1aa" text-anchor="middle">FRAME #01</text>
    <rect x="155" y="40" width="105" height="100" rx="4" fill="#3f3f46"/>
    <text x="207" y="95" font-family="sans-serif" font-size="12" font-weight="bold" fill="#a1a1aa" text-anchor="middle">FRAME #02</text>
    <rect x="280" y="40" width="105" height="100" rx="4" fill="#3f3f46"/>
    <text x="332" y="95" font-family="sans-serif" font-size="12" font-weight="bold" fill="#a1a1aa" text-anchor="middle">FRAME #03</text>
  </g>
</svg>''',

  'lay_accordion_fold.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="300" viewBox="0 0 380 300">
  <defs>
    <filter id="accShadow">
      <feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <g filter="url(#accShadow)">
    <rect x="20" y="20" width="340" height="260" rx="14" fill="#fdf4ff" stroke="#f472b6" stroke-width="3"/>
    <path d="M 40 45 L 120 35 L 120 245 L 40 255 Z" fill="#fae8ff" stroke="#e879f9" stroke-width="2"/>
    <path d="M 120 35 L 200 45 L 200 255 L 120 245 Z" fill="#fdf4ff" stroke="#e879f9" stroke-width="2"/>
    <path d="M 200 45 L 280 35 L 280 245 L 200 255 Z" fill="#fae8ff" stroke="#e879f9" stroke-width="2"/>
    <path d="M 280 35 L 340 45 L 340 255 L 280 245 Z" fill="#fdf4ff" stroke="#e879f9" stroke-width="2"/>
    <circle cx="190" cy="40" r="14" fill="#881337"/>
    <path d="M 190 40 Q 140 10 160 40 Q 190 40 190 40" fill="#9f1239" stroke="#881337" stroke-width="2"/>
    <path d="M 190 40 Q 240 10 220 40 Q 190 40 190 40" fill="#9f1239" stroke="#881337" stroke-width="2"/>
    <text x="190" y="150" font-family="sans-serif" font-size="16" font-weight="bold" fill="#78350f" text-anchor="middle">ACCORDION 3D FOLD</text>
    <text x="190" y="180" font-family="sans-serif" font-size="12" fill="#92400e" text-anchor="middle">Mo rong chua 8 anh ky niem</text>
  </g>
</svg>''',

  'lay_secret_pocket.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="280" viewBox="0 0 320 280">
  <defs>
    <filter id="pockShadow">
      <feDropShadow dx="3" dy="5" stdDeviation="3" flood-color="#78350f" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#pockShadow)">
    <rect x="20" y="20" width="280" height="240" rx="12" fill="#d97706" stroke="#78350f" stroke-width="4"/>
    <rect x="50" y="35" width="80" height="90" rx="6" fill="#fef3c7" stroke="#b45309" stroke-width="2" transform="rotate(-10 50 35)"/>
    <rect x="170" y="35" width="80" height="90" rx="6" fill="#fef3c7" stroke="#b45309" stroke-width="2" transform="rotate(8 170 35)"/>
    <path d="M 20 100 L 160 170 L 300 100 L 300 260 L 20 260 Z" fill="#b45309" stroke="#78350f" stroke-width="3"/>
    <circle cx="160" cy="180" r="16" fill="#fef3c7" stroke="#78350f" stroke-width="3"/>
    <circle cx="160" cy="180" r="4" fill="#78350f"/>
    <text x="160" y="235" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fef3c7" text-anchor="middle" letter-spacing="2">SECRET MEMORY TAG</text>
  </g>
</svg>''',

  'lay_mosaic_collage.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="300" viewBox="0 0 350 300">
  <defs>
    <filter id="mosShadow">
      <feDropShadow dx="3" dy="4" stdDeviation="3" flood-color="#000" flood-opacity="0.15"/>
    </filter>
  </defs>
  <g filter="url(#mosShadow)">
    <rect x="15" y="15" width="320" height="270" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="3"/>
    <rect x="30" y="30" width="135" height="135" rx="8" fill="#fed7aa" stroke="#fb923c" stroke-width="2"/>
    <text x="97" y="102" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ea580c" text-anchor="middle">MAIN PHOTO</text>
    <rect x="180" y="30" width="135" height="60" rx="8" fill="#e9d5ff" stroke="#c084fc" stroke-width="2"/>
    <text x="247" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7e22ce" text-anchor="middle">MOMENT 1</text>
    <rect x="180" y="105" width="135" height="60" rx="8" fill="#bbf7d0" stroke="#4ade80" stroke-width="2"/>
    <text x="247" y="140" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">MOMENT 2</text>
    <rect x="30" y="180" width="285" height="85" rx="8" fill="#fef08a" stroke="#facc15" stroke-width="2"/>
    <text x="172" y="228" font-family="sans-serif" font-size="13" font-weight="bold" fill="#854d0e" text-anchor="middle">PANORAMA GROUP SHOT</text>
  </g>
</svg>'''
}

books = {
  'bok_kraft_ring.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="350" viewBox="0 0 350 350">
  <defs>
    <filter id="bookShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="6" dy="8" stdDeviation="5" flood-color="#451a03" flood-opacity="0.35"/>
    </filter>
  </defs>
  <g filter="url(#bookShadow)">
    <rect x="45" y="25" width="275" height="300" rx="10" fill="#d97706" stroke="#92400e" stroke-width="4"/>
    <rect x="65" y="45" width="235" height="260" rx="6" fill="#b45309" opacity="0.15"/>
    <rect x="30" y="25" width="25" height="300" rx="4" fill="#78350f"/>
    <circle cx="42" cy="75" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="3"/>
    <circle cx="42" cy="175" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="3"/>
    <circle cx="42" cy="275" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="3"/>
    <rect x="290" y="155" width="35" height="40" rx="4" fill="#78350f" stroke="#451a03" stroke-width="2"/>
    <circle cx="308" cy="175" r="5" fill="#fef08a"/>
    <rect x="95" y="110" width="180" height="90" rx="6" fill="#fef3c7" stroke="#78350f" stroke-width="3" stroke-dasharray="6 4"/>
    <text x="185" y="148" font-family="'Patrick Hand', cursive, sans-serif" font-size="24" font-weight="bold" fill="#78350f" text-anchor="middle">OUR MEMORIES</text>
    <text x="185" y="175" font-family="sans-serif" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle" letter-spacing="2">VINTAGE SCRAPBOOK</text>
  </g>
</svg>''',

  'bok_pastel_hologram.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="350" viewBox="0 0 350 350">
  <defs>
    <linearGradient id="holoBook" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbcfe8" />
      <stop offset="30%" stop-color="#e9d5ff" />
      <stop offset="70%" stop-color="#bae6fd" />
      <stop offset="100%" stop-color="#fed7aa" />
    </linearGradient>
    <filter id="holoShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="6" dy="8" stdDeviation="5" flood-color="#8b5cf6" flood-opacity="0.35"/>
    </filter>
  </defs>
  <g filter="url(#holoShadow)">
    <rect x="45" y="25" width="275" height="300" rx="16" fill="url(#holoBook)" stroke="#ffffff" stroke-width="5"/>
    <rect x="30" y="25" width="25" height="300" rx="6" fill="#c084fc"/>
    <path d="M 295 160 C 295 145, 280 145, 280 160 C 280 175, 295 190, 295 190 C 295 190, 310 175, 310 160 C 310 145, 295 145, 295 160 Z" fill="#881337" stroke="#ffffff" stroke-width="3"/>
    <circle cx="185" cy="165" r="55" fill="#ffffff" opacity="0.9" stroke="#e879f9" stroke-width="3"/>
    <text x="185" y="160" font-family="'Patrick Hand', cursive, sans-serif" font-size="20" font-weight="bold" fill="#7e22ce" text-anchor="middle">SWEET</text>
    <text x="185" y="182" font-family="sans-serif" font-size="11" font-weight="bold" fill="#a855f7" text-anchor="middle" letter-spacing="3">MOMENTS</text>
  </g>
</svg>''',

  'bok_velvet_black.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="350" viewBox="0 0 350 350">
  <defs>
    <linearGradient id="goldCorner" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#eab308" />
      <stop offset="100%" stop-color="#854d0e" />
    </linearGradient>
    <filter id="velvetShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="6" dy="8" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>
  <g filter="url(#velvetShadow)">
    <rect x="45" y="25" width="275" height="300" rx="10" fill="#18181b" stroke="#27272a" stroke-width="4"/>
    <polygon points="45,25 90,25 45,70" fill="url(#goldCorner)" stroke="#713f12" stroke-width="1"/>
    <polygon points="320,25 275,25 320,70" fill="url(#goldCorner)" stroke="#713f12" stroke-width="1"/>
    <polygon points="45,325 90,325 45,280" fill="url(#goldCorner)" stroke="#713f12" stroke-width="1"/>
    <polygon points="320,325 275,325 320,280" fill="url(#goldCorner)" stroke="#713f12" stroke-width="1"/>
    <rect x="95" y="110" width="180" height="100" rx="6" fill="#09090b" stroke="url(#goldCorner)" stroke-width="3"/>
    <text x="185" y="155" font-family="Georgia, serif" font-size="18" font-weight="bold" fill="#fef08a" text-anchor="middle" letter-spacing="3">CHRONICLES</text>
    <text x="185" y="180" font-family="sans-serif" font-size="10" fill="#ca8a04" text-anchor="middle" letter-spacing="4">DARK ACADEMIA</text>
  </g>
</svg>'''
}

insp_mockups = {
  'insp_dalat_vintage.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400">
  <defs>
    <filter id="inspShadow"><feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#000" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="500" height="400" fill="#f7f3eb"/>
  <rect x="25" y="25" width="450" height="350" rx="16" fill="#e8d8c3" stroke="#b45309" stroke-width="3" filter="url(#inspShadow)"/>
  <g transform="translate(60, 50) rotate(-6)">
    <rect width="160" height="190" rx="6" fill="#ffffff" filter="url(#inspShadow)"/>
    <rect x="12" y="12" width="136" height="136" fill="#84cc16" opacity="0.6"/>
    <circle cx="80" cy="70" r="25" fill="#facc15"/>
    <text x="80" y="170" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Da Lat 2026</text>
  </g>
  <g transform="translate(260, 110) rotate(8)">
    <rect width="160" height="190" rx="6" fill="#ffffff" filter="url(#inspShadow)"/>
    <rect x="12" y="12" width="136" height="136" fill="#0ea5e9" opacity="0.6"/>
    <text x="80" y="170" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Quan Ca Phe Mo Suong</text>
  </g>
  <g transform="translate(60, 260) scale(0.6)">
    <rect width="250" height="150" rx="14" fill="#0f172a" stroke="#eab308" stroke-width="4"/>
    <text x="125" y="65" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fef08a" text-anchor="middle">Indie Vibe Da Lat</text>
  </g>
  <g transform="translate(320, 40) scale(0.45)">
    <circle cx="60" cy="60" r="45" fill="#f59e0b"/>
  </g>
</svg>''',

  'insp_y2k_classmate.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400">
  <defs><filter id="inspShadow2"><feDropShadow dx="5" dy="6" stdDeviation="4" flood-color="#8b5cf6" flood-opacity="0.3"/></filter></defs>
  <rect width="500" height="400" fill="#faf5ff"/>
  <rect x="25" y="25" width="450" height="350" rx="16" fill="#f3e8ff" stroke="#c084fc" stroke-width="4" filter="url(#inspShadow2)"/>
  <g transform="translate(50, 60) rotate(-4)">
    <rect width="280" height="120" rx="8" fill="#18181b"/>
    <rect x="20" y="25" width="70" height="70" fill="#ec4899"/>
    <rect x="105" y="25" width="70" height="70" fill="#a855f7"/>
    <rect x="190" y="25" width="70" height="70" fill="#06b6d4"/>
  </g>
  <g transform="translate(240, 190) rotate(5)">
    <rect width="200" height="150" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
    <rect x="15" y="15" width="80" height="80" fill="#fde047"/>
    <rect x="105" y="15" width="80" height="80" fill="#4ade80"/>
  </g>
  <g transform="translate(360, 50) scale(0.4)">
    <path d="M150 20 Q150 150 20 150 Q150 150 150 280 Q150 150 280 150 Q150 150 150 20 Z" fill="#881337" stroke="#fff" stroke-width="4"/>
  </g>
  <g transform="translate(60, 220) scale(0.6)">
    <rect width="220" height="100" rx="20" fill="#fde047" stroke="#000" stroke-width="4"/>
    <text x="110" y="60" font-family="Impact" font-size="28" fill="#000" text-anchor="middle">BESTIES 4EVER</text>
  </g>
</svg>''',

  'insp_love_anniversary.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400">
  <defs><filter id="inspShadow3"><feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#881337" flood-opacity="0.25"/></filter></defs>
  <rect width="500" height="400" fill="#fff1f2"/>
  <rect x="25" y="25" width="450" height="350" rx="16" fill="#ffe4e6" stroke="#881337" stroke-width="3" filter="url(#inspShadow3)"/>
  <g transform="translate(60, 80)">
    <rect width="220" height="170" rx="12" fill="#fff" stroke="#881337" stroke-width="3"/>
    <text x="110" y="90" font-family="sans-serif" font-size="15" font-weight="bold" fill="#881337" text-anchor="middle">365 DAYS WITH YOU</text>
  </g>
  <g transform="translate(290, 160) rotate(8)">
    <rect width="150" height="180" rx="8" fill="#ffffff" filter="url(#inspShadow3)"/>
    <rect x="12" y="12" width="126" height="126" fill="#fda4af"/>
    <text x="75" y="160" font-family="sans-serif" font-size="12" fill="#881337" text-anchor="middle">Hen Ho Dau Tien</text>
  </g>
  <g transform="translate(320, 40) scale(0.45)">
    <path d="M 150 85 C 130 25, 35 35, 35 120 C 35 185, 150 260, 150 260 C 150 260, 265 185, 265 120 C 265 35, 170 25, 150 85 Z" fill="#881337" stroke="#fff" stroke-width="4"/>
  </g>
</svg>''',

  'insp_dark_academia.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400">
  <defs><filter id="inspShadow4"><feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#000" flood-opacity="0.5"/></filter></defs>
  <rect width="500" height="400" fill="#18181b"/>
  <rect x="25" y="25" width="450" height="350" rx="16" fill="#09090b" stroke="#eab308" stroke-width="3" filter="url(#inspShadow4)"/>
  <g transform="translate(50, 70)">
    <rect width="380" height="130" rx="8" fill="#27272a" stroke="#ca8a04" stroke-width="2"/>
    <rect x="20" y="25" width="100" height="80" fill="#52525b"/>
    <rect x="140" y="25" width="100" height="80" fill="#52525b"/>
    <rect x="260" y="25" width="100" height="80" fill="#52525b"/>
  </g>
  <g transform="translate(60, 230)">
    <rect width="180" height="90" rx="8" fill="#d97706" stroke="#92400e" stroke-width="2"/>
    <text x="90" y="55" font-family="serif" font-size="14" fill="#fef3c7" text-anchor="middle">CINEMATIC DIARY</text>
  </g>
  <g transform="translate(260, 220) scale(0.6)">
    <rect width="250" height="150" rx="14" fill="#0f172a" stroke="#fde047" stroke-width="4"/>
  </g>
</svg>'''
}

# Write files with both descriptive and SKU names
base_dir = os.path.dirname(os.path.abspath(__file__))
stickers_dir = os.path.join(base_dir, 'static', 'assets', 'stickers')
layouts_dir = os.path.join(base_dir, 'static', 'assets', 'layouts')
books_dir = os.path.join(base_dir, 'static', 'assets', 'books')

for d in [stickers_dir, layouts_dir, books_dir]:
    os.makedirs(d, exist_ok=True)

# 1. Write descriptive stickers
for fname, svg in stickers.items():
    with open(os.path.join(stickers_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

# Map to STK-001..012
stk_map = {
    'stk_001.svg': stickers.get('stk_y2k_stars.svg'),
    'stk_002.svg': stickers.get('stk_vintage_flower.svg'),
    'stk_003.svg': stickers.get('stk_genz_doodle.svg'),
    'stk_004.svg': stickers.get('stk_washi_tape.svg'),
    'stk_005.svg': stickers.get('stk_retro_cassette.svg'),
    'stk_006.svg': stickers.get('stk_sparkle_heart.svg'),
    'stk_007.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="gradShadow"><feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#1e1b4b" flood-opacity="0.4"/></filter></defs><g filter="url(#gradShadow)"><polygon points="150,45 270,105 150,165 30,105" fill="#1e1b4b" stroke="#f59e0b" stroke-width="4"/><path d="M85 135 L85 185 Q150 225 215 185 L215 135" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/><circle cx="150" cy="105" r="8" fill="#fbbf24"/><path d="M150 105 Q195 125 205 175" stroke="#f59e0b" stroke-width="4" fill="none"/><rect x="198" y="175" width="14" height="35" rx="3" fill="#fbbf24" stroke="#d97706" stroke-width="2"/><rect x="50" y="235" width="200" height="40" rx="8" fill="#fbbf24" stroke="#78350f" stroke-width="3"/><text x="150" y="261" font-family="sans-serif" font-size="14" font-weight="bold" fill="#451a03" text-anchor="middle" letter-spacing="2">GRADUATION 2026</text></g></svg>''',
    'stk_008.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="camShadow"><feDropShadow dx="4" dy="5" stdDeviation="3" flood-color="#451a03" flood-opacity="0.35"/></filter></defs><g filter="url(#camShadow)"><rect x="35" y="80" width="230" height="150" rx="16" fill="#78350f" stroke="#451a03" stroke-width="5"/><rect x="35" y="80" width="230" height="35" rx="8" fill="#d97706" stroke="#451a03" stroke-width="3"/><circle cx="80" cy="98" r="10" fill="#fef3c7" stroke="#451a03" stroke-width="2"/><circle cx="150" cy="165" r="48" fill="#1c1917" stroke="#fbbf24" stroke-width="6"/><circle cx="150" cy="165" r="32" fill="#292524" stroke="#f59e0b" stroke-width="3"/><circle cx="138" cy="153" r="10" fill="#ffffff" opacity="0.75"/><text x="150" y="255" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#78350f" text-anchor="middle" letter-spacing="2">35MM ANALOG SHOT</text></g></svg>''',
    'stk_009.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="stampShadow"><feDropShadow dx="3" dy="4" stdDeviation="3" flood-color="#0369a1" flood-opacity="0.3"/></filter></defs><g filter="url(#stampShadow)"><circle cx="150" cy="150" r="115" fill="none" stroke="#0284c7" stroke-width="6" stroke-dasharray="12 6"/><circle cx="150" cy="150" r="95" fill="#f0f9ff" stroke="#0284c7" stroke-width="3"/><path d="M85 150 L215 150" stroke="#0284c7" stroke-width="3"/><text x="150" y="80" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0369a1" text-anchor="middle" letter-spacing="3">PASSPORT ENTRY</text><text x="150" y="225" font-family="monospace" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">WANDERLUST EXP</text></g></svg>''',
    'stk_010.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="wax3D"><feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="#4c0519" flood-opacity="0.45"/></filter></defs><g filter="url(#wax3D)"><path d="M150 30 C190 25, 230 45, 255 80 C280 115, 275 165, 260 205 C245 245, 205 275, 160 270 C115 265, 75 250, 45 210 C15 170, 20 120, 50 80 C80 40, 110 35, 150 30 Z" fill="#881337" stroke="#4c0519" stroke-width="4"/><circle cx="150" cy="150" r="75" fill="#9f1239" stroke="#fda4af" stroke-width="3"/><text x="150" y="175" font-family="Georgia, serif" font-size="75" font-style="italic" font-weight="bold" fill="#fecdd3" text-anchor="middle">S</text></g></svg>''',
    'stk_011.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="cupShadow"><feDropShadow dx="3" dy="5" stdDeviation="3" flood-color="#581c87" flood-opacity="0.3"/></filter></defs><g filter="url(#cupShadow)"><rect x="35" y="40" width="230" height="220" rx="24" fill="#faf5ff" stroke="#a855f7" stroke-width="4"/><path d="M90 100 L170 100 L160 190 Q130 205 100 190 Z" fill="#c084fc" stroke="#7e22ce" stroke-width="3"/><text x="150" y="235" font-family="sans-serif" font-size="16" font-weight="bold" fill="#6b21a8" text-anchor="middle">Coffee &amp; Memories</text></g></svg>''',
    'stk_012.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><defs><filter id="frameShadow"><feDropShadow dx="4" dy="5" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/></filter></defs><g filter="url(#frameShadow)"><rect x="25" y="25" width="250" height="250" rx="16" fill="#18181b" stroke="#3f3f46" stroke-width="4"/><rect x="55" y="55" width="190" height="190" rx="8" fill="#27272a" stroke="#52525b" stroke-width="2"/><text x="150" y="155" font-family="monospace" font-size="16" font-weight="bold" fill="#71717a" text-anchor="middle">ISO 400 FILM</text></g></svg>'''
}

for fname, svg in stk_map.items():
    with open(os.path.join(stickers_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

# 2. Write descriptive layouts & mapped layouts
for fname, svg in layouts.items():
    with open(os.path.join(layouts_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

lay_map = {
    'lay_001.svg': layouts.get('lay_polaroid_single.svg'),
    'lay_002.svg': layouts.get('lay_filmstrip_triple.svg'),
    'lay_003.svg': layouts.get('lay_accordion_fold.svg'),
    'lay_004.svg': layouts.get('lay_secret_pocket.svg'),
    'lay_005.svg': layouts.get('lay_mosaic_collage.svg'),
    'lay_006.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="360" viewBox="0 0 320 360"><defs><filter id="watShadow"><feDropShadow dx="3" dy="5" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/></filter></defs><g filter="url(#watShadow)"><rect x="20" y="20" width="280" height="320" rx="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="3"/><rect x="45" y="40" width="230" height="150" rx="8" fill="#dbeafe" stroke="#60a5fa" stroke-width="2"/><rect x="45" y="70" width="230" height="150" rx="8" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/><rect x="45" y="100" width="230" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="3"/><text x="160" y="180" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e40af" text-anchor="middle">WATERFALL SLIDER</text></g></svg>''',
    'lay_007.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320"><defs><filter id="circShadow"><feDropShadow dx="3" dy="5" stdDeviation="4" flood-color="#78350f" flood-opacity="0.25"/></filter></defs><g filter="url(#circShadow)"><rect x="15" y="15" width="290" height="290" rx="16" fill="#fffbeb" stroke="#d97706" stroke-width="3"/><circle cx="160" cy="160" r="100" fill="#fef3c7" stroke="#b45309" stroke-width="4" stroke-dasharray="10 6"/><text x="160" y="165" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">PORTRAIT FRAME</text></g></svg>''',
    'lay_008.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="300" viewBox="0 0 350 300"><defs><filter id="hexShadow"><feDropShadow dx="4" dy="4" stdDeviation="3" flood-color="#a855f7" flood-opacity="0.3"/></filter></defs><g filter="url(#hexShadow)"><rect x="15" y="15" width="320" height="270" rx="14" fill="#09090b" stroke="#a855f7" stroke-width="3"/><polygon points="120,40 180,40 210,95 180,150 120,150 90,95" fill="#27272a" stroke="#ec4899" stroke-width="3"/><polygon points="220,105 280,105 310,160 280,215 220,215 190,160" fill="#27272a" stroke="#8b5cf6" stroke-width="3"/><text x="150" y="100" font-family="monospace" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">HEX 1</text></g></svg>'''
}

for fname, svg in lay_map.items():
    with open(os.path.join(layouts_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

# 3. Write descriptive books & mapped books
for fname, svg in books.items():
    with open(os.path.join(books_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

book_map = {
    'scr_001.svg': books.get('bok_kraft_ring.svg'),
    'scr_002.svg': books.get('bok_pastel_hologram.svg'),
    'scr_003.svg': books.get('bok_velvet_black.svg'),
    'scr_004.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="350" viewBox="0 0 350 350"><defs><filter id="linenShadow" x="-10%" y="-10%" width="130%" height="130%"><feDropShadow dx="6" dy="8" stdDeviation="5" flood-color="#78350f" flood-opacity="0.3"/></filter></defs><g filter="url(#linenShadow)"><rect x="45" y="25" width="275" height="300" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="4"/><rect x="65" y="45" width="235" height="260" rx="6" fill="#fde68a" opacity="0.3"/><rect x="30" y="25" width="25" height="300" rx="4" fill="#b45309"/><circle cx="42" cy="75" r="14" fill="#ca8a04"/><circle cx="42" cy="175" r="14" fill="#ca8a04"/><circle cx="42" cy="275" r="14" fill="#ca8a04"/><text x="185" y="160" font-family="Georgia, serif" font-size="18" font-weight="bold" fill="#78350f" text-anchor="middle">BOTANICAL HERITAGE</text><text x="185" y="185" font-family="sans-serif" font-size="11" fill="#92400e" text-anchor="middle">ORGANIC FABRIC</text></g></svg>'''
}

for fname, svg in book_map.items():
    with open(os.path.join(books_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

# 4. Write inspiration mockups
for fname, svg in insp_mockups.items():
    with open(os.path.join(layouts_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

insp_map = {
    'insp_001.svg': insp_mockups.get('insp_dalat_vintage.svg'),
    'insp_002.svg': insp_mockups.get('insp_y2k_classmate.svg'),
    'insp_003.svg': insp_mockups.get('insp_dark_academia.svg'),
    'insp_004.svg': insp_mockups.get('insp_love_anniversary.svg'),
    'insp_005.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400"><rect width="500" height="400" fill="#f0fdf4"/><rect x="25" y="25" width="450" height="350" rx="16" fill="#ffffff" stroke="#16a34a" stroke-width="3"/><text x="250" y="200" font-family="sans-serif" font-size="20" font-weight="bold" fill="#15803d" text-anchor="middle">GRADUATION CLASS OF 2026</text></svg>''',
    'insp_006.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="400" viewBox="0 0 500 400"><rect width="500" height="400" fill="#fefce8"/><rect x="25" y="25" width="450" height="350" rx="16" fill="#ffffff" stroke="#ca8a04" stroke-width="3"/><text x="250" y="200" font-family="monospace" font-size="20" font-weight="bold" fill="#854d0e" text-anchor="middle">COZY DAILY JOURNAL</text></svg>'''
}

for fname, svg in insp_map.items():
    with open(os.path.join(layouts_dir, fname), 'w', encoding='utf-8') as f:
        f.write(svg.strip())

print('All vector graphic assets generated successfully!')


