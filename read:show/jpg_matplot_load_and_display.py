
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("/Users/RuneNisbeth/Documents/6semester/fagprojekt/python/Nyhavn.jpg")
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()