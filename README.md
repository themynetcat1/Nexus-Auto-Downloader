# Nexus Mods & Vortex Auto-Downloader

A lightweight Python quality-of-life (QoL) automation tool designed to streamline downloading mod collections and long mod lists via Vortex and Nexus Mods without manual clicking.

---

## Features
- **Visual Detection:** Automatically detects interface buttons on screen via OpenCV image recognition.
- **Fail-Safe & Smart Retries:** Retries 3 times with 2-second intervals before cleanly exiting if a button is not found.
- **Global Hotkey:** Press `F8` anywhere to start the automation loop.
- **Instant Abort:** Move your mouse to the top-left corner of the screen (`0,0`) to trigger the failsafe and stop immediately.

---

## Quick Start (No Python Required)

1. Download the latest **`NexusAutoDownloader_Portable.zip`** from the [Releases](../../releases) tab.
2. Extract the ZIP archive anywhere on your PC.
3. Open **Vortex** and prepare your mod download queue.
4. Double-click **`Launch.bat`**.
5. Press **`F8`** to start downloading.

*(The portable release runs on an embedded Python environment. No installation, PATH configuration, or admin privileges needed.)*

---

## Running from Source (For Developers)

### Prerequisites
- Python 3.8+
- Any modern web browser (Opera, Chrome, Edge, Brave, Firefox, etc.)

### Installation
1. Clone or download this repository.
2. Ensure `vortex_manual.png` and `slow_download.png` are in the root directory alongside `main.py`.
3. Double-click **`run.bat`** (or manually run `pip install -r requirements.txt` followed by `python main.py`).
4. Press **`F8`** to begin.

---

## Why Not a Standalone `.exe`?
Standalone compiled binaries (`.exe` via PyInstaller) that hook global keyboard events (`keyboard`) and simulate input (`pyautogui`) are frequently flagged as false-positives by Windows Defender and antivirus engines. Providing an open-source portable environment ensures 100% transparency, safety, and reliability.

---

## License
Distributed under the **MIT License**. See `LICENSE` for more information.
