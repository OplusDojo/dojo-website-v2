# Assembles index.html from the template, the blueprint fragment, the scrolling strip, the pixel band and the iso generator.
# The dark v3 experiment is archived in lab/v3/.
import subprocess, sys, os
sys.dont_write_bytecode = True
from offices import render as render_offices
here = os.path.dirname(__file__)
root = os.path.join(here, '..', '..')
bp = open(os.path.join(here, 'blueprint.html')).read()
bp = bp.replace('<div data-sc-stage>', '<div data-sc-stage>\n      <div class="bp__head"><span class="chip">Approach</span><h2>Concept to production, in four revisions.</h2></div>', 1)
bp = bp.replace('data-folio="III|Concept to production" data-dark', '')
js = open(os.path.join(here, 'blueprint.js')).read()

TECH = [('amazonwebservices', 'AWS'), ('kubernetes', 'Kubernetes'), ('docker', 'Docker'), ('terraform', 'Terraform'),
        ('python', 'Python'), ('typescript', 'TypeScript'), ('nodedotjs', 'Node.js'), ('react', 'React'),
        ('nextdotjs', 'Next.js'), ('postgresql', 'PostgreSQL')]
TECH_B = [('redis', 'Redis'), ('graphql', 'GraphQL'), ('fastapi', 'FastAPI'), ('pytorch', 'PyTorch'),
          ('langchain', 'LangChain'), ('githubactions', 'GitHub Actions'),
          ('grafana', 'Grafana'), ('tailwindcss', 'Tailwind CSS')]

SERVICES = ['LLM integrations', 'RAG pipelines', 'Autonomous agents', 'AI copilots', 'Agentic workflows']  # kept for reference; the top row now shows AI_MODELS

# top row of the strip: the AI models and labs we build with (icons from simple-icons; openai.svg predates its removal there)
AI_MODELS = [('openai', 'ChatGPT'), ('claude', 'Claude'), ('googlegemini', 'Gemini'), ('deepseek', 'DeepSeek'),
             ('bytedance', 'ByteDance'), ('kimi', 'Kimi'), ('qwen', 'Qwen'), ('mistralai', 'Mistral AI'),
             ('metaai', 'Meta AI'), ('perplexity', 'Perplexity'), ('huggingface', 'Hugging Face')]

def loop(one):
    # two identical tracks side by side make the loop seamless; the second is hidden from screen readers
    return f'<div class="mq__track">{one}</div><div class="mq__track" aria-hidden="true">{one}</div>'

def tech(items):
    return loop(''.join(f'<span class="mq__item"><img src="assets/tech/{k}.svg" alt="" width="30" height="30">{n}</span>' for k, n in items))

def ai_models():
    # short list, so each track carries it twice to stay wider than a 1920px screen; the repeat is hidden from screen readers
    item = lambda k, n, hide: f'<span class="mq__item"' + (' aria-hidden="true"' if hide else '') + f'><img src="assets/tech/{k}.svg" alt="" width="30" height="30">{n}</span>'
    a = ''.join(item(k, n, False) for k, n in AI_MODELS); b = ''.join(item(k, n, True) for k, n in AI_MODELS)
    return f'<div class="mq__track">{a + b}</div><div class="mq__track" aria-hidden="true">{b + b}</div>'

def services():
    # the list is short, so each track carries it twice to stay wider than a 1920px screen;
    # the repeat inside the first track is hidden from screen readers
    a = ''.join(f'<span class="mq__svc">{n}</span>' for n in SERVICES)
    b = a.replace('class="mq__svc"', 'class="mq__svc" aria-hidden="true"')
    return f'<div class="mq__track">{a + b}</div><div class="mq__track" aria-hidden="true">{a + a}</div>'

def photo(m):
    # a real photo when assets/team/<slug>.jpg exists, otherwise the initials block
    slug, ini, name = m.group(1), m.group(2), m.group(3)
    if os.path.exists(os.path.join(root, 'assets', 'team', slug + '.jpg')):
        return f'<img class="person__photo" src="assets/team/{slug}.jpg" width="144" height="144" alt="{name}" loading="lazy">'
    return f'<div class="person__mono" aria-hidden="true">{ini}</div>'

import re
def lucide(m):
    # inline a Lucide icon (ISC licence, lab/gen/icons/) so it takes the card's colour through currentColor
    svg = open(os.path.join(here, 'icons', m.group(1) + '.svg')).read()
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S).strip()
    svg = re.sub(r'\s*class="[^"]*"', '', svg, count=1)
    svg = re.sub(r'\s+', ' ', svg).replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
    return f'<span class="svc-ico">{svg}</span>'

src = open(os.path.join(here, 'index.src.html')).read()
src = re.sub(r'\{\{LUCIDE ([a-z-]+)\}\}', lucide, src)
src = re.sub(r'\{\{PHOTO (\S+) (\S+) ([^}]+)\}\}', photo, src)
src = (src.replace('{{BLUEPRINT}}', bp).replace('{{BLUEPRINT_JS}}', js)
          .replace('{{OFFICE_NETWORK}}', render_offices())
          .replace('{{MARQUEE_SVC}}', ai_models()).replace('{{MARQUEE_TECH}}', tech(TECH + TECH_B)))
tmp = os.path.join(here, '_index.tmp.html')
open(tmp, 'w').write(src)
subprocess.run([sys.executable, os.path.join(here, 'iso.py'), tmp, os.path.join(root, 'index.html')], check=True)
os.remove(tmp)
print('built index.html')
ph = len(re.findall(r'<\w+[^>]*\sdata-placeholder[\s>]', src))
if ph:
    print(f'WARNING: {ph} placeholder metrics (data-placeholder) in index.html. Replace with real figures before the site goes public.')
