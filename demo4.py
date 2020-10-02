#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
duration = 5.5  # seconds
fs = 44100  # Sample rate
data = []

def callback(indata, outdata, frames, time, status):
    global data
    if status:
        print(status)
    outdata[:] = indata
    data[:] = indata

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))

filedata = np.concatenate(data)
print(filedata.shape)

write('demo4.wav', fs, filedata)
