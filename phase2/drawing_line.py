import cv2

image = cv2.imread('phase2/N.png')

if image is not None:
    # cv2.line(image, (100,100), (400,400), (0,255,0), 1)
    pt1= (100,100)
    pt2= (400,400)
    color= (0,255,0)
    thickness= 2
    cv2.line(image, pt1, pt2, color, thickness)
    cv2.rectangle(image, (200,200), (600,600), (0,0,255), 2)
    cv2.imshow('Image', image) # display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")