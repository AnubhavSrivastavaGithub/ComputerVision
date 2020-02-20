import numpy as np
import cv2

image = np.ones((512,512,3),np.uint8)
cv2.line(image, (0,168),(300,0),(150,100,200),5)
cv2.circle(image, (150,84), 70, (200,0,0),5)
cv2.circle(image, (150,84), 50, (200,0,0),5)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
