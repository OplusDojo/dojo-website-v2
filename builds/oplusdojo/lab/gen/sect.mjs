// Screenshots named sections of a page: node sect.mjs URL OUTDIR WIDTH HEIGHT sel1 sel2 ...
import { chromium } from 'playwright-core';
const [,, url, out, w, h, ...sels] = process.argv;
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
const p = await b.newPage({ viewport: { width: +w, height: +h } });
await p.goto(url, { waitUntil: 'networkidle' });
const H = await p.evaluate(() => document.documentElement.scrollHeight);
for (let y = 0; y < H; y += 400) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(60); }
for (const s of sels) {
  const y = await p.evaluate(s => { const e = document.querySelector(s); return e ? e.getBoundingClientRect().top + scrollY : -1; }, s);
  if (y < 0) { console.log('missing', s); continue; }
  await p.evaluate(y => scrollTo(0, y - 64), y); await p.waitForTimeout(1600);
  await p.screenshot({ path: `${out}/${s.replace(/[^a-z0-9]/gi, '')}.png` });
}
await b.close();
