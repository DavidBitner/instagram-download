import os
from tkinter.filedialog import askdirectory
import tkinter as tk

directory = askdirectory(title="Escolha onde salvar")
root = tk.Tk()
root.withdraw()
while True:
    profile = input("Profile name: [0 to end] @")
    if profile == '0':
        break
    dirname = f'--dirname-pattern={directory}/@{profile}'
    os.system(f"instaloader {dirname} --fast-update --no-videos --no-captions --no-metadata-json --no-compress-json {profile}")
