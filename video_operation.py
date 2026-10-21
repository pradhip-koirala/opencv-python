
import os
# This line tells Qt to completely ignore and hide internal warning logs
os.environ["QT_LOGGING_RULES"] = "*.warning=false"

import cv2
video = cv2.VideoCapture('ved1.mp4')


if not video.isOpened():
    print("Error: Could not open or find the video file.")
    exit()

while video.isOpened():
    ret, frame = video.read()

    if ret:
        cv2.imshow('Video Playback', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            break
video.release()
cv2.destroyAllWindows()