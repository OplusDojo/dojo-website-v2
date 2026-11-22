# Claude Code entry point

@AGENTS.md

AGENTS.md owns the shared workflow, design constraints and skill-invocation policy. Read its linked documents when the relevant task requires them.

Claude-specific setup:

- Project frontend skills live globally under `~/.agents/skills/`, with Claude aliases under `~/.claude/skills/`; the project-local skill folders are empty.
- The eight design skills listed in [docs/skills.md](docs/skills.md) were verified on November 22, 2026 with `disable-model-invocation: true`. Recheck this frontmatter after skill updates. Repository instructions still govern explicit use even if an agent ignores that flag.
- `.claude/settings.json` disables the automatically loading frontend-design and nateherk-design plugins for this project. Preserve that configuration.
- Impeccable is installed as a skill, not as an enabled project hook suite. Enable hooks only when requested.
- Agentation uses the preview's existing HTTP server at localhost:4747. Client configuration and end-to-end verification are described in [development instructions](docs/development.md).

Keep project policy in AGENTS.md and detailed setup in docs/, rather than duplicating them here.
