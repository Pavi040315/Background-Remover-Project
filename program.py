# program about background remover from webcam feed using face recognition

#add filters and effects later

import face_recognition
import cv2 #######
from cvzone.SelfiSegmentationModule import SelfiSegmentation   
import numpy as np
import os
from datetime import datetime


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    _, frame = capture.read()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break
    

capture.release()
cv2.destroyAllWindows()