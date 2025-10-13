import cv2

img = cv2.imread("phase2/N.png",cv2.IMREAD_GRAYSCALE)

ret, thres_img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)

cv2.imshow('Image', thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#| Pixel value | Result (in binary thresholding) |
# | ----------- | ------------------------------- |
# | > 100       | becomes **255 (white)**         |
# | ≤ 100       | becomes **0 (black)**           |
