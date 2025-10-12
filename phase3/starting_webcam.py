import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()# it will read the frame and give a bool value for ret
    #and due to this mechanism we can look out the real time video

    if not ret:
        break

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # chect for every 1 millisecond whether user has pressed 'q'
        print("Video quitting")
        break

cap.release()
cv2.destroyAllWindows()