#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import sys

FS = 44100  # SAMPLE RATE
SECONDS = 10  # DURATION OF RECORDING
MULTIPLIER = 1000
VOICE = 0.01
data = []
silence = 0 # global variable to denote silence
OUTPUT = "main.wav"
QUIT = 50 # Quit application after 100 loops of nonrecording

# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file

def getdb(frame):
    return np.sqrt(np.power(frame, 2).mean())

def callback(indata, outdata, frames, time, status):
    global data
    global silence
    global OUTPUT
    if status:
        print(status)
        # Record voice here
    if getdb(indata) > VOICE:
    # if True:
        print("Recording")
        data.append(indata)
        filedata = np.concatenate(data)
        write(OUTPUT, FS, filedata)
        silence = 0
    else:
        print("Stop Recording")
        silence += 1
    if silence > QUIT:
        sys.exit(0)
    return 0


def main(filename, time):
    global OUTPUT
    global SECONDS
    if filename:
        OUTPUT = filename
    if time:
        SECONDS = time

    with sd.Stream(channels=2, callback=callback):
        sd.sleep(int(SECONDS * MULTIPLIER))

    return 0

# main()
