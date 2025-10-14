import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands # importing hand module
mp_draw = mp.solutions.drawing_utils #importing drawing module

# Creating Hand object
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

#creating fps counter
pTime = 0
cTime = 0

cap = cv2.VideoCapture(0) #opening webcam to capture realtime video

while True:
    success, img = cap.read() #reading video img will contain video in frames, sucess is bool value
    if not success:
        break
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting to RGB mediapipe process on RGB
    results = hands.process(imgRGB)

    # If hand landmarks are found
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of each landmark
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:  # Tip of thumb
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

    # Calculating FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Hand Tracking", img)#displaying video
    if cv2.waitKey(1) & 0xFF == ord('q'): #if q is pressed, video will quit
        break

cap.release()
cv2.destroyAllWindows()
