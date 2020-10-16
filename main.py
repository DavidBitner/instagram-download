import os

while True:
    profile = input("Profile name: [0 to end] @")
    os.system(f"instaloader --no-videos --no-captions --no-metadata-json --no-compress-json profile {profile}")
