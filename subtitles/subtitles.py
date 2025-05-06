from pytubefix import YouTube
from pytubefix.cli import on_progress
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re



def get_subtitles(url,caption_code="a.pt"):
    yt = YouTube(url,on_progress_callback=on_progress)
    title = yt.title
    channel_id = yt.channel_url
    captions = yt.captions[caption_code]
    srt_subtitles = captions.generate_srt_captions()

    srt_parsed = parse_srt_string(srt_subtitles)

    grouped_subtitles = group_subtitle_texts(srt_parsed=srt_parsed)

    docs = chunk_subtitles(grouped_subtitles)

    podcast_dict = {}
    podcast_dict["title"] = title
    podcast_dict["channel_url"] = channel_id
    podcast_dict["subtitle"] = docs
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

def chunk_subtitles(subtitles):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=100,
    )

    splitted_subs = text_splitter.split_text(subtitles)
    docs = text_splitter.create_documents(splitted_subs)

    return docs

    







