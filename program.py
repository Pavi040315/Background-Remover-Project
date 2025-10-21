# program about background remover from webcam feed using face recognition

#add filters and effects later

import face_recognition
import cv2 #######
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation   
import numpy as np
import os
from datetime import datetime


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

segmentor = SelfiSegmentation()

background_img = cv2.imread("sunset.jpg")
background_img = cv2.resize(background_img, (640, 480))


while True:
    _, frame = capture.read()

    remBG = segmentor.removeBG(frame, background_img, 0.9)
    imageStack = cvzone.stackImages([frame, remBG], 2, 1)

    cv2.imshow("BG Remover", imageStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break


capture.release()
cv2.destroyAllWindows()