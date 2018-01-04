#coding: utf-8

import sys
import wave
import pyaudio
import numpy as np
import scipy.signal
from statistics import mean

format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024

audio = pyaudio.PyAudio()

if len(sys.argv) >= 2:
    from_file = True
else:
    from_file = False

if from_file:
    print("WAV file: ", sys.argv[1])
    wf = wave.open(sys.argv[1], "r")
    format = audio.get_format_from_width(wf.getsampwidth())
    channels = wf.getnchannels()
    rate = wf.getframerate()
    print("Sample Width: ", wf.getsampwidth())
    print("#Frames:      ", wf.getnframes())
    print("Params:       ", wf.getparams())
    print("Seconds:      ", float(wf.getnframes())/wf.getframerate())

print("Format:       ", format)
print("#Channels:    ", channels)
print("Frame Rate:   ", rate)
print("Chunk:        ", chunk)


stream = audio.open(
	format=format,
	channels = channels,
	rate = rate,
	input=True)

w = wave.Wave_write("output.wav")
w.setnchannels(channels)
w.setsampwidth(2)
w.setframerate(rate)

f1 = 23
f2 = 27
data_f1 = []
data_f2 = []
axis = np.fft.fftfreq(chunk, d=1.0/rate)
#print(','.join(map(str, axis[f1:f2])))
print(axis[f1], axis[f2])


while True:
    if from_file:
        data = wf.readframes(chunk)
        if channels == 2:
            data = data[::channels]
        if data == '':
            break;
    else:
        data = stream.read(chunk)
   
    w.writeframes(data)
    data = np.frombuffer(data, dtype="int16")/32768.0
    if len(data) != chunk:
        break
    data = np.hamming(len(data)) * data
    data = np.fft.fft(data)
    data = np.abs(data)
#    print(','.join(map(str, data[23:30])))
#    print(data[f1],data[f2])
    if len(data_f1) > 40:
        del data_f1[0]
        del data_f2[0]
    data_f1.append(data[f1])
    data_f2.append(data[f2])
#    print(mean(data_f1), mean(data_f2))
    if mean(data_f1) > 3:
        print("ring!")

w.close()
stream.close()
audio.terminate()
