# Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpeg")
print(img.shape)

imgResize = cv2.resize(img, (250, 250))
print(imgResize.shape)

imgCropped = img[0:200, 200:300]

cv2.imshow("I", img)
cv2.imshow("IR", imgResize)
cv2.imshow("IC", imgCropped)
cv2.waitKey(0)