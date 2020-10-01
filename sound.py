#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

FS = 44100  # SAMPLE RATE
SECONDS = 20  # DURATION OF RECORDING
MULTIPLIER = 1000
VOICE = 0.01
data = []


# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file

def getdb(frame):
    return np.sqrt(np.power(frame, 2).mean())

def detectspeech(indata, outdata, frames, time, status):
    global data
    if status:
        print(status)
        # Record voice here
        if getdb(indata) > VOICE:
            data.append(indata)
    # outdata[:] = indata
    # print(getdb(indata))
    return 0
    # return myrecording

def recordspeech(myrecording):
    myrecording = sd.rec(int(SECONDS * FS), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    # Record voice here
    pass

def writespeech():
    pass

def main():
    with sd.Stream(channels=1,
                   callback=detectspeech):
        sd.sleep(int(SECONDS * MULTIPLIER))
    # try:
    #     detectspeech()
    # except:
    #     print("detectspeech")
    # try:
    #     recordspeech()
    # except:
    #     print("detectspeech")
    # try:
    #     writespeech()
    # except:
    #     print("writespeech")
    #     writespeech()
    return 0

main()
