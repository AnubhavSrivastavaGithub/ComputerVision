import cv2
import numpy as np

img = cv2.imread('watch.jpg')
img2= cv2.imread('city.jpg')
cv2.imshow('Image1',img)
cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

// Load Two Images simultaneously and show them in two different windows 'Image1' & 'Image2'.
// Both the two Images city.jpg & watch.jpg are in the same directory.
// Both the images can be of different sizes.
// Both the images can be of different color codes.
// Enter any key to destroy windows.
