#import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/Users/RuneNisbeth/Documents/6semester/fagprojekt/PiPyOpenCV/SteveJobs.jpeg")
#print(img)

#plt.imshow(img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
