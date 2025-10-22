# program about background remover from webcam feed using face recognition

# add comments later
# add functionality to change background from a set of images
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


captured_images_folder = os.makedirs("Captured_Images", exist_ok=True)
csv_folder = os.makedirs("CSV Files", exist_ok=True)
csv_folder = open("CSV Files/capture_log.csv", "a")
csv_folder.write("timestamp,filename\n")


while True:
    _, frame = capture.read()

    remBG = segmentor.removeBG(frame, background_img, 0.8) #changed background
    imageStack = cvzone.stackImages([frame, remBG], 2, 1) #both side by side

    cv2.imshow("BG Remover", imageStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break


cv2.imwrite(f"Captured_Images/frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg", remBG) 
csv_folder.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg\n")
csv_folder.close()


capture.release()
cv2.destroyAllWindows()