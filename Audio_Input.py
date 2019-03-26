import pyaudio
import numpy as np
import struct

# Constants for Audio Input
CHUNK = 10240
RATE = 44100
FORMAT = pyaudio.paInt16

# Setup pyaudio and stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                input=True)

data = stream.read(CHUNK)

data_int = np.fromstring(data,np.int16)
print(data_int)
data_dft = np.abs(np.fft.rfft(data_int))

print(np.argmax(data_dft))


