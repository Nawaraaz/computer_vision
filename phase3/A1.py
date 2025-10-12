import cv2

camera = cv2.VideoCapture(0)

frame_width= input("Enter the width of the frame in integer format for default live as it is: ")
if frame_width == "":
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))



frame_height= input("Enter the height of the frame in integer format for default live as it is: ")
if frame_height == "":
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = input("Enter the codec of the video in string format for default live as it is: ")
if codec == "":
    codec = cv2.VideoWriter_fourcc(*'XVID')

output = input("Enter the path where you want to save the video: ")

if output == "":
    output = 'output.avi'

fps = input("Enter the fps of the video in integer format for default live as it is: ")
if fps == "":
    fps = 20

recorder = cv2.VideoWriter(output, codec, fps, (frame_width, frame_height))

while True:
    sucess, frame = camera.read()

    if not sucess:
        break

    recorder.write(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Quitting")
        break


recorder = cv2.VideoWriter('output.avi', codec, fps, (frame_width, frame_height))

while True:
    sucess, frame = camera.read()

    if not sucess:
        break

    recorder.write(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Quitting")
        break