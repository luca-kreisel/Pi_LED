from PIL import ImageGrab
import numpy as np

import time
import socket
import pickle
import  sys



#Constants
WAIT = 0.05
Pi_IP = "192.168.1.158"
Pi_Port = 6000




#Setup and connect socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Pi_IP,Pi_Port))

while True:
    #Get Screenshot using ImageGrab and convert it to numpy array, concatinate it so it is only one continuous array of pixels
    screenshot = ImageGrab.grab()
    screenshot = screenshot.resize((150,150))
    screen_np = np.array(screenshot)
    (i,j,k) = screen_np.shape
    screen_np = np.reshape(screen_np,(i*j,k))





    #Find the most frequent colour
    colours, counts = np.unique(screen_np, return_counts=True, axis= 0)
    most_frequent_colour = colours[np.argmax(counts)]
    print(most_frequent_colour)
    r = most_frequent_colour[0]
    g = most_frequent_colour[1]
    b = most_frequent_colour[2]


    #send data over tcp socket to Pi:

    #marshall data first (resulting size 29)
    data = pickle.dumps((r,g,b), protocol=2)
    #send it over tcp
    print (sys.getsizeof(data))
    s.send(data)



    time.sleep(WAIT)


