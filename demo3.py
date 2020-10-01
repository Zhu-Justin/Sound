#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
fs = 44100  # Sample rate
duration = 5  # seconds

# data = np.array([])
data = []

def callback(indata, outdata, frames, time, status):
    global data
    if status:
        print(status)
    data.append(indata)
    outdata[:] = indata

with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))

print("Data")
print(len(data))
# print((data))
print(data[0].shape)

filedata = np.concatenate(data)
print(filedata.shape)

write('outputcall.wav', fs, filedata)
# Save as WAV file
