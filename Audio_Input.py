import pyaudio
import numpy as np
import colorsys
import pygame



# Constants for Audio Input
CHUNK = 1024*4
RATE = 44100
FORMAT = pyaudio.paInt16

# Setup pyaudio and stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                input=True)

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
while True:
    # Get pitch of input every 0.1s
    data = stream.read(CHUNK)

    # convert to int array
    data_int = np.fromstring(data,np.int16)
    # use dft to get frequency spectrum
    data_dft = np.abs(np.fft.rfft(data_int))

    # pitch is frequency with highest magnitude
    pitch = np.argmax(data_dft)


    # map pitch to colour(HSV):
    # Range of pitch is usually [0,500], so calculate hue value (0 to 1) of Hsv as: pitch/500
    hue = 1
    if pitch < 1000:
        hue =  pitch/1000
    print(hue)
    # calculate (normalized) rgb value for easier output
    (r,g,b) = colorsys.hsv_to_rgb(hue,0.75,0.75)

    (r,g,b) = (r*255,g*255,b*255)

    #output using pygame

    screen.fill((r,g,b))
    pygame.display.update()















