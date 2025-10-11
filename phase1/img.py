import cv2

image = cv2.imread('phase1/N.png')

if image is not None:
    cv2.imshow('Image', image) #oprn the window
    cv2.waitKey(0) #wait for any key if pressed it will close
    cv2.destroyAllWindows() #close the window
else:
    print("Image not found")

print("image size:", image.size) # it will print the size of the image"image.shape) # it will print the shape( height, width , channels) of the image
