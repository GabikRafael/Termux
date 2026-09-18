from pathlib import Path
try: import tomllib
except ImportError: import tomli as tomllib
def project_root(path):
    path=Path(path).resolve()
    for p in (path, *path.parents):
        if (p/'devbox.toml').exists(): return p
    return path
def load_config(root):
    f=Path(root)/'devbox.toml'
    return tomllib.loads(f.read_text()) if f.exists() else {}
