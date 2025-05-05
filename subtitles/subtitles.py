from pytubefix import YouTube
from pytubefix.cli import on_progress

from pydub import AudioSegment
import re



def get_subtitles(url,caption_code="a.en"):
    yt = YouTube(url,on_progress_callback=on_progress)
    title = yt.title
    channel_id = yt.channel_url
    captions = yt.captions[caption_code]
    print(captions.code)
    srt_subtitles = captions.generate_srt_captions()

    podcast_dict = {}
    podcast_dict["title"] = title
    podcast_dict["channel_url"] = channel_id
    podcast_dict["srt_subtitle"] = srt_subtitles

    return podcast_dict


def parse_srt_string(srt_text):
    blocks = re.split(r'\n{2,}', srt_text.strip())
    parsed_text = []

    for block in blocks:
        lines = block.strip().split('\n')
        id = lines[0]
        timestamp = lines[1]
        subtitle = lines[2]
        parsed_text.append([id,timestamp,subtitle])

    return parsed_text

def group_subtitle_texts(srt_parsed):
    all_subs = ""
    for lines in srt_parsed:
        all_subs += lines[2]

    return all_subs

    







