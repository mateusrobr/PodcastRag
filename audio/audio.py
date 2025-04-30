from pytubefix import YouTube
from pytubefix.cli import on_progress

from pydub import AudioSegment



def get_audio_file(url):
    yt = YouTube(url,on_progress_callback=on_progress)
    filename = yt.title.replace(" ", "_")
    ys = yt.streams.get_audio_only()
    ys.download(output_path="./audio",filename=filename)


def convert_m4a_wav(filename):
    wav_filename = 'output.wav'
    sound = AudioSegment.from_file(filename, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')






