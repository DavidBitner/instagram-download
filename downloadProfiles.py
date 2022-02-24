import os
from tkinter.filedialog import askdirectory
import tkinter as tk

login_name = ''
profiles = ["", "", ""]

root = tk.Tk()
directory = askdirectory(title="Save location")
root.destroy()

for profile in profiles:
  dirname = f'--dirname-pattern={directory}/@{profile}'
  os.system(f"instaloader {dirname} --login {login_name} --fast-update --no-videos --no-captions --no-metadata-json --no-compress-json {profile} ")

  #os.system(f"instaloader {dirname} --login {login_name} --no-videos --no-captions --no-metadata-json --no-compress-json {profile}")
