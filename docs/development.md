# Development and feedback

## Local preview

Run from `builds/oplusdojo/`:

```bash
npm ci
npm run dev -- 9500
```

`dev.py` binds to localhost, rebuilds homepage and case studies at startup, bundles the development toolbar with esbuild, and starts or reuses Agentation at port 4747. Its default site port is 4500; the current working preview is 9500. Inspect listeners before starting a second server on either port.

The watcher monitors root site files, work/, assets/ and lab/gen/. Generator or team-photo changes rebuild the pages. Updates refresh the browser and restore scroll position. Refresh at the top to review the hero entrance; hot reload halfway down the page can miss it.

A plain `python3 -m http.server <port>` serves existing generated files without rebuilding, hot reload or Agentation. Comparison previews should serve an identified main-branch snapshot on a separate free port. Port 9800 previously served such a snapshot; it is not a live view of current main. Verify which directory a server owns before editing.

## Build outputs

```bash
python3 lab/gen/build.py
python3 lab/gen/cases.py
```

The first builds index.html; the second builds work/elora.html, work/tenera.html and work/ralhf.html. Homepage generation warns about five `data-placeholder` metrics. The warning does not mean their claims have been approved.

Python 3 is required for generators and preview. The installed Node dependencies support browser checks and the React-based development toolbar; the deployed website itself is static. `package.json` has no real test suite: its test script is a placeholder.

## Agentation

`agentation-preview.jsx` mounts one toolbar connected to `http://localhost:4747`. The preview injects its bundle from `/__dev/agentation.js` into served HTML. Generated production HTML contains no toolbar mount or development refresh script.

To register a client against the same server:

```bash
codex mcp add agentation -- npx -y agentation-mcp@1.3.2 server --mcp-only --http-url http://localhost:4747
```

For Claude Code, register the equivalent command with `claude mcp add`. Reconnect the client's tools after configuration changes. Check services with:

```bash
npx agentation-mcp doctor --http-url http://localhost:4747
```

A healthy server is not proof of browser sync. Create a clearly identified browser test annotation, retrieve its exact text and page through `agentation_get_all_pending`, and resolve that test annotation after verification. Existing user notes have also been successfully read and resolved through this server.

When processing feedback:

1. Read pending annotations and check their URL and section. Distinguish 9500 from old 4500/9800 comparison previews.
2. Confirm the target branch and base from the user's latest instruction. Annotation location alone does not select a Git branch.
3. Apply and verify the requested changes, then resolve only the addressed annotations with a short summary.

When Agentation's MCP tools are not exposed directly in the session, its installed MCP SDK can connect to `http://localhost:4747/mcp` using `StreamableHTTPClientTransport`. Reuse the existing server; avoid competing instances on the same port.

## Motion implementation

- `motion-refinements.css`: CSS hero entrance, design-token bridge to the taste layer, focus styling and reduced-motion rules.
- `motion-refinements.js`: one-time IntersectionObserver entrances driven by native Web Animations. It owns opposing logo-band wipes, masked headings, alternating service entrances, team scale entrances, testimonial soft-focus entrances and closing effects.
- Selected Work's heading and entire cards use simple fade-and-rise. Team figures use that simpler treatment too.
- `assets/motion/`: vendored taste motion CSS/module for micro-interactions. Keep source edits outside vendored files where possible.
- Logo entrances animate the outer bands. Continuous marquee travel animates the inner tracks, so the timelines do not overwrite each other. Track-duration synchronisation lives in the homepage source.
- The blueprint and footer map retain their own scroll timelines. The blueprint reverses when scrolling up; the map reaches completion near the page bottom.
- Finished entrance animations release inline opacity and animation transforms. Focus, printing, restored browser pages and reduced-motion changes reveal relevant content immediately.

## Verification

Rebuild first, then use headless Chrome with Playwright from the site's installed dependencies. Check 1440px desktop and 390px phone; team changes also need 1024px and 768px tablet checks. Inspect actual screenshots, image loading, console errors, horizontal overflow, final scroll states and keyboard focus. Check reduced motion separately.

For settled section screenshots:

```bash
mkdir -p lab/shots
node lab/gen/sect.mjs http://localhost:9500 lab/shots 1440 900 '#team' '#work'
```

For entrances, capture during animation and after completion. Check that different recipes actually animate, content finishes visible, backward scrolling does not replay one-time entrances, and hover still works after arrival. A backgrounded app browser can throttle animation frames; use headless Chrome or a foreground page.

Ad hoc check scripts and screenshots under lab/ are ignored, local evidence rather than a maintained test suite. Full taste-gate findings include retained-layout conflicts and unresolved issues; do not report GATE: PASS without the actual result. The quoted word “effortlessly” has a local waiver because it is part of a supplied client testimonial.
