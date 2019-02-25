import cv2
import matplotlib.pyplot as plt
#import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("/Users/RuneNisbeth/Documents/6semester/fagprojekt/python/Paper.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    plt.imshow(frame)
    plt.show()

