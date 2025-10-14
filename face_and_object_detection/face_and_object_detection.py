import cv2

face_cascade = cv2.CascadeClassifier("face_and_object_detection/haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, 1.1, 5) #(image, scaleFactor, minNeighbors) (if minNeighbrours = 3: loosew checking 5: safe checking 6or more: strict checking)

    for (x, y, w, h) in face:
        #x- how far from left
        #y- how far from top
        #w- width of face
        #h- height of face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Webcam face detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Quitting")
        break
cap.release()
cv2.destroyAllWindows()