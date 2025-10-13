import cv2

image = cv2.imread('phase4/out.jpg')
blur = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow('orginal Image', image)
cv2.imshow('Blured Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()