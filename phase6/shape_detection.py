import cv2
import numpy as np

img = cv2.imread("phase1/N.png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

for contours in contours:
    approx = cv2.approxPolyDP(contours, 0.01*cv2.arcLength(contours, True), True)

    if len(approx) == 3:
        print("Triangle")
    elif len(approx) == 4:
        print("Rectangle")
    elif len(approx) == 5:
        print("Pentagon")
    elif len(approx) > 5:
        print("Circle")
    else:
        print("unknown shape")
    

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, str(len(approx)), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()