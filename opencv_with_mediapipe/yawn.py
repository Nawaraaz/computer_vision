import cv2
import mediapipe as mp
import math
import time

# Function to calculate MAR
def compute_mar(landmarks, img, vertical_indices, horizontal_indices):
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

    # MAR
    return v_dist / h_dist

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, min_detection_confidence=0.7, min_tracking_confidence=0.7)


MAR_THRESHOLD = 0.6   # Tune based on distance
CONSEC_FRAMES = 20 # Tune
yawn_counter = 0
total_yawns = 0

cap = cv2.VideoCapture(0) #capturing realtime video
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #mediapipe uses RGB so converting realtime video into RGB
    results = face_mesh.process(img_rgb) #processing realtime video converted to rgb

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # computing MAR
        mar = compute_mar(landmarks, img, vertical_indices=[13,14], horizontal_indices=[78,308])

        # Yawn logic
        if mar > MAR_THRESHOLD:
            yawn_counter += 1
        else:
            if yawn_counter >= CONSEC_FRAMES:
                total_yawns += 1
                print("Yawn detected!", total_yawns)
            yawn_counter = 0

        #creating mouth points
        for idx in [13,14,78,308]:
            lm = landmarks[idx]
            cx, cy = int(lm.x * img.shape[1]), int(lm.y * img.shape[0])
            cv2.circle(img, (cx, cy), 2, (0,255,0), -1)

    # Display FPS and total yawns
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.putText(img, f'Total Yawns: {total_yawns}', (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Yawn Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
