# Vercel deployment

## Existing destination

Verified November 22, 2026:

- Production alias: https://oplusdojo.vercel.app
- Project: `oplusdojo`
- Scope: `op-lus-dojo` (OPlusDojo)
- Project ID: `prj_dPrSAIHpJUOV9Sm4WcY7VulKuRX9`
- Root directory: `.`; framework preset: Other.
- No Git repository is connected. Pushing main does not deploy it automatically.

The last verified deployment was commit `6ace7bd`, deployment `dpl_2E8cw7eRdZn22koHHbtF9g9AQRoJ`. The subsequent team-card commit `c9a1ae3` is on main but has not been deployed. These hashes refer to the original sample-oplus-dojo repository before the v2 import; v2 starts a fresh Git history. They are dated observations, not an automatically updated status feed.

Reuse this project for authorised deployments. Do not substitute the neighbouring dojo-website project's build configuration or create a new project/URL.

## Prepare the committed static site

Deploy only when the user requests deployment. Inspect branch, status and remote, and make sure the requested site changes are committed on main. Build changes before committing them. A push request alone is not a deployment request.

The proven approach stages only committed runtime files in a temporary directory. It excludes the local preview, Agentation toolbar source, generators, archived experiments, screenshots, dependencies and account credentials. Run the following from the repository root:

```bash
export OPLUS_DEPLOY_DIR="$(mktemp -d -t oplusdojo-deploy)"
python3 - <<'PY'
import json, os, subprocess
from pathlib import Path
out = Path(os.environ['OPLUS_DEPLOY_DIR'])
base = 'builds/oplusdojo/'
files = subprocess.check_output(
    ['git', 'ls-tree', '-r', '--name-only', 'HEAD', base], text=True).splitlines()
for name in files:
    rel = name[len(base):]
    path = Path(rel)
    runtime_folder = rel.startswith(('assets/', 'work/')) and path.suffix != '.md'
    runtime_root = len(path.parts) == 1 and path.suffix in ('.html', '.css', '.js')
    if runtime_folder or runtime_root:
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(subprocess.check_output(['git', 'show', 'HEAD:' + name]))
(out / 'vercel.json').write_text(json.dumps({
    'framework': None, 'buildCommand': None,
    'installCommand': None, 'outputDirectory': '.'
}))
(out / '.vercelignore').write_text('.env*\n.git/\nnode_modules/\n')
print('Staged committed site:', out)
PY
```

Inspect the staged content before publishing. It should contain index.html, the current CSS/JS, assets/ and work/, with no dev toolbar injection.

## Deploy and verify

Use the existing authenticated Vercel CLI session; do not print auth files or tokens:

```bash
npx --yes vercel@latest whoami
npx --yes vercel@latest project inspect oplusdojo --scope op-lus-dojo
cd "$OPLUS_DEPLOY_DIR"
npx --yes vercel@latest link --yes --project oplusdojo --scope op-lus-dojo
npx --yes vercel@latest deploy --prod --yes --scope op-lus-dojo
```

Linking may create .env.local and project metadata in the temporary folder. Keep environment files excluded and leave credentials out of the repository. The staged site has no package.json and needs no remote installation or build step.

Completion means Vercel reports READY for the production target and assigns the existing production alias. Verify the alias itself, not only the unique deployment URL:

- Homepage and current motion CSS/JS return successfully and match the committed files.
- All three case study URLs load: /work/elora.html, /work/tenera.html, /work/ralhf.html.
- Development hot-reload and Agentation scripts are absent.
- Report the deployed commit and stable URL. Update the dated deployment record in this file and README when it changes.

If access protection intercepts checks, use Vercel's authenticated curl/inspect commands without weakening the project's protection settings. Last deployment metadata listed Vercel Authentication; the stable alias returned the actual site to the verification requests. Verify current behaviour rather than assuming either public access or protection.
