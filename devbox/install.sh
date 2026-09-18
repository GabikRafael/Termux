#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
if [ ! -d "${PREFIX:-}/bin" ] || [ "${PREFIX:-}" != "/data/data/com.termux/files/usr" ]; then echo "DevBox must be installed from Termux (PREFIX is not Termux)." >&2; exit 1; fi
case "$(uname -m)" in aarch64|armv7l|i686|x86_64) ;; *) echo "Unsupported architecture: $(uname -m)" >&2; exit 1;; esac
command -v python >/dev/null 2>&1 || pkg install python
install -Dm755 "$ROOT/bin/devbox" "$PREFIX/bin/devbox"
install -d "$PREFIX/lib/devbox"
cp -R "$ROOT/lib" "$PREFIX/lib/devbox/"
echo "DevBox installed successfully."
devbox doctor
