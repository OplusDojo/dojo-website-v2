"""Local preview with automatic page generation and browser refresh."""
import json
import atexit
from pathlib import Path
import subprocess
import sys
import threading
import time
from urllib.request import urlopen
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parent
state = {"version": 0, "error": None}
lock = threading.Lock()

CLIENT = b"""<script>
(() => {
  let version;
  const key = '__dojo_scroll:' + location.pathname;
  const saved = sessionStorage.getItem(key);
  if (saved !== null) {
    sessionStorage.removeItem(key);
    addEventListener('load', () => requestAnimationFrame(() => scrollTo(0, +saved)));
  }
  async function check() {
    try {
      const next = await fetch('/__dev/version', {cache: 'no-store'}).then(r => r.json());
      if (next.error) console.error('[preview]', next.error);
      if (version !== undefined && next.version !== version) {
        sessionStorage.setItem(key, scrollY);
        location.reload();
        return;
      }
      version = next.version;
    } catch (_) { /* Retry while the preview server restarts. */ }
    setTimeout(check, 700);
  }
  check();
})();
</script>"""
CLIENT += b'<script src="/__dev/agentation.js" defer></script>'


def build_toolbar():
    subprocess.run([
        str(ROOT / 'node_modules/.bin/esbuild'), str(ROOT / 'agentation-preview.jsx'),
        '--bundle', '--minify', '--format=iife', '--define:process.env.NODE_ENV="development"',
        '--outfile=' + str(ROOT / '.agentation/toolbar.js'),
    ], cwd=ROOT, check=True)


def start_feedback_server():
    def healthy():
        try:
            with urlopen('http://localhost:4747/health', timeout=1) as response:
                return response.status == 200
        except OSError:
            return False
    if healthy():
        print('Using existing Agentation server on localhost:4747', flush=True)
        return
    process = subprocess.Popen([
        'node', str(ROOT / 'node_modules/agentation-mcp/dist/cli.js'), 'server',
    ], cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)
    def stop():
        process.terminate()
        process.wait(timeout=5)
    atexit.register(stop)
    for _ in range(40):
        if healthy():
            return
        if process.poll() is not None:
            break
        time.sleep(0.1)
    raise RuntimeError('Agentation server did not start on localhost:4747')


def snapshot():
    files = {}
    for folder in (ROOT, ROOT / "work", ROOT / "assets", ROOT / "lab/gen"):
        entries = folder.iterdir() if folder == ROOT else folder.rglob('*')
        for file in entries:
            if not file.is_file() or file.name.startswith('.') or file.suffix in ('.pyc', '.tmp') or '_index.tmp' in file.name:
                continue
            info = file.stat()
            files[file] = (info.st_mtime_ns, info.st_size)
    return files


def build():
    for script in ('build.py', 'cases.py'):
        subprocess.run([sys.executable, str(ROOT / 'lab/gen' / script)], cwd=ROOT, check=True)


def watch():
    previous = snapshot()
    while True:
        time.sleep(0.5)
        try:
            current = snapshot()
            if current == previous:
                continue
            changed = {p for p in current.keys() | previous.keys() if current.get(p) != previous.get(p)}
            if ROOT / 'agentation-preview.jsx' in changed:
                build_toolbar()
            if any(ROOT / 'lab/gen' in p.parents or ROOT / 'assets/team' in p.parents for p in changed):
                build()
            previous = snapshot()
            with lock:
                state.update(version=state['version'] + 1, error=None)
            print('Updated preview', flush=True)
        except Exception as error:
            previous = current
            with lock:
                state['error'] = str(error)
            print(f'Preview build failed: {error}', flush=True)


class Preview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        if self.path.split('?')[0] == '/__dev/agentation.js':
            data = (ROOT / '.agentation/toolbar.js').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/javascript; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        if self.path.split('?')[0] == '/__dev/version':
            with lock:
                data = json.dumps(state).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()

    def send_head(self):
        file = Path(self.translate_path(self.path))
        if file.is_dir():
            file = file / 'index.html'
        if file.suffix == '.html' and file.is_file():
            import io
            data = file.read_bytes().replace(b'</body>', CLIENT + b'</body>')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return io.BytesIO(data)
        return super().send_head()

    def log_message(self, format, *args):
        if self.path.split('?')[0] != '/__dev/version':
            super().log_message(format, *args)


if __name__ == '__main__':
    build()
    build_toolbar()
    server = ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1]) if len(sys.argv) > 1 else 4500), Preview)
    start_feedback_server()
    threading.Thread(target=watch, daemon=True).start()
    print(f'Live preview: http://localhost:{server.server_port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
