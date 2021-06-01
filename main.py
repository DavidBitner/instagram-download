import os
from tkinter.filedialog import askdirectory
import tkinter as tk

options = ['1 - Posts', '2 - IGTV', '3 - Fast Update']
for o in options:
    print(o)
option = int(input('Option: '))
root = tk.Tk()
directory = askdirectory(title="Save location")
root.destroy()
while True:
    profile = input("Profile name: [0 to end] @")
    if profile == '0':
        break
    dirname = f'--dirname-pattern={directory}/@{profile}'
    if option == 1:
        os.system(f"instaloader {dirname} --no-videos --no-captions --no-metadata-json --no-compress-json {profile}")
    elif option == 2:
        os.system(f"instaloader {dirname} --igtv --no-posts --no-captions --no-metadata-json --no-compress-json {profile}")
    elif option == 3:
        os.system(f"instaloader {dirname} --fast-update --no-videos --no-captions --no-metadata-json --no-compress-json {profile} ")
