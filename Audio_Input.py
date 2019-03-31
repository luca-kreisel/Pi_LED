import pyaudio
import numpy as np
import colorsys
from neopixel import *



# Constants for Audio Input
CHUNK = 1024*2
RATE = 44100
FORMAT = pyaudio.paInt16

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Setup pyaudio and stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                input=True)
#Setup led strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:
    # Get pitch of input every 0.1s
    data = stream.read(CHUNK,
		exception_on_overflow = False)

    # convert to int array
    data_int = np.fromstring(data,np.int16)
    # use dft to get frequency spectrum
    data_dft = np.abs(np.fft.rfft(data_int))

    # pitch is frequency with highest magnitude
    pitch = np.argmax(data_dft)


    # map pitch to colour(HSV):
    # Range of pitch is usually [0,500], so calculate hue value (0 to 1) of Hsv as: pitch/500
    hue = 1.0
    if pitch < 100:
        hue =  pitch/100.0
    print(hue)
    # calculate (normalized) rgb value for easier output
    (r,g,b) = colorsys.hsv_to_rgb(hue,0.75,0.75)

    (r,g,b) = (r*255,g*255,b*255)

    #output using neopixel
    for i in range(strip.numPixels()):
            strip.setPixelColorRGB(i, int(r), int(g),int(b))
    strip.show()
















