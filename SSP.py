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
    fps = capture.get(cv2.CAP_PROP_FPS)
    fc = capture.get(cv2.CAP_PROP_FRAME_COUNT)

    if not capture.isOpened():
        print("Something went wrong...")

    return capture, fps, fc



def frame_picker(capture):

    split_frames = []

    success, frame = capture.read()

    while success:
        cv2.imshow("swim-vid", frame)
        print("Press Space to save, Press Enter to continue... ")
        key_pressed = cv2.waitKey(delay=0)

        if key_pressed == ord(" "):
            split_frames.append(int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
            print(split_frames)
        elif key_pressed == ord("\r"):
            success, frame = capture.read()

        
    
    return split_frames



capture, fps, fc = load_video()
frame_picker(capture)






