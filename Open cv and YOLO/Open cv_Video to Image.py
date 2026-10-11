import cv2
import os

video = "D:\Sangavi A\San's  DataScience Folder\Deep Learning Folder\Video.mp4"

output = "frames"
os.makedirs(output, exist_ok=True)

capture = cv2.VideoCapture(video)

count = 0

while True:
    ret, frame = capture.read()

    if not ret:
        break

    fline_name = os.path.join(output, f"frame_{count:04d}.jpg")
    cv2.imwrite(fline_name, frame)

    count += 1

capture.release()
# print(f"Extracted {count} Frames.")


ThreshFr = "Thresh Freams"
os.makedirs(ThreshFr, exist_ok=True)

while True:
    ret_trf, frame_trf = capture.read()

    if not ret_trf:
        break
    Gray = cv2.cvtColor(frame_trf, cv2.COLOR_BGR2GRAY)

    _, Thresh = cv2.threshold(fline_name, frame_trf, 127, 255, cv2.THRESH_BINARY)

    fline_name = os.path.join(ThreshFr, f"frame_{count:04d}.png")
    cv2.imwrite(fline_name, Thresh)

    count += 1

capture.release()
print(f"Extracted {count} Thresh Frames.")
