import torch
import sounddevice as sd
import time
from settings import *

def torch_say(words):
    config = configparser.ConfigParser()
    config.read("Scripts\settings.ini")

    language = config["Settings"]["language"]
    model_id = config["Settings"]["model_id"]
    sample_rate = int(config["Settings"]["sample_rate"])
    speaker = config["Settings"]["speaker"]
    put_accent = bool(config["Settings"]["put_accent"])
    put_yo = bool(config["Settings"]["put_yo"])
    device = torch.device(config["Settings"]["device"])  # cpu or gpu

    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                  model='silero_tts',
                                  language=language,
                                  speaker=model_id)
    model.to(device)

    audio = model.apply_tts(text=words + "..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()