import cv2

face_cascade = cv2.CascadeClassifier("face_and_object_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("face_and_object_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("face_and_object_detection/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

    cv2.imshow('Webcam face detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Quitting")
        break
cap.release()
cv2.destroyAllWindows()