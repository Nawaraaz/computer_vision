import cv2

image = cv2.imread('phase1/N.png')

if image is not None:
    h, w, c = image.shape # it will print the shape( height, width , channels) of the image

    print("height:", h)
    print("width:", w)
    print("channels:", c)
else:
    print("Image not found")