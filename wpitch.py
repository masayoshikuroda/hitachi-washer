#!/usr/bin/python

import sys
import aubio
import numpy as num
import pyaudio
from argparse import ArgumentParser

usage = 'Usage: python {} [-s silence] [-u unit]'
argparser = ArgumentParser(usage=usage)
argparser.add_argument('-f', '--file'   , type=str   , dest='file'    , default=None    , help='input wave file name')
argparser.add_argument('-m', '--method' , type=str   , dest='method'  , default='fcomb' , help='detect method', choices=['yinfft', 'yin', 'yinfast', 'fcomb', 'mcomb', 'schmitt', 'specacf'])
argparser.add_argument('-r', '--rate'   , type=int   , dest='rate'    , default=8000    , help='samplerate')
argparser.add_argument('-b', '--buffer' , type=int   , dest='buf_size', default=2048)
argparser.add_argument('-s', '--silence', type=float , dest='silence' , default=-90     , help='silence threshold in dB')
argparser.add_argument('-u', '--unit'   , type=str   , dest='unit'    , default='Hz'    , help='pitch unit', choices=['Hz', 'midi'])
args = argparser.parse_args()

detector = aubio.pitch(
    method = args.method,
    buf_size = args.buf_size,
    hop_size = args.buf_size//2,
    samplerate = args.rate
    )
detector.set_unit(args.unit)
detector.set_silence(args.silence)

def get_from_pyaudio():
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format = pyaudio.paFloat32,
        channels = 1,
        rate = args.rate,
        input = True,
        frames_per_buffer = args.buf_size
        )
    return stream

def get_from_wave(fname):
    src = aubio.source(fname, samplerate=args.rate, hop_size=args.buf_size//2, channels=1)
    return src

def analyze_frame(samples):
    pitch = detector(samples)[0]
    volume = num.sum(samples**2)/len(samples)
    volume = "{:.6f}".format(volume)
    print(pitch)
    sys.stdout.flush()

def write_pitch_from_wave(src):
    while True:
        samples, read = src()
        analyze_frame(samples)
        if read < src.hop_size:
            break

def write_pitch_from_stream(stream):
    while stream.is_active():
        data = stream.read(args.buf_size//2)
        samples = num.fromstring(data, dtype=aubio.float_type)
        analyze_frame(samples)

print >> sys.stderr, 'samplerate=' + str(args.rate)
print >> sys.stderr, 'buf_size=' + str(args.buf_size)
print >> sys.stderr, 'silence=' + str(args.silence)
print >> sys.stderr, 'unit=' + str(args.unit)
print >> sys.stderr, 'pitchs/second=' + '{:.1f}'.format(args.rate/(1.0*args.buf_size//2))

if args.file != None:
    src = get_from_wave(args.file)
    write_pitch_from_wave(src)
else:
    stream = get_from_pyaudio()
    write_pitch_from_stream(stream)
