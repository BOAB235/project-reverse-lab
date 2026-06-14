#!/usr/bin/env python3
# proxy.py - tiny local CORS proxy for the oscilloscope HTML page
# Run:  python proxy.py
# Then in the HTML keep "Use local proxy" enabled (default ON).
#
# ============================================================================
# DEPENDENCIES / PORTABILITY  ->  NOTHING TO INSTALL  (pip install = NONE)
# ============================================================================
# Requires only:  Python >= 3.6   (tested on 3.13.5)
#
# ALL modules below ship INSIDE Python itself (the "standard library").
# They are NOT on PyPI and must NOT be pip-installed. Trying to do so fails,
# e.g. `pip install http.server` -> ERROR (no such package). This is normal
# and is exactly why this proxy is 100% reproducible on any machine that has
# Python: there are zero third-party versions to pin or break.
#
#   module            pip package?   notes
#   ----------------  -------------  -----------------------------------------
#   http.server       (built-in)     HTTP server base classes
#   http.client       (built-in)     IncompleteRead exception
#   socketserver      (built-in)     ThreadingTCPServer
#   urllib.request    (built-in)     outbound HTTP to the scope
#   urllib.parse      (built-in)     URL parsing / query decoding
#   socket            (built-in)     timeout handling
#   sys               (built-in)     stderr logging
#
# To verify on any machine:   python -c "import http.server, socketserver, \
#   urllib.request, urllib.parse, http.client, socket, sys; print('OK')"
#
# (Optional) freeze the interpreter version for a teammate:
#   python --version            -> e.g. "Python 3.13.5"
#   No requirements.txt is needed because there are no PyPI dependencies.
# ============================================================================

import http.server, socketserver, urllib.request, urllib.parse, http.client, socket, sys

PORT = 8765   # must match "Proxy port" in the HTML

class Proxy(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_GET(self):
        q = urllib.parse.urlparse(self.path).query
        target = urllib.parse.parse_qs(q).get('u', [None])[0]
        if not target:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'missing ?u='); return
        try:
            r = urllib.request.urlopen(target, timeout=10)
            ct = r.headers.get('Content-Type', 'application/octet-stream')
            # The scope often advertises a wrong Content-Length and then closes
            # the socket early (IncompleteRead) or stops sending (read timeout).
            # In every case the bytes already received ARE the complete reply,
            # so we read in chunks and keep whatever arrives.
            chunks = []
            try:
                while True:
                    b = r.read(4096)
                    if not b:
                        break
                    chunks.append(b)
            except http.client.IncompleteRead as ir:
                chunks.append(ir.partial)
            except (socket.timeout, TimeoutError):
                pass
            data = b''.join(chunks)
            self.send_response(200)
            self.send_header('Content-Type', ct)
            self.send_header('Content-Length', str(len(data)))
            self._cors(); self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(502); self._cors(); self.end_headers()
            try:
                self.wfile.write(str(e).encode())
            except Exception:
                pass

    def log_message(self, fmt, *args):
        sys.stderr.write("[proxy] %s - %s\n" % (self.address_string(), fmt % args))

with socketserver.ThreadingTCPServer(('127.0.0.1', PORT), Proxy) as srv:
    print(f"CORS proxy listening on http://127.0.0.1:{PORT}/   (Ctrl+C to stop)")
    srv.serve_forever()
