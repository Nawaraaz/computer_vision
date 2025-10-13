import cv2

image = cv2.imread("phase2/N.png",cv2.IMREAD_GRAYSCALE)
edges= cv2.Canny(image, 50, 150) #It separates “significant” pixels from “insignificant” ones based on intensity.
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
 