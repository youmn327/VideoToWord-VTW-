import subprocess
import os
def MP4_to_WAV(MP4_item,this_path,save_file_id):
    print("NMWENTER")
    command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(MP4_item, os.path.join(this_path, save_file_id))
    subprocess.call(command, shell=True)
    print("NMWENTER")