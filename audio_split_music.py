# 모듈 로딩 후 오디오 추출
# https://zulko.github.io/moviepy/getting_started/audioclips.html
import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube 
from pydub import AudioSegment
import subprocess

# 사용중지
def NEW_Youtube_download_mp4(url):
    print("YTSTART")
    # DOWNLOAD_FOLDER = "data"
    Video_download = YouTube(url)
    videos = Video_download.streams.filter(only_audio = True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input("enter: "))
    videos[strm].download()
    print("su")

    # Video_download = Video_download.streams.get_highest_resolution()
    # Video_name = Video_download.title
    # video_ds =  Video_download.vid_descr
    # # Video_name = Video_name[:len(Video_name)//4]+"_뒤생략"
    # print(video_ds)
    # print("YTPASS")
    # if len(Video_name) > 34:
    #     print("name_length_error")
    #     Video_name = "NEW_video"
    #     Video_download.set_filename(Video_name)
    #     Video_download.download(DOWNLOAD_FOLDER)
    #     MP4_to_MP3(Video_name)
    # Video_download.download(DOWNLOAD_FOLDER)
    # return MP4_to_MP3(Video_name)

# 첫번째 youtube 영상 다운
def Youtube_download_mp4(url):

    #youtube download link 
    DOWNLOAD_FOLDER = "data"
    Video_download = YouTube(url) 

    # 화질 up
    Video_download = Video_download.streams.get_highest_resolution()

    # 영상 제목
    Video_name = Video_download.title
    # Video_name = Video_name[:len(Video_name)//4]+"_뒤생략"
    # 영상 정보    
    Video_name = "NEW_video"

    # if len(Video_name) > 34:
    #     Video_download.download(filename = Video_name+".mp4",output_path = DOWNLOAD_FOLDER)
    #     return MP4_to_MP3(Video_name)

    Video_download.download(filename = Video_name+".mp4",output_path = DOWNLOAD_FOLDER)
    return MP4_to_MP3(Video_name)
    
# 제목 그대로
def MP4_to_MP3(Video_name):
    print("M43start")
    Video_path = "data/"+Video_name+".mp4"
    MP3_Path = "data/"+Video_name+".mp3"
    
    clip = mp.VideoFileClip(Video_path)
    
    clip.audio.write_audiofile(MP3_Path)
    
    return MP3_to_WAV(MP3_Path)

def MP4_Transfer_WAV(Video_name):
    print("MWSTART")
    Video_path = "data/"+Video_name+".mp4"
    # clip = mp.VideoFileClip(Video_path)
    WAV_path = "data/"+Video_name+".wav"
    # MP4_to_WAV(Video_path,Video_path,WAV_path)
    # clip.audio.write_audiofile(WAV_path)
    print("MWPASS")
    return WAV_Transfer_Text(WAV_path)

def MP3_to_WAV(MP3_Path):
    # Video_path = "data/"+"NEW_video.mp3"
    # # clip = mp.VideoFileClip(Video_path)
    WAV_path = MP3_Path[:-4]+".wav"
    print(MP3_Path)
    print(WAV_path)

    
    subprocess.call(['data//ffmpeg-3.4.1-win64-static//bin//ffmpeg.exe', '-i', MP3_Path,WAV_path])
    
    # audSeg = AudioSegment.from_mp3(MP3_Path)
    # print(audSeg)
    # audSeg.export("data/NEW_video.wav", format="wav")
    # clip.audio.write_audiofile(WAV_path)
    
    return WAV_Transfer_Text(WAV_path)
    
def WAV_Transfer_Text(WAV_path):
# moviepy에서 error 
    print("WTSTART")
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    Sound_File= sr.AudioFile(WAV_path)

    with Sound_File as source:
        Sound_Before_Text = recognizer.record(source)
    
    Sound2Text = recognizer.recognize_google(audio_data=Sound_Before_Text, language="ko-KR")
    print("WTPASS")
    print(Sound2Text)
    print(Sound_Before_Text)


url = input()
Youtube_download_mp4(url)
