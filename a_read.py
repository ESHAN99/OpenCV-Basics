# Read : Images, Video, Webcam

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break



