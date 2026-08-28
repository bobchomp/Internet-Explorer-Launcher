import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import urllib.request
import urllib.error
import json
import os
import tempfile

VERSION = "dev"
GITHUB_REPO = "bobchomp/Internet-Explorer-Launcher"


def check_for_updates():
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
        req = urllib.request.Request(url, headers={"User-Agent": "IELauncher"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
        latest = data.get("tag_name", "").lstrip("v")
        if VERSION == "dev" or not latest:
            return
        if tuple(int(x) for x in latest.split(".")) > tuple(int(x) for x in VERSION.split(".")):
            asset_url = next(
                (a["browser_download_url"] for a in data.get("assets", [])
                 if a["name"].endswith("-Setup.exe")),
                None,
            )
            root.after(0, lambda: show_update_dialog(latest, asset_url))
    except Exception:
        pass


def show_update_dialog(latest_version, asset_url):
    dialog = tk.Toplevel(root)
    dialog.title("Update Available")
    dialog.resizable(False, False)
    dialog.grab_set()

    frame = tk.Frame(dialog, padx=20, pady=16)
    frame.pack()

    tk.Label(frame, text=f"A newer version of IE Launcher is available (v{latest_version}).",
             wraplength=320).pack(pady=(0, 4))
    tk.Label(frame, text="Please update now.", fg="gray").pack(pady=(0, 12))

    def do_update():
        if not asset_url:
            messagebox.showerror("Error", "Could not find installer download link.")
            return
        btn.config(state="disabled", text="Downloading...")
        dialog.update()

        def download_and_run():
            try:
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix="-Setup.exe")
                tmp.close()
                urllib.request.urlretrieve(asset_url, tmp.name)
                subprocess.Popen([tmp.name])
                root.after(0, root.destroy)
            except Exception as e:
                root.after(0, lambda: messagebox.showerror("Download Failed", str(e)))
                root.after(0, lambda: btn.config(state="normal", text="Update"))

        threading.Thread(target=download_and_run, daemon=True).start()

    btn = tk.Button(frame, text="Update", command=do_update, padx=10, pady=4)
    btn.pack()


def launch_in_ie():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("No URL", "Please enter a URL.")
        return
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        import win32com.client
        ie = win32com.client.Dispatch("InternetExplorer.Application")
        ie.Visible = True
        ie.Navigate(url)
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch Internet Explorer:\n{e}")


root = tk.Tk()
root.title("IE Launcher")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

tk.Label(frame, text="URL:").grid(row=0, column=0, sticky="w", pady=(0, 6))
url_entry = tk.Entry(frame, width=48)
url_entry.insert(0, "https://example.com")
url_entry.grid(row=0, column=1, padx=(6, 0), pady=(0, 6))

btn = tk.Button(frame, text="Open in Internet Explorer", command=launch_in_ie,
                padx=8, pady=4)
btn.grid(row=1, column=0, columnspan=2, pady=(6, 0))

url_entry.bind("<Return>", lambda e: launch_in_ie())

threading.Thread(target=check_for_updates, daemon=True).start()

root.mainloop()
