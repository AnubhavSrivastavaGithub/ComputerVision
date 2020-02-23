import cv2
import numpy as np

img = cv2.imread('watch.jpg')
img2= cv2.imread('city.jpg')
cv2.imshow('Image1',img)
cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
