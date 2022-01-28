import os
from utils import *

def twitch_download(channel, numberOfClips):
    os.system("twitch-dl clips " + channel + " --period last_day --download --limit " + str(numberOfClips))
    move_files()




