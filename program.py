# program about background remover from webcam feed using face recognition

# add comments later

import cv2 #######
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation   
import numpy as np
import os
from datetime import datetime


# Initialize webcam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# Initialize Selfie Segmentation model (for background removal)
segmentor = SelfiSegmentation()


# Create necessary folders 
backgrounds_folder = os.makedirs("Backgrounds", exist_ok=True)
captured_images_folder = os.makedirs("Captured_Images", exist_ok=True)
csv_folder = os.makedirs("CSV Files", exist_ok=True)


# Open CSV file to log captured images
csv_folder = open("CSV Files/capture_log.csv", "a")
csv_folder.write("timestamp,filename\n")
background_files = ["sunset.jpg", "beach.jpg", "mountains.jpg", "city.jpg"]
bg_index = 0


# Refresh the list of background files 
background_files = [
     f for f in os.listdir("Backgrounds")
        if os.path.isfile(os.path.join("Backgrounds", f))
]


# Allow user to add new background images
add_background = input("Do you want to add a new background image? (Y/N):").upper()
while add_background == 'Y':
    new_bg_path = input("Enter the path of the new background image: ")
    new_bg_file = os.path.basename(new_bg_path)
    destination_path = os.path.join("Backgrounds", new_bg_file)
    try:
        new_bg_img = cv2.imread(new_bg_path)
        cv2.imwrite(destination_path, new_bg_img)
        background_files.append(new_bg_file)
        print(f"Background image '{new_bg_file}' added successfully.")
    except Exception as e:
        print("Error adding background image!!!")
    add_background = input("Do you want to add another background image? (Y/N):").upper()


# Background selection
bg_selection = print("Available backgrounds in 'Backgrounds' folder:")
for i, bg in enumerate(background_files, start=1):
        print(f"{i}. {bg}")
background_filename = input("Enter the background image filename (with extension) to use from 'Backgrounds' folder: ")
if background_filename.isdigit():
    bg_index = int(background_filename) - 1
    background_filename = background_files[bg_index]
print(f"Select background: {background_filename}")


# Load background image
background_img = cv2.imread(f"Backgrounds/{background_filename}")
background_img = cv2.resize(background_img, (640, 480))


# Main loop
while True:

    _, frame = capture.read()

    remBG = segmentor.removeBG(frame, background_img, 0.8) #changed background
    imageStack = cvzone.stackImages([frame, remBG], 2, 1) #both side by side

    cv2.imshow("BG Remover", imageStack)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename = f"frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        filepath = os.path.join("Captured_Images", filename)
        cv2.imwrite(filepath, remBG)
        snapshot_url = f"file:///{os.path.abspath(filepath).replace(os.sep, '/')}"
        csv_folder.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{snapshot_url},{background_files[bg_index]}\n")
        print(f"Saved: {filename} with background {background_files[bg_index]}")

    elif key == ord('q'):
        break


csv_folder.close()
capture.release()
cv2.destroyAllWindows()