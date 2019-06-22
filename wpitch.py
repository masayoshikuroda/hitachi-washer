import sys
import aubio
import numpy as num
import pyaudio

unit = 'Hz'
silence = -40

# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = 8000,
    input = True,
    frames_per_buffer = 2048
    )

# Aubio's pitch detection.
pDetection = aubio.pitch(
    method = "fcomb",
    buf_size = 2048,
    hop_size = 1024,
    samplerate = 8000
    )

# Set unit.
pDetection.set_unit(unit)
pDetection.set_silence(silence)

while True:
    data = stream.read(1024)
    samples = num.fromstring(data, dtype=aubio.float_type)
    pitch = pDetection(samples)[0]
    volume = num.sum(samples**2)/len(samples)
    volume = "{:.6f}".format(volume)
    print(pitch)
    sys.stdout.flush()