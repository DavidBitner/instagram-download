import instaloader
from tkinter.filedialog import askdirectory
import tkinter as tk

root = tk.Tk()
directory = askdirectory(title="Save location")
root.destroy()

login_username = input('Enter Instagram Login:')
profile_download = ''

L = instaloader.Instaloader(download_videos=False,download_video_thumbnails=False,
save_metadata=False,request_timeout=30000.0,dirname_pattern=f'{directory}/@{profile_download}')

L.interactive_login(login_username)

L.download_profile(profile_download)
