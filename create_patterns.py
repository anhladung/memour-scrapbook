import os

PATTERNS_DIR = os.path.join('static', 'assets', 'patterns')
os.makedirs(PATTERNS_DIR, exist_ok=True)

patterns = [
    ('pat_kraft.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#e8d8c3"/>
  <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/></filter>
  <rect width="400" height="400" fill="#d97706" opacity="0.12" filter="url(#noise)"/>
  <path d="M20,50 Q40,48 60,52 M150,180 Q180,182 210,178 M280,320 Q310,318 340,322 M80,280 Q100,282 120,279 M250,80 Q270,78 290,82" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.3" fill="none"/>
</svg>'''),
    ('pat_grid.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#fcfaf6"/>
  <defs>
    <pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse">
      <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#881337" stroke-width="0.6" stroke-opacity="0.2"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#grid)"/>
</svg>'''),
    ('pat_dotgrid.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#fbf8f2"/>
  <defs>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="1.2" fill="#78350f" fill-opacity="0.35"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#dots)"/>
</svg>'''),
    ('pat_botanical.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#f5f0e6"/>
  <defs>
    <pattern id="flora" width="80" height="80" patternUnits="userSpaceOnUse">
      <circle cx="40" cy="40" r="4" fill="#d97706" fill-opacity="0.6"/>
      <path d="M40,30 Q35,35 40,40 Q45,35 40,30 M40,50 Q35,45 40,40 Q45,45 40,50 M30,40 Q35,35 40,40 Q35,45 30,40 M50,40 Q45,35 40,40 Q45,45 50,40" fill="#881337" fill-opacity="0.35"/>
      <circle cx="15" cy="15" r="2" fill="#059669" fill-opacity="0.4"/>
      <circle cx="65" cy="65" r="2" fill="#059669" fill-opacity="0.4"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#flora)"/>
</svg>'''),
    ('pat_vintage_news.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#eedcc8"/>
  <line x1="20" y1="30" x2="180" y2="30" stroke="#78350f" stroke-width="3" stroke-opacity="0.4"/>
  <line x1="20" y1="45" x2="180" y2="45" stroke="#78350f" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="20" y1="55" x2="170" y2="55" stroke="#78350f" stroke-width="1" stroke-opacity="0.2"/>
  <line x1="20" y1="65" x2="180" y2="65" stroke="#78350f" stroke-width="1" stroke-opacity="0.2"/>
  <rect x="220" y="30" width="150" height="90" fill="#d97706" fill-opacity="0.15" stroke="#78350f" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="20" y1="150" x2="380" y2="150" stroke="#78350f" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="4 2"/>
  <line x1="20" y1="180" x2="380" y2="180" stroke="#78350f" stroke-width="1" stroke-opacity="0.2"/>
  <line x1="20" y1="195" x2="370" y2="195" stroke="#78350f" stroke-width="1" stroke-opacity="0.2"/>
  <line x1="20" y1="210" x2="380" y2="210" stroke="#78350f" stroke-width="1" stroke-opacity="0.2"/>
  <circle cx="320" cy="300" r="45" fill="none" stroke="#881337" stroke-width="2" stroke-opacity="0.3" stroke-dasharray="3 3"/>
  <text x="320" y="305" font-family="monospace" font-size="11" font-weight="bold" fill="#881337" fill-opacity="0.4" text-anchor="middle">POSTAGE 1998</text>
</svg>'''),
    ('pat_gingham_pink.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#ffffff"/>
  <defs>
    <pattern id="gingham" width="40" height="40" patternUnits="userSpaceOnUse">
      <rect x="0" y="0" width="20" height="40" fill="#f472b6" fill-opacity="0.22"/>
      <rect x="0" y="0" width="40" height="20" fill="#f472b6" fill-opacity="0.22"/>
      <rect x="0" y="0" width="20" height="20" fill="#db2777" fill-opacity="0.25"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#gingham)"/>
</svg>'''),
    ('pat_black_card.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#1c1917"/>
  <filter id="blacknoise"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2"/></filter>
  <rect width="400" height="400" fill="#44403c" opacity="0.25" filter="url(#blacknoise)"/>
</svg>'''),
    ('pat_parchment.svg', '''<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#ebd8b8"/>
  <radialGradient id="parchmentGrad" cx="50%" cy="50%" r="50%">
    <stop offset="60%" stop-color="#ebd8b8" stop-opacity="0"/>
    <stop offset="100%" stop-color="#b45309" stop-opacity="0.35"/>
  </radialGradient>
  <rect width="400" height="400" fill="url(#parchmentGrad)"/>
  <path d="M0,0 Q200,40 400,0 L400,400 Q200,360 0,400 Z" fill="#92400e" fill-opacity="0.05"/>
</svg>''')
]

for filename, content in patterns:
    with open(os.path.join(PATTERNS_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(content)

print('8 Paper patterns successfully created in static/assets/patterns!')
