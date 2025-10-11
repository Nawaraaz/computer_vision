import cv2

image = cv2.imread('phase1/N.png')

if image is not None:
    sucess = cv2.imwrite('phase1/output.jpg', image)

    if sucess:
        print("Image saved")
    else:
        print("Image not saved")
else:
    print("Image not found")
