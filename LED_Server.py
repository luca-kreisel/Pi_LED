import socket
from neopixel import *



# LED strip configuration:
LED_COUNT      = 300   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 45     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


#Create and bind socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#So you can reuse server after restart more quickly
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("",6000))

s.listen(1)

#Setup led strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:
    s_new, client = s.accept()
    print (client)
    while True:
        data_recv = s_new.recv(34)

        data = data_recv.decode(encoding="utf-8")
        r_s = data[0:3].lstrip('0')
        g_s = data[3:6].lstrip('0')
        b_s = data[6:9].lstrip('0')
        print (r_s)
        print(g_s)
        print(b_s)
        r = g= b= 0
        if r_s != '':
            r = int(r_s)
        if g_s != '':
            g = int(g_s)
        if b_s != '':
            b = int(b_s)
        #Calculate brightness so no voltage drop on the led
        relative = int((3*255)/(r+g+b+1)*45)
        if relative>255:
            relative = 255


        #display colour on strip
        for i in range(300):
            strip.setPixelColorRGB(i, r,g, b)
        strip.setBrightness(relative)
        strip.show()
        print (r,g,b)







