# Generates isometric SVG fragments for the O+Dojo home page.
import math, sys
C, S = math.cos(math.radians(30)), 0.5

def P(x, y, z, ox, oy):
    return (ox + (x - y) * C, oy + (x + y) * S - z)

def poly(pts, cls, extra=''):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<polygon class="{cls}" points="{d}"{extra}/>'

def slab(x0, y0, z, w, d, h, ox, oy, top='t', left='l', right='r'):
    p = lambda x, y, zz: P(x, y, zz, ox, oy)
    t = [p(x0, y0, z+h), p(x0+w, y0, z+h), p(x0+w, y0+d, z+h), p(x0, y0+d, z+h)]
    lf = [p(x0, y0+d, z+h), p(x0+w, y0+d, z+h), p(x0+w, y0+d, z), p(x0, y0+d, z)]
    rt = [p(x0+w, y0, z+h), p(x0+w, y0+d, z+h), p(x0+w, y0+d, z), p(x0+w, y0, z)]
    return poly(lf, left) + poly(rt, right) + poly(t, top)

def line(a, b, cls):
    return f'<line class="{cls}" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>'

def stack():
    ox, oy = 300, 150
    W = 240
    layers = [
        # key, z, label, parallax rate, decoration
        ('data',   0,   'YOUR DATA', '1.2', 'grid'),
        ('models', 78,  'MODELS · LLM GATEWAY', '0.5', 'ring'),
        ('agents', 156, 'AGENTS', '-0.2', 'cubes'),
        ('sec',    234, 'SECURITY · IAM · KMS', '-0.9', 'dash'),
        ('obs',    312, 'OBSERVABILITY · 24/7', '-1.6', 'dots'),
    ]
    out = []
    for key, z, label, rate, deco in layers:
        p = lambda x, y, zz: P(x, y, zz, ox, oy + 330)
        hl = key == 'agents'
        g = [f'<g class="iso-layer iso-{key}" data-sc-parallax="{rate}">']
        g.append(slab(0, 0, z, W, W, 14, ox, oy + 330,
                      top='t hl' if hl else 't', left='l hl' if hl else 'l', right='r hl' if hl else 'r'))
        zt = z + 14
        if deco == 'grid':
            for i in range(1, 6):
                g.append(line(p(i*W/6, 12, zt), p(i*W/6, W-12, zt), 'deco'))
                g.append(line(p(12, i*W/6, zt), p(W-12, i*W/6, zt), 'deco'))
        elif deco == 'ring':
            pts = [p(W/2 + 70*math.cos(a), W/2 + 70*math.sin(a), zt) for a in [i*math.pi/24 for i in range(48)]]
            g.append(poly(pts, 'deco-fill'))
            pts = [p(W/2 + 38*math.cos(a), W/2 + 38*math.sin(a), zt) for a in [i*math.pi/24 for i in range(48)]]
            g.append(poly(pts, 'deco'))
        elif deco == 'cubes':
            for cx, cy in [(186, 120), (120, 186), (186, 186)]:
                g.append(slab(cx, cy, zt, 34, 34, 24, ox, oy + 330, top="ct", left="cl", right="cr"))
        elif deco == 'dash':
            g.append(poly([p(16, 16, zt), p(W-16, 16, zt), p(W-16, W-16, zt), p(16, W-16, zt)], 'deco dash'))
            for cx, cy in [(W/2, 16), (W-16, W/2)]:
                g.append(poly([p(cx-9, cy-9, zt), p(cx+9, cy-9, zt), p(cx+9, cy+9, zt), p(cx-9, cy+9, zt)], 'deco-solid'))
        elif deco == 'dots':
            prev = None
            for i, v in enumerate([30, 52, 40, 70, 58, 86, 80, 104]):
                q = p(20 + i*28, W - 20 - v, zt)
                if prev: g.append(line(prev, q, 'deco strong'))
                g.append(f'<circle class="deco-solid" cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="3"/>')
                prev = q
        # leader + label to the right
        a = p(W, W*0.15, z + 7)
        b = (ox + 250, a[1])
        g.append(line(a, b, 'leader'))
        g.append(f'<circle class="leader-dot" cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="2.5"/>')
        g.append(f'<text class="iso-label" x="{b[0]+8:.1f}" y="{b[1]+4:.1f}">{label}</text>')
        g.append('</g>')
        out.append(''.join(g))
    return '<svg class="iso" viewBox="40 100 700 640" role="img" aria-label="Exploded isometric view of an agentic AI system: your data, models, agents, security and observability as stacked layers">' + ''.join(out) + '</svg>'

def icon(kind):
    ox, oy = 60, 20
    if kind == 'ai':
        body = slab(0, 0, 0, 60, 60, 10, ox, oy+60) + slab(8, 8, 10, 22, 22, 30, ox, oy+60, 'ct', 'cl', 'cr') + slab(34, 30, 10, 20, 20, 18, ox, oy+60, 'ct', 'cl', 'cr')
    elif kind == 'cloud':
        body = slab(0, 0, 0, 60, 60, 8, ox, oy+60) + slab(0, 0, 18, 60, 60, 8, ox, oy+60, 't hl', 'l hl', 'r hl') + slab(0, 0, 36, 60, 60, 8, ox, oy+60)
    elif kind == 'sec':
        body = slab(0, 0, 0, 60, 60, 8, ox, oy+60) + slab(14, 14, 8, 32, 32, 34, ox, oy+60, 't hl', 'l hl', 'r hl')
    elif kind == 'ops':
        body = ''.join(slab(i*21, 0, 0, 16, 60, 10 + i*14, ox, oy+60, 'ct' if i == 2 else 't', 'cl' if i == 2 else 'l', 'cr' if i == 2 else 'r') for i in range(3))
    else:  # arch
        body = slab(0, 0, 0, 60, 60, 6, ox, oy+60) + slab(0, 0, 6, 26, 60, 26, ox, oy+60) + slab(34, 0, 6, 26, 26, 44, ox, oy+60, 't hl', 'l hl', 'r hl')
    return f'<svg class="ico" viewBox="0 -4 130 152" aria-hidden="true">{body}</svg>'

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    s = open(src).read().replace('{{ISO_STACK}}', stack())
    for k in ['ai', 'cloud', 'sec', 'ops', 'arch']:
        s = s.replace('{{ICON_' + k.upper() + '}}', icon(k))
    open(dst, 'w').write(s)
