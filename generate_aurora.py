import random

svg = []
svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="100%" height="300">')
svg.append('<defs>')

# Radial Gradient with animated colors
svg.append('<radialGradient id="aurora" cx="50%" cy="0%" r="125%">')
svg.append('  <stop offset="0%" stop-color="#020617" />')
svg.append('  <stop offset="100%" stop-color="#13FFAA">')
svg.append('    <animate attributeName="stop-color" values="#13FFAA;#1E67C6;#CE84CF;#DD335C;#13FFAA" dur="10s" repeatCount="indefinite" />')
svg.append('  </stop>')
svg.append('</radialGradient>')

# Clip path for typing
svg.append('<clipPath id="typing-clip">')
svg.append('  <rect x="0" y="-45" height="60" class="mask-rect" />')
svg.append('</clipPath>')

# Clip path for marquee (centered 600px wide area)
svg.append('<clipPath id="marquee-clip">')
svg.append('  <rect x="0" y="-20" width="600" height="40" />')
svg.append('</clipPath>')

svg.append('</defs>')

svg.append('<style>')
svg.append('''
  /* Typing Animation CSS */
  .typing-text {
    font-family: 'Courier New', Courier, monospace;
    font-size: 42px;
    font-weight: 800;
    fill: #ffffff;
    letter-spacing: 2px;
    text-shadow: 0px 4px 12px rgba(255,255,255,0.2);
  }
  .cursor {
    animation: cursorMove 6s steps(11, end) infinite, blink 0.8s infinite;
  }
  @keyframes blink { 50% { opacity: 0; } }
  
  .mask-rect {
    animation: maskMove 6s steps(11, end) infinite;
  }
  
  /* 11 characters * ~27.2px width = ~300px */
  @keyframes maskMove {
    0%, 10% { width: 0; }
    40%, 80% { width: 300px; }
    90%, 100% { width: 0; }
  }
  
  @keyframes cursorMove {
    0%, 10% { transform: translateX(0); }
    40%, 80% { transform: translateX(300px); }
    90%, 100% { transform: translateX(0); }
  }

  /* Marquee Animation CSS */
  .marquee-text {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 16px;
    font-weight: 500;
    fill: #e2e8f0;
    letter-spacing: 1px;
  }
''')
svg.append('</style>')

# Background (Solid dark base + heavily softened aurora gradient)
svg.append('<rect width="100%" height="100%" fill="#030712" />')
svg.append('<rect width="100%" height="100%" fill="url(#aurora)" opacity="0.035" />')

# Stars
for _ in range(300):
    cx = random.uniform(0, 800)
    cy = random.uniform(0, 300)
    r = random.uniform(0.5, 1.8)
    delay = random.uniform(0, 5)
    dur = random.uniform(2, 6)
    svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#ffffff" opacity="0.1">')
    svg.append(f'  <animate attributeName="opacity" values="0.1;0.8;0.1" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite" />')
    svg.append('</circle>')

# Typing Name
svg.append('<g transform="translate(250, 140)">')
svg.append('  <text x="0" y="0" class="typing-text" clip-path="url(#typing-clip)">HASSAN KHAN</text>')
svg.append('  <text x="0" y="0" class="typing-text cursor">_</text>')
svg.append('</g>')

# Scrolling Marquee
svg.append('<g transform="translate(100, 180)" clip-path="url(#marquee-clip)">')
svg.append('  <text y="0" class="marquee-text">')
svg.append('    Backend Developer  •  AI/LLM Enthusiast  •  System Design')
svg.append('    <animate attributeName="x" from="600" to="-600" dur="12s" repeatCount="indefinite" />')
svg.append('  </text>')
svg.append('</g>')

# Static Sub-tagline
svg.append('<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" text-anchor="middle">')
svg.append('  <text x="400" y="235" font-size="16" font-weight="500" fill="#e2e8f0" font-style="italic">Building intelligent backend systems which are AI-driven,</text>')
svg.append('  <text x="400" y="260" font-size="16" font-weight="500" fill="#e2e8f0" font-style="italic">event-driven architecture, and distributed systems.</text>')
svg.append('</g>')

svg.append('</svg>')

with open('aurora-banner.svg', 'w') as f:
    f.write('\n'.join(svg))
