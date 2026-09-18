#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
: "${PREFIX:?Run from Termux}"
rm -f "$PREFIX/bin/devbox"
rm -rf "$PREFIX/lib/devbox"
echo "DevBox uninstalled."
