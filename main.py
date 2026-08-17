import os
import sys
import time
import pyautogui
import keyboard

# Failsafe: Moving the mouse to the top-left corner (0,0) aborts the script
pyautogui.FAILSAFE = True

# Start Hotkey
START_KEY = "f8"


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Target image paths
VORTEX_BTN = resource_path("vortex_manual.png")
SLOW_BTN = resource_path("slow_download.png")


def find_button_with_retries(image_path, button_name, max_retries=3, delay_between=2.0):
    """
    Searches for the target image on screen with retry logic and error protection.
    """
    for attempt in range(1, max_retries + 1):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location is not None:
                return location
        except Exception:
            pass

        if attempt < max_retries:
            print(f"[!] {button_name} not detected ({attempt}/{max_retries}). Retrying in {delay_between}s...")
            time.sleep(delay_between)

    return None


print("=" * 60)
print(" Nexus Mods & Vortex Auto-Downloader ")
print("=" * 60)
print(f"[*] Ready. Press [{START_KEY.upper()}] to start the automation.")
print("[*] Emergency Stop: Move mouse cursor to the top-left corner.")
print("=" * 60)

# Wait until the user presses the start key
keyboard.wait(START_KEY)
print(f"\n[+] [{START_KEY.upper()}] pressed! Starting download routine...\n")

counter = 1

try:
    while True:
        # --- STEP 1: Search for Vortex "Download Manually" Button ---
        vortex_pos = find_button_with_retries(
            VORTEX_BTN, "Vortex 'Download Manually'", max_retries=3, delay_between=2.0
        )

        if vortex_pos is None:
            print("\n[-] Vortex button not found after 3 attempts. Exiting.")
            break

        vx, vy = pyautogui.center(vortex_pos)
        print(f"[{counter}] Vortex: 'Download Manually' clicked.")
        pyautogui.click(vx, vy)

        # Wait for the browser tab to load
        time.sleep(1)

        # --- STEP 2: Search for Browser "Slow Download" Button ---
        slow_pos = find_button_with_retries(
            SLOW_BTN, "Browser 'Slow Download'", max_retries=3, delay_between=2.0
        )

        if slow_pos is None:
            print("\n[-] 'Slow Download' button not found after 3 attempts. Exiting.")
            break

        sx, sy = pyautogui.center(slow_pos)
        print(f"[{counter}] Browser: 'Slow Download' clicked.")
        pyautogui.click(sx, sy)

        # Wait for countdown to finish and Vortex to regain focus
        print(f"[{counter}] Download triggered. Waiting 6s for countdown & Vortex focus...")
        time.sleep(6)

        print(f"[{counter}] Round completed. Checking next mod...\n")
        counter += 1

except KeyboardInterrupt:
    print("\n[!] Program interrupted by user.")
except pyautogui.FailSafeException:
    print("\n[!] Failsafe triggered: Mouse moved to top-left corner. Exiting.")

input("\nPress Enter to exit...")