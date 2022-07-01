# 모듈 로딩 후 오디오 추출
# https://zulko.github.io/moviepy/getting_started/audioclips.html
import moviepy.editor as mp
import speech_recognition as sr
import os
from pydub import AudioSegment

# importing the module 
from pytube import YouTube 

DOWNLOAD_FOLDER = "data"
url = input()
Video_download = YouTube(url) 

Video_download = Video_download.streams.get_highest_resolution()
Video_name = Video_download.title
Video_download.download(DOWNLOAD_FOLDER)



clip = mp.VideoFileClip("data/"+Video_name+".mp4")
clip.audio.write_audiofile("data/audio.wav")
# moviepy에서 error 
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
Sound_File= sr.AudioFile("data/audio.wav")

with Sound_File as source:
    Sound_Before_Text = recognizer.record(source)

Sound2Text = recognizer.recognize_google(audio_data=Sound_Before_Text, language="ko-KR")
print(Sound2Text, Sound_Before_Text)