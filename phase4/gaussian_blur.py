import cv2

image = cv2.imread('phase2/N.png')

if image is not None:
    blured_image = cv2.GaussianBlur(image, (5, 5), 2) # blur the image
    cv2.imshow('orginal Image', image) # display the image
    cv2.imshow('Blured Image', blured_image) # display the blured image
    cv2.waitKey(0)
    cv2.destroyAllWindows()