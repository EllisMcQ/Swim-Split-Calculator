import cv2
import os


def load_video():
    
    file_found = False

    while not file_found:
        video_path = input("Enter Video Path: ")


        if os.path.exists(video_path):
            print("File found")
            file_found = True
        else:
            print("Something went wrong...")

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        print("Something went wrong...")

load_video()

    


