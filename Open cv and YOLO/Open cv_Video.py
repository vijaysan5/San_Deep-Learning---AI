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
print(f"Extracted {count} Frames.")
