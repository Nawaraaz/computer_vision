import cv2

image = cv2.imread('phase1/N.png')

if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    cv2.imshow('Grayscale Image', gray_image) # display the grayscale image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('phase1/output.jpg', gray_image) # save the grayscale image
else:
    print("Image not found")