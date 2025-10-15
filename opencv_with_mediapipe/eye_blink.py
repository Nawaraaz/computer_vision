import cv2
import mediapipe as mp
import math
import time

# Function to calculate EAR
def compute_ear(landmarks, img, vertical_indices, horizontal_indices):
    h, w, _ = img.shape
    # Vertical distance
    top = landmarks[vertical_indices[0]]
    bottom = landmarks[vertical_indices[1]]
    v_dist = math.hypot(int(top.x*w) - int(bottom.x*w),
                        int(top.y*h) - int(bottom.y*h))
    
    # Horizontal distance
    left = landmarks[horizontal_indices[0]]
    right = landmarks[horizontal_indices[1]]
    h_dist = math.hypot(int(left.x*w) - int(right.x*w),
                        int(left.y*h) - int(right.y*h))
    
    # EAR
    return v_dist / h_dist


mp_face_mesh = mp.solutions.face_mesh # importing face mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, min_detection_confidence=0.7, min_tracking_confidence=0.7)

#variables to count blinks
EAR_THRESHOLD = 0.25   # Adjust if needed
CONSEC_FRAMES = 2
blink_counter = 0
total_blinks = 0

# capturing video in real time using webcam
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Compute EAR for left and right eyes
        left_ear = compute_ear(landmarks, img, [159,145], [33,133])
        right_ear = compute_ear(landmarks, img, [386,374], [362,263])
        avg_ear = (left_ear + right_ear) / 2

        # Blink logic
        if avg_ear < EAR_THRESHOLD:
            blink_counter += 1
        else:
            if blink_counter >= CONSEC_FRAMES:
                total_blinks += 1
                print("Blink detected!", total_blinks)
            blink_counter = 0

        # Drawing eye points
        for idx in [33, 133, 159, 145, 362, 263, 386, 374]:
            lm = landmarks[idx]
            cx, cy = int(lm.x * img.shape[1]), int(lm.y * img.shape[0])
            cv2.circle(img, (cx, cy), 2, (0,255,0), -1)

    # Displaying FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.putText(img, f'Total Blinks: {total_blinks}', (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Eye Blink Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
