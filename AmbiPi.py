from PIL import ImageGrab, Image
import numpy as np

import time
import socket

import  sys



#Constants
WAIT = 0.1
Pi_IP = "192.168.1.158"
Pi_Port = 6000




#Setup and connect socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Pi_IP,Pi_Port))

while True:
    #Get Screenshot using ImageGrab and convert it to numpy array, concatinate it so it is only one continuous array of pixels
    screenshot = ImageGrab.grab()
    screenshot = screenshot.resize((1,1))
    screen_np = np.array(screenshot)

    (r,g,b) = screen_np[0][0]


    #send data over tcp socket to Pi:

    #first create string and pad zeros
    r_s = str(g).zfill(3)
    g_s = str(r).zfill(3)
    b_s = str(b).zfill(3)

    data = (r_s + g_s + b_s).encode()

    print (sys.getsizeof(data))

    #then send string over tcp
    s.send(data)





    time.sleep(WAIT)


