# O+Dojo website v2

A static marketing site for O+Dojo's AI and cloud engineering services. Its purpose is to win clients, projects and investor confidence by showing experienced engineers who own systems through production. The main action is **Book a call**.

Repository: [OplusDojo/dojo-website-v2](https://github.com/OplusDojo/dojo-website-v2) (private).

Work on the website in `builds/oplusdojo/`. This repository was imported from `shafaaf/sample-oplus-dojo` at site revision `c9a1ae3`, including the updated documentation. It starts a fresh Git history. The neighbouring `../dojo-website/` is a separate project.

## Local preview

```bash
cd builds/oplusdojo
npm ci
npm run dev -- 9500
```

Open [localhost:9500](http://localhost:9500/). The preview rebuilds generated pages, refreshes the browser and restores scroll position. Agentation appears at bottom right and syncs to `http://localhost:4747`. Running `npm run dev` without a port uses 4500.

## Current experience

- White canvas, black text, green highlights and graphics, blue brand logo.
- Hero: “AI systems built for production.” Credentials: Amazon, Meta, Slack and BlackBerry.
- Two continuously scrolling logo rows with matched travel speeds and opposing entrance wipes.
- Services, the reversible “Concept to production, in four revisions” blueprint, three case studies, team, figures, testimonials and a closing call to action.
- Four linked portrait cards across desktop, two columns on tablet and one on phone. Green highlight and lift on hover; no separate social icons. All four currently open the owner's LinkedIn as explicitly requested.
- Varied viewport entrances inspired by Codegent. Selected Work and the team figures retain the simpler fade-and-rise treatment selected through Agentation.
- A black footer containing the connected location map and contact/address information. The map draws connections as the visitor approaches the bottom of the page.

The cities represent where people work, not four official offices. Existing footer addresses remain part of the approved layout; see [product context](PRODUCT.md) for unresolved content details.

## Editing

The homepage and case studies are generated. Edit their sources and rebuild:

```bash
cd builds/oplusdojo
python3 lab/gen/build.py
python3 lab/gen/cases.py
```

Commit generated HTML with its sources. See [AGENTS.md](AGENTS.md) for the file ownership map and shared working rules.

## Documentation

| Document | Use it for |
|---|---|
| [PRODUCT.md](PRODUCT.md) | Audience, positioning, factual evidence and outstanding content approvals |
| [AGENTS.md](AGENTS.md) | Shared agent instructions, design constraints and source files |
| [CLAUDE.md](CLAUDE.md) | Claude-specific entry point importing the shared instructions |
| [Development](docs/development.md) | Hot reload, Agentation, motion behaviour and visual checks |
| [Skills](docs/skills.md) | All project-relevant design and support skills, installation and precedence |
| [Deployment](docs/deployment.md) | Existing Vercel project, static upload procedure and verification |
| [Asset credits](builds/oplusdojo/assets/CREDITS.md) | Image provenance |
| [FINGERPRINTS.md](FINGERPRINTS.md) | Historical scroll-craft registry; append according to that skill's rules |

## Deployment status

As of November 22, 2026:

- Production URL: [oplusdojo.vercel.app](https://oplusdojo.vercel.app/).
- Last verified deployment: `6ace7bd` (homepage motion).
- Imported site revision: `c9a1ae3` in the source repository (four interactive team cards). These cards have not yet been deployed to Vercel.
- Vercel is not connected to Git; pushing `main` alone does not deploy it.

This is a dated record, not an automatic deployment indicator. Verify the current deployment before reporting its status.

## Validation and remaining content work

The motion and team-card changes were checked in headless Chrome, including desktop, tablet, phone, hover, keyboard focus and reduced motion. There is no maintained automated test suite; `npm test` is the package's placeholder command and fails intentionally.

The full taste gate has not passed. Its broad layout/copy rules conflict with several retained design choices and also identified issues outside the motion work. Five homepage metrics remain explicitly marked `data-placeholder`; the generator warns about them. These are unresolved content items, not confirmed client results. See [PRODUCT.md](PRODUCT.md).
