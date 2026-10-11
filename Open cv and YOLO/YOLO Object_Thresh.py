# Thresh Video 

from ultralytics import YOLO
import cv2

# Auto Download "yolov8n.pt"
Model = YOLO("yolov8n.pt")

Capture = cv2.VideoCapture("San's  DataScience Folder/Deep Learning Folder/Video.mp4")

if not Capture.isOpened():
    print("Its not open")
    exit()

while True:
    ret, frame = Capture.read()

    if not ret:
        break

    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, Thresh = cv2.threshold(Gray, 127, 255, cv2.THRESH_BINARY)

    Result = Model(Thresh)

    Frame_plot = Result[0].plot()



    cv2.imshow("YOLO Object", Frame_plot)
    

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

    
Capture.release()
cv2.destroyAllWindows()