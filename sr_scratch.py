from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import logging
import sys
import numpy
from numpy.fft import fft, fftshift
numpy.set_printoptions(threshold=sys.maxsize)

samplerate, data = wavfile.read('./test.wav')
# print(data)

window = numpy.hanning(51)
A = fft(window, 2048) / 25.5

print(A)