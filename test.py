import shutil
import torch
import torchaudio
import os
import torch.nn as nn
import torch.nn.functional as F
import IPython
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices


preset = "fast"
voice = "seanwolf"
path = voice
files = []

def upload_files():
    custom_voice_folder = f"tortoise/voices/{voice}"
    os.makedirs(custom_voice_folder, exist_ok=True)

    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)

    for i, file in enumerate(files):
        shutil.copyfile(f"{path}/{file}", os.path.join(custom_voice_folder, f'{i}.wav'))

# # Call the function to upload files
upload_files()

# This will download all the models used by Tortoise from the HuggingFace hub.
tts = TextToSpeech()
# # Generating speech with the custom voice.
voice_samples, conditioning_latents = load_voice(voice)

text = """
Ouviram do Ipiranga as margens plácidas
"""
gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                          preset=preset)
torchaudio.save(f'generated-{voice}.wav', gen.squeeze(0).cpu(), 24000)