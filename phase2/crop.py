import cv2

image = cv2.imread('phase1/N.png')

if image is not None:
    cropped_image = image[100:400, 100:400] # crop the image to 300x300 pixels
    cv2.imshow('Cropped Image', cropped_image) # display the cropped image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")