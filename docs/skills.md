# Project skills

Verified locally on November 22, 2026. This is the project-relevant catalogue, not an inventory of unrelated account-wide skills.

## Invocation and precedence

The user selects frontend/design skills explicitly for the current request. Use that one design skill; do not combine design systems implicitly. Support skills such as Agentation, documentation and code review serve different tasks. The user's current instructions and approved decisions win over a skill's default aesthetic rules.

In particular, the user rejected a largely static interpretation of taste and explicitly requested varied Codegent-style scroll entrances. Preserve that decision. They subsequently chose simpler entrances for Selected Work and the team figures. Taste's gate is diagnostic evidence, not permission to redesign retained sections or claim the gate passed.

## Design catalogue

`skills-lock.json` records upstream sources, skill paths and recorded hashes for these eight design skills. It does not automatically prove the current installed files match those hashes.

| Skill | Project use | Upstream |
|---|---|---|
| `scroll-craft` (user alias: scrollcraft) | Original page planning, scroll engine and signature blueprint/map work | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) |
| `frontend-design` | Original visual direction and section design | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| `design-taste-frontend` (taste) | Selected typography, testimonial cards and motion guidance; assets/motion is vendored from it | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `impeccable` | Available commands for interface audits, polish, layout and related design passes | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| `better-ui` | Available surface, alignment, icon and micro-interaction polish | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) |
| `ui-ux-pro-max` | Available searchable styles, palettes, fonts, UX rules and stack guidance | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| `animate` | Available motion implementation workflow; distinct from Impeccable's animate command | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| `copywriting` | Available marketing-copy workflow, subject to PRODUCT.md's evidence constraints | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) |

“Available” does not mean it was applied to the current design. The supplied skill instructions describe their current workflows; consult the selected skill before using it rather than treating this table as its full specification.

## Support skills

| Skill | Use |
|---|---|
| `agentation` | Development toolbar and live feedback connection. Inspect the existing mount/endpoint, verify actual annotation delivery, and resolve addressed notes. See development.md. |
| `writing-for-agents` | Maintaining AGENTS.md, CLAUDE.md and documentation reached by agent instructions. Shared rules have one owner; detailed setup is linked on demand. |

Both support skills are installed globally and have Claude aliases. They are not entries in this repository's design-skill lockfile; do not fabricate provenance or computed hashes for them. Other globally available process skills are not project dependencies unless a task invokes them.

## Installation and agent configuration

The ten skills above were verified at `~/.agents/skills/<name>/SKILL.md`, with symlinks at `~/.claude/skills/<name>`. Project-local `.agents/skills/` and `.claude/skills/` are empty; skill code is not committed here.

For each design skill on a new machine, take the source from skills-lock.json:

```bash
npx skills add <source> --skill <name> -g --agent claude-code codex
```

Check the installed skill and agent alias after installation. All eight design SKILL.md files currently include `disable-model-invocation: true`; Agentation and writing-for-agents do not. Recheck after updates, which can change frontmatter or behaviour. Explicit-use repository policy applies regardless of an agent's support for that frontmatter.

Claude's project settings disable the automatically loading frontend-design and nateherk-design plugins. Impeccable was installed as a plain skill; its plugin hook suite is not enabled. Read CLAUDE.md before changing those settings.

For ui-ux-pro-max, the local search script is available directly if plugin environment variables are absent:

```bash
python3 ~/.agents/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>
```

## References and limits

- Baseten: initial colour/layout reference.
- Codegent: user-selected variety and pacing of entrances.
- Gradient Labs: user-selected portrait-card composition.
- Metalab's Uber work page: case-study structure reference.

Borrow interaction and composition ideas while retaining O+Dojo's real content, photographs, branding and current user decisions. A reference site's staff photos, biographies and claims are not assets for this project.
