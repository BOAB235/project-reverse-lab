# Oscilloscope Capture

Capture **screenshots** and **signal data (CSV)** from a Tektronix **TDS 3000 series**
oscilloscope (tested on a **TDS 3034B**) over its built-in **HTTP/Ethernet server** —
no special drivers, no NI-VISA, no USB.

There are two ways to use it:

| Version | Folder | Needs | Best for |
|---|---|---|---|
| **HTML app** (recommended) | `html_version/` | Python (for a tiny helper proxy) + a browser | Everyday use, nice UI, click-to-save |
| **Python scripts** | `python_version/` | Python + `requests` | Automation / scripting |

---

## What it does

- Grabs the live **screen image** from the scope (`Image.png`).
- Reads the **waveform** of the active channels and saves it as a **CSV**
  (`time, CH1, CH2, …` or a compact `CH1, CH2, …, Ts` form).
- Optionally adds a **parameters block** to the CSV: timebase, trigger, per-channel
  settings (scale, position, coupling, impedance, bandwidth, probe…), the on-screen
  **measurements** (MEAS1–4), and **cursor** values.
- **Read-only**: it never changes the scope. If the scope is running it stays running;
  if it is stopped/triggered it stays stopped. Nothing is forced back to RUN.

---

## HTML app (recommended)

Files in `html_version/`:

- `oscillo.html` — the app (settings, capture buttons, log). All settings are saved
  in the browser (localStorage), so they are remembered next time.
- `proxy.py` — a tiny **local CORS proxy**. **Nothing to install** — it uses only the
  Python standard library (works on any Python ≥ 3.6).
- `start_oscillo.bat` — Windows one-click launcher (starts the proxy + opens the page).
- `start_oscillo.sh` — Linux/macOS launcher.

### Quick start (Windows)

1. Connect the scope by Ethernet and note its **IP** (scope menu → *Utility → I/O*).
2. Double-click **`start_oscillo.bat`**.
   - A small minimized window "Oscillo Proxy" opens (leave it running).
   - The page `oscillo.html` opens in your browser.
3. Enter the **Scope IP** (and subnet mask), click **Test connection** — the LED next
   to the button turns green when the scope answers.
4. Tick what you want — **Image**, **Signal**, **Signal + parameters** — then click **Save**.

> When you are done, just close the "Oscillo Proxy" window.

### Quick start (Linux/macOS)

```bash
cd html_version
./start_oscillo.sh
```

### Why is a proxy needed? (CORS)

The scope's web server does **not** send the `Access-Control-Allow-Origin` header, so a
browser is **not allowed** to read its responses directly (this is a browser security
rule, not a bug). The tiny `proxy.py` runs on your own machine (`127.0.0.1:8765`),
relays requests to the scope, and adds the missing header so the browser can read the
data. It also works around a scope quirk where it reports a wrong `Content-Length` and
closes the connection early.

**Only one proxy at a time** — if you launched it with the `.bat`, don't start a second
one (you'll get a "port already in use" error).

### Save location

- **Choose working folder** → files are written straight into that folder. Because the
  browser writes them silently (File System Access API), they do **not** appear in the
  download bar — that's a browser limitation.
- **Browser default (Downloads)** → every file appears in the **download bar** at the top,
  so you can click to open the file or its folder.

You get one or the other, never both for the same file.

### Time column option

- **Full time array** → CSV has a `time` column (`time, CH1, CH2, …`).
- **Ts only (smaller file)** → CSV is `CH1, CH2, …, Ts`, where the sample period **Ts**
  is written **once** on the first row. Rebuild time later with `time[i] = i * Ts`.
  This makes the file smaller because the time column is not repeated.

---

## Python scripts

Files in `python_version/`:

- `screen_shot_and_Signal_V6.py` — captures the image **and** the signal CSV.
- `screen_shot_V1.py` — captures the screenshot only.

These talk to the scope directly with the `requests` library (no browser, no proxy).

### Install

```bash
pip install requests==2.32.5
pip install "urllib3<2"
```

(Pinned versions known to work with the scope's HTTP server.)

### Run

```bash
cd python_version
python screen_shot_and_Signal_V6.py
```

Edit the IP address near the top of the script to match your scope.

---

## How it talks to the scope (technical)

The scope exposes a SCPI bridge at `http://<scope-ip>/Comm.html`. The app/scripts send
short, safe SCPI queries (`*IDN?`, `WFMPRE?`, `CURVE?`, channel/trigger settings, on-screen
measurements, cursors) and parse the plain-text reply.

The waveform is converted to volts with the scope preamble:

```
volts = (raw - y_offset) * y_mult + y_origin
time  = index * x_increment        # x_increment = Ts
```

**Important:** only short, read-only commands are used. Sending a very large GET (e.g. a
full setup string) can crash the scope's web server, so that is deliberately avoided.

---

## Requirements

- A Tektronix TDS 3000 series scope with the Ethernet/HTTP option, reachable on your network.
- **HTML app:** any modern browser + Python ≥ 3.6 (for the proxy; nothing to `pip install`).
  Folder picker and silent-folder save are Chrome/Edge only; other browsers fall back to
  the normal Downloads bar.
- **Python scripts:** Python with `requests` (and `urllib3 < 2`).

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| "Failed to fetch" / red LED | Make sure `proxy.py` is running (use `start_oscillo.bat`) and "Use local proxy" is ticked. |
| "Port already in use" | A proxy is already running — don't start a second one. |
| Test connection stays not-tested | Check the scope IP/mask, cable, and that the scope's HTTP server is enabled. |
| No download bar when a folder is chosen | Expected — the browser writes silently to the chosen folder. Use "reset" to go back to Downloads if you want the bar. |
| Capture is slow | Untick **Signal + parameters** — reading all settings/measurements is the slow part. Plain **Signal** is fast. |
