"""Generate the office map from public-domain Natural Earth 110m land geometry.

Coordinates are approximate city centres, not street-address pins.
Source: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_land.geojson
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OFFICES = [
    ('toronto', 'Toronto', 'Canada', -79.38, 43.65, -90, -42),
    ('new-york', 'New York', 'United States', -74.01, 40.71, -76, 57),
    ('dubai', 'Dubai', 'United Arab Emirates', 55.27, 25.20, -26, -40),
    ('dhaka', 'Dhaka', 'Bangladesh', 90.41, 23.81, 58, 51),
]


def project(lon, lat):
    return 600 + lon * 3.12 * (0.78 + 0.22 * math.cos(math.radians(lat))), 325 - lat * 3.65


def inside(lon, lat, ring):
    result = False
    previous = ring[-1]
    for current in ring:
        x1, y1 = previous
        x2, y2 = current
        if (y1 > lat) != (y2 > lat) and lon < (x2 - x1) * (lat - y1) / (y2 - y1) + x1:
            result = not result
        previous = current
    return result


def render():
    polygons = json.loads((HERE / 'offices-land.json').read_text())
    bounds = [(min(p[0] for p in rings[0]), min(p[1] for p in rings[0]),
               max(p[0] for p in rings[0]), max(p[1] for p in rings[0]), rings) for rings in polygons]
    dots, regions = [], [[] for _ in OFFICES]
    for row in range(79):
        lat = -56 + row * 1.8
        for column in range(200):
            lon = -179 + column * 1.8 + (row % 2) * 0.9
            land = any(a <= lon <= c and b <= lat <= d and inside(lon, lat, rings[0])
                       and not any(inside(lon, lat, hole) for hole in rings[1:])
                       for a, b, c, d, rings in bounds)
            if not land:
                continue
            x, y = project(lon, lat)
            dot = f'M{x:.1f},{y:.1f}h.1'
            dots.append(dot)
            for i, (_, _, _, ox, oy, _, _) in enumerate(OFFICES):
                if ((lon - ox) * math.cos(math.radians(oy))) ** 2 + (lat - oy) ** 2 < 26 ** 2:
                    regions[i].append(dot)

    paths = ['<path class="offices__land" d="' + ''.join(dots) + '"/>']
    for i, region in enumerate(regions):
        paths.append(f'<path class="offices__region" data-office-region="{i}" d="{"".join(region)}"/>')
    # Each route is decorative, connecting office locations rather than claiming flight paths.
    for i, (start, end, lift) in enumerate([(0, 1, 28), (0, 2, 155), (1, 3, 125), (2, 3, 65)]):
        a, b = OFFICES[start], OFFICES[end]
        x1, y1 = project(a[3], a[4])
        x2, y2 = project(b[3], b[4])
        d = f'M{x1:.1f},{y1:.1f} C{x1+(x2-x1)*.3:.1f},{min(y1,y2)-lift:.1f} {x1+(x2-x1)*.7:.1f},{min(y1,y2)-lift:.1f} {x2:.1f},{y2:.1f}'
        paths.append(f'<path class="offices__route-base" d="{d}"/><path class="offices__route" data-office-route="{i}" pathLength="1" d="{d}"/>')
    for i, (slug, city, country, lon, lat, dx, dy) in enumerate(OFFICES):
        x, y = project(lon, lat)
        align = 'end' if dx < 0 else 'start'
        paths.append(f'''<g class="offices__pin" data-office-pin="{i}">
          <circle class="offices__ring" cx="{x:.1f}" cy="{y:.1f}" r="10"/>
          <circle class="offices__point" cx="{x:.1f}" cy="{y:.1f}" r="4"/>
          <path class="offices__leader" d="M{x:.1f},{y:.1f}l{dx*.48:.1f},{dy:.1f}h{dx*.52:.1f}"/>
          <text x="{x+dx:.1f}" y="{y+dy-9:.1f}" text-anchor="{align}">{city}</text>
        </g>''')
    return '''<section class="offices" id="offices" aria-labelledby="offices-h">
    <div class="offices__stage">
      <div class="frame offices__layout">
        <div class="offices__copy">
          <h2 id="offices-h" class="display display--lg">Four locations.<br><span>One connected team.</span></h2>
          <p>From North America to the Middle East and South Asia.</p>
        </div>
        <div class="offices__visual">
          <svg class="offices__map" viewBox="190 20 920 500" role="img" aria-label="Our offices connected across Toronto, New York, Dubai and Dhaka" focusable="false">
            <g class="offices__geography">''' + '\n'.join(paths) + '''</g>
          </svg>
        </div>
      </div>
    </div>
  </section>'''
