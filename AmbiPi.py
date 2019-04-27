from PIL import ImageGrab
import numpy as np




#Get Screenshot using ImageGrab and convert it to numpy array, concatinate it so it is only one continuous array of pixels
screenshot = ImageGrab.grab()
screenshot = screenshot.resize((100,100))
screen_np = np.array(screenshot)
(i,j,k) = screen_np.shape
screen_np = np.reshape(screen_np,(i*j,k))





#Find the most frequent colour
colours, counts = np.unique(screen_np, return_counts=True, axis= 0)
most_frequent_colour = colours[np.argmax(counts)]


print(most_frequent_colour)
