import cv2
import os
from Race import Race


def load_video():
    
    file_found = False

    while not file_found:
        video_path = input("Enter Video: ")
        end_time = float(input("Time of race (00.00): --> "))

        if os.path.exists(video_path):
            print("File found")
            file_found = True
        else:
            print("Something went wrong...")

    capture = cv2.VideoCapture(video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)

    if not capture.isOpened():
        print("Something went wrong...")

    return capture, fps, end_time


def frame_picker(capture):

    split_frames = []

    success, frame = capture.read()

    print(" 'Space' - Mark Split  |  'Backspace' - Rewind Frame   |  'Enter' — Continue  |  'Q' — Finish ")
    while success:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("swim-vid", frame)
        #print(" 'Space' to save, 'Enter' to continue, 'Q' to Finish ")
        key_pressed = cv2.waitKey(delay=0)
        

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
    segment_splits = []
    segment_splits.append(splits[0] - start_time)

    for i in range(1, len(splits)):
        segment_splits.append(round(splits[i] - splits[i-1], 2))

    distances = [15, 25, 35, 50]
    split_dicts = []
    for d, s, c in zip(distances, segment_splits, splits):
        split_dicts.append({"distance": d, "segment_split": s, "cumulative_split": round(c, 2)})
    
    print(f"""splits:
          
15m = {round(segment_splits[0], 2)}
25m = {round(segment_splits[0]+segment_splits[1], 2), segment_splits[1]}
35m = {round(segment_splits[0]+segment_splits[1]+segment_splits[2], 2), segment_splits[2]}
50m = {end_time, segment_splits[3]}
          """)
    
    return split_dicts


def get_save_info():
    stroke = input("Stroke: ")
    distance = int(input("Distance: "))
    course = input("LC/SC: ")
    date = input("Date - (DD/MM/YY): ")

    return stroke, distance, course, date



capture, fps, end_time = load_video()
split_frame_nums = frame_picker(capture)
split_dicts = calculator(split_frame_nums, fps, end_time)

choice = input("Press S to save, C to cancel: ").lower()
if choice == "s":
    stroke, distance, course, date = get_save_info()
    race = Race(None, stroke, distance, course, date, end_time)
    race.splits = split_dicts
    results = race.save_race()
    print("Saved")
