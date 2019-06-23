import sys
import aubio
import numpy as num
import pyaudio
from argparse import ArgumentParser

usage = 'Usage: python {} [-s silence] [-u unit]'
argparser = ArgumentParser(usage=usage)
argparser.add_argument('-s', '--silence', type=float, dest='silence', default=-90,  help='silence threshold in dB')
argparser.add_argument('-u', '--unit'   , type=str,   dest='unit',    default='Hz', help='pitch unit', choices=['Hz', 'midi'])
args = argparser.parse_args()

detector = aubio.pitch(
    method = 'fcomb',
    buf_size = 2048,
    hop_size = 1024,
    samplerate = 8000
    )
detector.set_unit(args.unit)
detector.set_silence(args.silence)


audio = pyaudio.PyAudio()
stream = audio.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = 8000,
    input = True,
    frames_per_buffer = 2048
    )

while stream.is_active():
    data = stream.read(1024)
    samples = num.fromstring(data, dtype=aubio.float_type)
    pitch = detector(samples)[0]
    volume = num.sum(samples**2)/len(samples)
    volume = "{:.6f}".format(volume)
    print(pitch)
    sys.stdout.flush()
