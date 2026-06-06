import cv2
import os


def load_video():
    
    file_found = False

    while not file_found:
        video_path = input("Enter Video: ")
        end_time = float(input("Time of race (00.00): -->   "))



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

    return capture, fps, end_time


def frame_picker(capture):

    split_frames = []

    success, frame = capture.read()


    print(" 'Space' to save, 'Enter' to continue, 'Q' to Finish ")
    while success:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("swim-vid", frame)
        #print(" 'Space' to save, 'Enter' to continue, 'Q' to Finish ")
        key_pressed = cv2.waitKey(delay=0)
        print(split_frames)

        if key_pressed == ord(" "):
            split_frames.append(int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
            print("Saved frame " + str(capture.get(cv2.CAP_PROP_POS_FRAMES)))
            success, frame = capture.read()
        elif key_pressed == ord("\r"):
            success, frame = capture.read()
        elif key_pressed == ord("\x08"):
            prev_frame = int(capture.get(cv2.CAP_PROP_POS_FRAMES)) - 2
            if split_frames and prev_frame == split_frames[-1]:
                split_frames.pop()
            current = capture.get(cv2.CAP_PROP_POS_FRAMES)
            capture.set(cv2.CAP_PROP_POS_FRAMES, current - 2)
            success, frame = capture.read()
        elif key_pressed == ord("q"):
            break
            

    return split_frames
 

def calculator(split_frames, fps, end_time):

    splits = [round(i/fps, 2) for i in split_frames]
    start_time = round(splits[3] - end_time, 2)

    s1 = round(splits[0] - start_time, 2)
    s2 = round(splits[1] - splits[0], 2)
    s3 = round(splits[2] - splits[1], 2)
    s4 = round(splits[3] - splits[2], 2)
    print(f"""splits:
          
15m = {s1}
25m = {round(s1+s2, 2), s2}
35m = {round(s1+s2+s3, 2), s3}
50m = {end_time, s4}
          """)
    return splits



capture, fps, end_time = load_video()
split_frame_nums = frame_picker(capture)
calculator(split_frame_nums, fps, end_time)