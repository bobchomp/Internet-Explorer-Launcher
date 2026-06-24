import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def launch_in_ie():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("No URL", "Please enter a URL.")
        return
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    ie_paths = [
        r"C:\Program Files\Internet Explorer\iexplore.exe",
        r"C:\Program Files (x86)\Internet Explorer\iexplore.exe",
    ]
    ie_exe = next((p for p in ie_paths if os.path.exists(p)), None)
    if ie_exe is None:
        messagebox.showerror("Not Found", "Internet Explorer not found on this system.")
        return

    subprocess.Popen([ie_exe, url])

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

root.mainloop()
