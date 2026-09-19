import os

NOTE_SVGS = {
    "lay_note_lined.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="noteShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <g filter="url(#noteShadow)">
    <!-- Base Note Paper Sheet -->
    <rect x="20" y="20" width="320" height="260" rx="8" fill="#fdfbf7" stroke="#e5e0d8" stroke-width="2"/>
    <!-- Top Washi Tape -->
    <rect x="130" y="10" width="100" height="22" rx="3" fill="#fb7185" opacity="0.85" transform="rotate(-2 180 20)"/>
    <!-- Title Area -->
    <text x="45" y="60" font-family="'Patrick Hand', cursive, sans-serif" font-size="20" font-weight="bold" fill="#881337">✦ Nhật Ký Ghi Chú:</text>
    <!-- Ruled Lines for Handwriting -->
    <line x1="45" y1="90" x2="315" y2="90" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="125" x2="315" y2="125" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="160" x2="315" y2="160" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="195" x2="315" y2="195" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="230" x2="315" y2="230" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="260" x2="315" y2="260" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <text x="310" y="272" font-family="'Patrick Hand', cursive" font-size="12" fill="#94a3b8" text-anchor="end">MEMOUR • Write your story here...</text>
  </g>
</svg>""",

    "lay_note_grid.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="gridNoteShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.2"/>
    </filter>
    <pattern id="noteGridPattern" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M 16 0 L 0 0 0 16" fill="none" stroke="#e2e8f0" stroke-width="1"/>
    </pattern>
  </defs>
  <g filter="url(#gridNoteShadow)">
    <rect x="20" y="20" width="320" height="260" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="35" y="35" width="290" height="230" fill="url(#noteGridPattern)"/>
    <!-- Cute Binder Clip -->
    <rect x="155" y="12" width="50" height="18" rx="4" fill="#334155"/>
    <circle cx="180" cy="21" r="4" fill="#f8fafc"/>
    <text x="45" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="900" fill="#0f172a">MEMO NOTE ✦</text>
  </g>
</svg>""",

    "lay_note_kraft.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="kraftNoteShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#78350f" flood-opacity="0.25"/>
    </filter>
  </defs>
  <g filter="url(#kraftNoteShadow)">
    <rect x="20" y="20" width="320" height="260" rx="10" fill="#e8d8c3" stroke="#b45309" stroke-width="2"/>
    <rect x="32" y="32" width="296" height="236" rx="6" fill="none" stroke="#78350f" stroke-width="1.5" stroke-dasharray="5 4"/>
    <!-- Stamp -->
    <circle cx="285" cy="65" r="22" fill="none" stroke="#881337" stroke-width="2" opacity="0.8"/>
    <text x="285" y="68" font-family="monospace" font-size="8" font-weight="bold" fill="#881337" text-anchor="middle">PASSPORT</text>
    <!-- Lined rows -->
    <text x="45" y="65" font-family="'Patrick Hand', cursive" font-size="20" font-weight="bold" fill="#78350f">✦ Ghi Chú Kỷ Niệm:</text>
    <line x1="45" y1="100" x2="305" y2="100" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="140" x2="305" y2="140" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="180" x2="305" y2="180" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="220" x2="305" y2="220" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="250" x2="305" y2="250" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
  </g>
</svg>"""
}

target_dir = os.path.join("static", "assets", "layouts")
os.makedirs(target_dir, exist_ok=True)

for fname, content in NOTE_SVGS.items():
    fpath = os.path.join(target_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {fpath}")
