import cv2

image = cv2.imread('phase2/N.png')

if image is not None:
    h ,w , c = image.shape # it will print the shape( height, width , channels) of the image
    cv2.circle(image, ((w // 2)+5, h // 2), 250, (0, 0, 255), 2)
    cv2.imshow('Image', image) # display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")