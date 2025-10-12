import cv2

image = cv2.imread('phase2/N.png')

if image is not None:
    cv2.putText(image, 'Hello, World!', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(image, 'This is my logo do you like it?', (200, (image.shape[0]-200)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow('Image', image) # display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")