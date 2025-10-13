import cv2
import numpy as np

image = cv2.imread('phase4/out1.jpg')

sharpen_kernal = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

filter = cv2.filter2D(image, -1, sharpen_kernal)

cv2.imshow('orginal Image', image)
cv2.imshow('Sharpened Image', filter)
cv2.waitKey(0)
cv2.destroyAllWindows()