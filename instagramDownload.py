import os
from tkinter.filedialog import askdirectory
import tkinter as tk

# pip install instagram-scraper

root = tk.Tk()
saveLocation = askdirectory(title="Save location")
root.destroy()

login = input("Login: ")
password = input("Password: ")

# Download profiles separated by space
profiles = 'profile1 profile2 profile3 profile4'

os.system(f"instagram-scraper {profiles} -d {saveLocation} -n -u {login} -p {password} --media-types image --latest")
