import cv2
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
# bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitwise_and', bitwise_and)
cv2.imshow('bitwise_or', bitwise_or)
# cv2.imshow('bitwise_xor', bitwise_xor)
cv2.imshow('bitwise_not', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()  