@echo off
REM ============================================================
REM  start_oscillo.bat
REM  One double-click: starts the local CORS proxy (no install
REM  needed - Python stdlib only) and opens the HTML page.
REM ============================================================
cd /d "%~dp0"

REM Start the proxy in its own minimized window (stays running).
start "Oscillo Proxy" /min python "%~dp0proxy.py"

REM Give the proxy a moment to bind the port, then open the page.
timeout /t 1 /nobreak >nul
start "" "%~dp0oscillo.html"

echo Proxy started (minimized window) and page opened.
echo Close the "Oscillo Proxy" window when you are done.
