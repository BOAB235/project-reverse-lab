#!/usr/bin/env bash
# ============================================================
#  start_oscillo.sh  (Linux / macOS)
#  One command: starts the local CORS proxy (Python stdlib only,
#  no pip install) and opens the HTML page in the default browser.
#  Usage:  chmod +x start_oscillo.sh   then   ./start_oscillo.sh
# ============================================================
cd "$(dirname "$0")" || exit 1

# Pick a python interpreter.
PY="$(command -v python3 || command -v python)"
if [ -z "$PY" ]; then
  echo "ERROR: Python 3 not found. Install python3 and retry."
  exit 1
fi

# Start the proxy in the background (stays running).
"$PY" proxy.py &
PROXY_PID=$!
echo "Proxy started (PID $PROXY_PID) on http://127.0.0.1:8765/"

# Give it a moment to bind the port.
sleep 1

# Open the page with whatever opener exists.
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "oscillo.html"
elif command -v open >/dev/null 2>&1; then   # macOS
  open "oscillo.html"
else
  echo "Open oscillo.html manually in your browser."
fi

echo "Press Ctrl+C to stop the proxy."
# Wait so Ctrl+C stops the proxy cleanly.
trap 'kill $PROXY_PID 2>/dev/null; echo; echo "Proxy stopped."; exit 0' INT
wait $PROXY_PID
