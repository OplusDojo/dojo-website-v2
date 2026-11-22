# Shared agent instructions

## Scope and context

Work only on the sample site at `builds/oplusdojo/` unless the user expands scope. The neighbouring `../dojo-website/` is a different site. Read [README.md](README.md) for navigation and [PRODUCT.md](PRODUCT.md) before changing messaging, biographies or claims.

The product is an AI and cloud engineering services site. Its main action is **Book a call**. Preserve the user's latest approved design and instructions when a reference, skill or older document disagrees.

## Workflow

1. Check the current branch, working tree and running preview before editing. Preserve unrelated changes.
2. Use the source map below. Rebuild generated pages after source edits.
3. Review the result at the requested preview port; 9500 is the current working convention. Check desktop, phone and reduced motion. Interactive changes also need hover and keyboard checks.
4. For motion changes, verify actual playback during the entrance and the final state. A settled screenshot does not prove an animation runs.
5. Commit only when requested; include generated HTML. Push and deployment are separate actions. Read [deployment instructions](docs/deployment.md) before deploying to the existing Vercel project.

Read [development instructions](docs/development.md) when running the preview, handling Agentation or checking motion. Read [skills documentation](docs/skills.md) when invoking, installing or updating a project skill.

## Source map

Paths below are relative to `builds/oplusdojo/`.

| Change | Owning source |
|---|---|
| Homepage markup, team cards, page CSS, logo-speed synchronisation | `lab/gen/index.src.html` |
| Selected typography and testimonial layout | `selected-taste.css` |
| Hero entrance, viewport entrance recipes and motion styling | `motion-refinements.js`, `motion-refinements.css` |
| Vendored taste micro-interaction layer | `assets/motion/motion.js`, `assets/motion/motion.css` |
| Blueprint drawing and revision timeline | `lab/gen/blueprint.html`, `lab/gen/blueprint.js` |
| Location map geometry, pins, labels and heading | `lab/gen/offices.py`, `lab/gen/offices-land.json` |
| Location map styling and scroll progress | `offices.css`, `offices.js` |
| Shared tokens, navigation, buttons, footer and blueprint layout | `site.css` |
| Hero isometric graphics and service icons | `lab/gen/iso.py` |
| Logo lists and homepage assembly | `lab/gen/build.py` |
| Case study content and templates | `lab/gen/cases.py`, `case.css` |
| Local preview and feedback toolbar | `dev.py`, `agentation-preview.jsx` |

`index.html` and `work/*.html` are generated outputs. Keep `scrollcraft.js` and `scrollcraft.css` unchanged; extend the page-specific sources instead. Shared `site.css` changes also affect case studies, which must be checked.

The scroll engine publishes `--sc-p`; the blueprint reads it. The location map owns a separate native-scroll timeline. Keep those two signature scenes working when changing general entrances.

## Approved design and behaviour

- Full-width white/green/black design; the logo retains its blue. `.mark` is the green headline highlight. Keep the black map/footer composition.
- Current references: Baseten for visual direction, Codegent for varied entrances, Gradient Labs for the team-card composition, Metalab's Uber case study for case-study structure. References guide patterns, not copied assets or claims.
- Keep the two logo rows: AI models first, engineering tools second. Their pixel travel speeds match even though their track widths differ.
- The blueprint animation reverses on upward scroll. The user tried and reverted a completed-state lock.
- Viewport entrances run once per page visit and release their transforms when finished so hover still works. Respect reduced motion and keyboard access; keep content usable without JS.
- Selected Work uses whole-card fade-and-rise, not separate image wipes. The figures below Team also use simple fade-and-rise.
- Team cards are four across on desktop, two on tablet, one on phone. Entire cards are links; preserve their green hover highlight and lift. All four temporarily point to `https://www.linkedin.com/in/shafaafhossain/`, as the user explicitly requested. No separate LinkedIn or X icons.
- Toronto, New York, Dubai and Dhaka are work locations, not a claim of four official offices. Existing footer addresses were retained by the user; avoid silently replacing them.
- Preserve the light design. The archived dark fantasy-style site and the early paper/serif layout were rejected.

## Skills

Use a frontend/design skill only when the user names it in the current request, and use only that design skill for that request. A visual request alone does not activate a skill. Process/support skills such as Agentation and documentation work are separate. User instructions override skill defaults: the approved varied scroll entrances intentionally differ from taste's default prohibition on repeated viewport reveals.

The complete project skill catalogue and installation notes are in [docs/skills.md](docs/skills.md). Keep that catalogue current when the project's skill setup changes; preserve `skills-lock.json` provenance rather than inventing hashes.

## Content and release accuracy

- Preserve real names, roles, photographs and supplied quotations. Use [PRODUCT.md](PRODUCT.md) to distinguish confirmed facts from placeholders and pending approvals.
- Five homepage metrics are marked `data-placeholder`; the generator's warning is intentional. Do not describe them as verified results. RaLHF's generated case study still has no results or quote, while the homepage contains a user-supplied quote and placeholder figures.
- Use sentence case and plain English; no em dashes in site copy. Real people use their real photographs.
- Keep client-image and quotation approval questions recorded in PRODUCT.md. The repository remains private. Treat actual user publication instructions according to the authorised scope, rather than claiming deployment resolves those approvals.
- The Book a call action currently uses `mailto:hello@oplusdojo.com`, not a booking service.
- Report build, browser and taste-gate outcomes accurately. The taste gate has not passed; a successful local check is not a universal quality certification.

## Repository hygiene

Keep screenshots, recordings, temporary checks, browser profiles, generated toolbar bundles, dependencies and credentials out of commits. Screenshots and ad hoc checks belong under the ignored `lab/` directory. Keep operational documentation current when commands, source ownership, ports, skills or deployment behaviour change.
