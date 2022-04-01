from random import randint
import pyaudio
from time import sleep

audio = pyaudio.PyAudio()

INPUT_DEVICE_ID = 1
OUTPUT_DEVICE_ID = 3

instream = audio.open(format = pyaudio.paInt16, channels = 1, rate = 44100, input = True, input_device_index=INPUT_DEVICE_ID, frames_per_buffer = 512)
outstream = audio.open(format = pyaudio.paInt16, channels = 1, rate = 44100, output = True, output_device_index=OUTPUT_DEVICE_ID)
while True:
    data = instream.read(512, exception_on_overflow=False)
    sleep(0.005 * randint(0,2))
    outstream.write(data)