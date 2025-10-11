import cv2

image = cv2.imread('phase2/N.png')

if image is not None:
    resized_image = cv2.resize(image, (200, 200)) # resize the image to 200x200 pixels
    cv2.imshow('Resized Image', resized_image) # display the resized image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('phase2/output.jpg', resized_image) # save the resized image
else:
    print("Image not found")