import configparser
from torch_speak import *
from pyttsx_speak import *

def check_engine():
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.curdir) + "\settings.ini")
    speak_engine = {'say':pyttsx_say}
    if config["Settings"]["speaker_engine"] == 'torch':
        speak_engine = {'say':torch_say}
    elif config["Settings"]["speaker_engine"] == 'pyttsx':
        speak_engine = {'say':pyttsx_say}
    return speak_engine
