import yt_dlp
import os

DOWNLOAD_PATH = "/sdcard/Download/ZUNAR_DL/"

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

def download_video(url, quality="best"):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),
        'format': quality,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
