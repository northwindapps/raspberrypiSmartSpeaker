from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import logging
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

samplerate, data = wavfile.read('./test.wav')
print(data)