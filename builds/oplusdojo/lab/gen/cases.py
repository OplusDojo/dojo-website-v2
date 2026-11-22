# Builds work/<slug>.html case study pages from one template.
# Facts come from oplusdojo.com (read 2026-10-31) and each client's public site.
import os
here = os.path.dirname(__file__)
root = os.path.join(here, '..', '..')
os.makedirs(os.path.join(root, 'work'), exist_ok=True)

CASES = {
 'elora': dict(
  name='Elora', brand='#E0789F', logo='../assets/elora/logo-light.svg',
  title='Elora case study',
  tag='A secure care platform that helps frontline teams keep people covered.',
  meta=[('Industry', 'Healthcare and social services'), ('Platform', 'Mobile and web'),
        ('Our role', 'Architecture, AI development, DevOps'), ('Outcome', 'Launched 2x faster')],
  hero=('../assets/elora/hero.jpg', 3327, 2350, 'A care worker with an older patient and his family at home'),
  lead='Frontline caregivers were losing hours to paperwork. <em>Elora needed a platform secure enough for sensitive care data, credible enough for investors, and shipped fast.</em>',
  challenge='<p>Elora supports caregivers and social service professionals who coordinate care for the people who depend on them. Every hour spent on forms and follow-ups is an hour not spent with a client.</p><p>They needed a production system, not a prototype: one that protects sensitive data, scales with every new partner organisation, and holds up to investor scrutiny.</p>',
  built=['Architecture for a secure, scalable system', 'Caseload management', 'Community referrals', 'A collaborative care tool for frontline teams', 'AI development and DevOps infrastructure, delivered across time zones'],
  pair=[('../assets/elora/home-before-visit.png', 'Patients view in the Elora platform', 'Patient coverage at a glance'),
        ('../assets/elora/home-during-visit.png', 'Elora listening during a visit and filling in an intake form', 'AI that listens and fills in the forms')],
  show=('img', '../assets/elora/home-before-visit.png', 'The Elora platform'),
  show_cap='Built for the people doing the work. Caseloads, referrals and care coordination in one place.',
  trio=[('../assets/elora/home-before-visit.png', 'Before the visit', 'Coverage status for every patient, before anyone walks in the door.'),
        ('../assets/elora/home-during-visit.png', 'During the visit', 'Elora listens and completes intake and consent forms in the background.'),
        ('../assets/elora/home-after-visit.png', 'After the visit', 'Overdue follow-ups surface automatically, so nobody falls through.')],
  trio_note='Elora’s platform today. Product imagery from elorahq.com.',
  results=[('7', '+ hrs', 'Saved per case for caregivers and social service professionals'),
           ('2', 'x', 'Faster to launch, without compromising quality, compliance or security')],
  quote='I couldn’t be more impressed with the team at OPlus Dojo. Their commitment, expertise, and execution have been exceptional. Thanks to their work, our customers are thrilled, and both potential clients and investors have greater confidence in Elora’s vision and technology.',
  who=('Melanie Chen', 'CTO and Cofounder, EloraHQ'),
  next=('tenera', 'Tenera', '../assets/tenera/officeReport.jpg'),
 ),
 'tenera': dict(
  name='Tenera', brand='#5BB043', logo='../assets/tenera/Tenera-T-Green-BG.png',
  title='Tenera case study',
  tag='Intelligent automation for property maintenance, from the field to the finished report.',
  meta=[('Industry', 'Property technology'), ('Platform', 'AI platform, web and mobile'),
        ('Our role', 'Architecture, AI development, platform engineering'), ('Outcome', 'Accelerated launch')],
  hero=('../assets/tenera/officeReport.jpg', 1291, 768, 'A finished Tenera inspection report on a desktop monitor in a bright office'),
  lead='Property managers and service providers were buried in manual workflows. <em>Tenera needed a secure, scalable platform with AI at its core, and they needed it in market quickly.</em>',
  challenge='<p>The property maintenance lifecycle runs on site visits, photos, notes and reports, passed between property managers and service providers. Most of it was manual.</p><p>Tenera set out to automate it with AI. That meant a platform that could be trusted with real client data, scale with demand, and be easy enough for people in the field.</p>',
  built=['Architecture for a secure, scalable platform', 'Intelligent automation across the property maintenance lifecycle', 'Core workflow features for property managers and service providers', 'Embedded delivery alongside Tenera’s in-house team'],
  pair=[('../assets/tenera/artifact_gathering.jpg', 'A phone capturing photos and voice notes of a leak in a parking garage', 'Capture on site'),
        ('../assets/tenera/review_doc.jpg', 'An inspector in a hard hat reviewing a report on a tablet in a parking garage', 'Review in the field')],
  show=('video', '../assets/tenera/demo.mp4', 'Tenera generating an inspection report from site artifacts'),
  show_cap='From site visit to finished report. Photos, video and voice notes go in; a complete, formatted report comes out.',
  trio=[],
  trio_note='',
  results=[('20–30', '', 'Page technical reports, written by Tenera Reports in minutes, not hours'),
           ('Field', '→ report', 'Photos, video and voice notes in. A client-ready report out.')],
  quote='Partnering with OPlus Dojo has been a game-changer for us. Their team brought not only deep technical expertise in AI and scalable infrastructure but also a true understanding of how to translate complex workflows into seamless user experiences. They integrated effortlessly with our in-house team, consistently delivering high-quality solutions on time.',
  who=('Eugene Solodkin', 'CTO, Tenera'),
  next=('ralhf', 'RaLHF', '../assets/ralhf/top.jpg'),
 ),
 'ralhf': dict(
  name='RaLHF', brand='#8B5CF6', logo='../assets/ralhf/botfood-wordmark.svg',
  title='RaLHF case study',
  tag='A context assistant that gives your AI the history behind your life, on your terms.',
  # TODO(owner): confirm O+Dojo's exact role and add any results to quote.
  meta=[('Industry', 'Consumer AI'), ('Platform', 'Web, desktop and AI assistants'),
        ('Company', 'Bot Food Co, Toronto'), ('Status', 'In beta')],
  hero=('../assets/ralhf/top.jpg', 2880, 1800, 'The RaLHF home page: Are you Contexxt Maxxing?'),
  lead='Your AI is only as good as the information you feed it. <em>RaLHF collects the context people choose, keeps it fresh, and feeds it to the AI they already use.</em>',
  challenge='<p>Personal AI assistants start every conversation knowing almost nothing about you: what you buy, where you go, what you enjoy. People end up explaining their background again and again.</p><p>RaLHF set out to give people a history they own, collected from the accounts and files they choose, and to make it useful to any AI they use now or in years to come.</p>',
  built_h='The product',
  built=['Collects context from the web apps, files, folders and email people choose', 'Keeps that context fresh as life moves on', 'Feeds it to the AI assistants people already use', 'Puts people in control of what their AI can access'],
  pair=[('../assets/ralhf/cards.jpg', 'RaLHF context cards for subscriptions, travel, taste, watchlist and purchases', 'Your digital stream'),
        ('../assets/ralhf/phone.jpg', 'The RaLHF home page on a phone', 'Contexxt Maxxing, on mobile')],
  show=('video', '../assets/ralhf/scroll.mp4', 'Scrolling through the RaLHF home page'),
  show_cap='Your subscriptions, travel, taste and choices, turned into context your AI can use.',
  trio=[('../assets/ralhf/foryou.jpg', 'Is Contexxt Maxxing for you?', 'Personal help, recommendations that fit, and no more explaining your background.'),
        ('../assets/ralhf/history.jpg', 'A history you own', 'Start with the records you already have and keep adding what you cannot recreate later.'),
        ('../assets/ralhf/top.jpg', 'Context, maxxed', 'RaLHF, pronounced Ralph, is the context layer people own.')],
  trio_note='RaLHF today. Product imagery from ralhf.ai.',
  results=[],
  quote='',
  who=('', ''),
  next=('elora', 'Elora', '../assets/elora/hero.jpg'),
 ),
}

def page(slug, c):
    meta = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in c['meta'])
    built = ''.join(f'<li>{b}</li>' for b in c['built'])
    pair = ''.join(
        f'<figure class="{cls}" data-sc-in><div class="shot"><img src="{src}" alt="{alt}" data-sc-parallax="{rate}" decoding="async"></div><figcaption>{cap}</figcaption></figure>'
        for (src, alt, cap), cls, rate in zip(c['pair'], ['a', 'b'], ['0.8', '1.4']))
    kind, src, alt = c['show']
    screen = (f'<video src="{src}" muted loop playsinline autoplay aria-label="{alt}"></video>' if kind == 'video'
              else f'<img src="{src}" alt="{alt}">')
    trio = ''
    if c['trio']:
        items = ''.join(f'<figure data-sc-in><div class="shot"><img src="{s}" alt="{h}" decoding="async"></div><h3>{h}</h3><p>{p}</p></figure>' for s, h, p in c['trio'])
        trio = f'<section class="wide"><div class="trio" data-sc-in data-sc-stagger="80">{items}</div><p class="mono" style="color:var(--sc-ink-soft);margin:0 0 4rem">{c["trio_note"]}</p></section>'
    results = ''.join(f'<div data-sc-in><b>{n}<small>{u}</small></b><span>{t}</span></div>' for n, u, t in c['results'])
    results_html = (f'<section class="wide" aria-label="Results"><span class="chip" style="display:inline-flex;margin:4rem 0 0">Results</span><div class="results" style="margin-top:1.4rem">{results}</div></section>' if c['results'] else '')
    quote_html = (f'<section class="wide c-quote"><figure data-sc-in data-sc-stagger="80" style="margin:0"><blockquote>{c["quote"]}</blockquote><figcaption><b>{c["who"][0]}</b>{c["who"][1]}</figcaption></figure></section>' if c['quote'] else '')
    nslug, nname, nimg = c['next']
    hsrc, hw, hh, halt = c['hero']
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{c['title']} · O+Dojo</title>
<meta name="description" content="{c['tag']}">
<link rel="icon" href="../assets/OPlusDojo-favicon-32px.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../scrollcraft.css">
<link rel="stylesheet" href="../site.css">
<link rel="stylesheet" href="../case.css">
<style>:root {{ --brand: {c['brand']}; }}</style>
</head>
<body class="case-page">

<nav class="pill" aria-label="Primary">
  <a class="pill__mark" href="../index.html" aria-label="O+Dojo home"><img src="../assets/OPlusDojo-logo.final.svg" width="557" height="300" alt="O+Dojo"></a>
  <a href="../index.html#work">Work</a>
  <a href="../index.html#approach">Approach</a>
  <a class="pill__cta" href="mailto:hello@oplusdojo.com?subject=Book%20a%20call">Book a call</a>
</nav>

<main>
  <header class="c-hero wide" data-sc-in data-sc-stagger="80">
    <span class="chip">Case study</span>
    <h1 class="c-name">{c['name']}</h1>
    <p class="c-tag">{c['tag']}</p>
    <dl class="c-meta">{meta}</dl>
  </header>

  <section class="grow" data-sc-act="pin" data-sc-span="1.7" aria-label="{c['name']} hero image">
    <div data-sc-stage>
      <div class="grow__frame"><img src="{hsrc}" width="{hw}" height="{hh}" alt="{halt}"></div>
    </div>
  </section>

  <section class="wide c-over">
    <span class="chip" data-sc-in>Overview</span>
    <div data-sc-in data-sc-stagger="70">
      <p class="c-over__lead">{c['lead']}</p>
      <div class="c-cols">
        <div><h3>The challenge</h3>{c['challenge']}</div>
        <div><h3>{c.get('built_h', 'What we built')}</h3><ul>{built}</ul></div>
      </div>
    </div>
  </section>

  <section class="wide" data-sc-act="flow"><div class="pair">{pair}</div></section>

  <section class="show" data-sc-act="pin" data-sc-span="2" aria-label="{c['name']} product">
    <div data-sc-stage>
      <div class="show__screen">{screen}</div>
      <div class="show__cap" data-sc-cue="0.35 1 0.3 0"><span class="chip">The product</span><p>{c['show_cap']}</p></div>
    </div>
  </section>

  {trio}

  {results_html}

  {quote_html}

  <a class="next" href="{nslug}.html">
    <img src="{nimg}" alt="" decoding="async">
    <div class="next__scrim" aria-hidden="true"></div>
    <div class="next__copy"><div><span class="mono">Next case study</span><strong>{nname}</strong></div><span class="btn">View case <span class="arr" aria-hidden="true">→</span></span></div>
  </a>

  <footer class="wide c-foot">
    <span>© 2026 OPlus Dojo · <a href="mailto:hello@oplusdojo.com?subject=Book%20a%20call">Book a call</a></span>
    <span>Client imagery courtesy of {c['name']}’s public website.</span>
  </footer>
</main>

<script src="../scrollcraft.js"></script>
<script>ScrollCraft.mount(document.body);</script>
</body>
</html>
'''

for slug, c in CASES.items():
    open(os.path.join(root, 'work', slug + '.html'), 'w').write(page(slug, c))
    print('built work/' + slug + '.html')
