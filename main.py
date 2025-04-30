from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=PGUdWfB8nLg"

yt = YouTube(url, on_progress_callback=on_progress)

caption = yt.captions['a.en']
caption.save_captions("captions.txt")