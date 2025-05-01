from pytubefix import YouTube
from pytubefix.cli import on_progress

from pydub import AudioSegment



def get_subtitles(url):
    yt = YouTube(url,on_progress_callback=on_progress)
    captions = yt.captions["a.pt"]

    srt_subtitles = captions.generate_srt_captions()
    return srt_subtitles


def convert_m4a_wav(filename):
    wav_filename = 'output.wav'
    sound = AudioSegment.from_file(filename, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')






