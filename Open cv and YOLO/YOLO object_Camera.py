from ultralytics import YOLO
import cv2

# Download YOLO :
Project = YOLO("yolov8n.pt")

# Open Camera on sys :
Capture = cv2.VideoCapture(0)

# Read :
if not Capture.isOpened() :
    print("Cann't Open Camera")
    exit()

while True :
    ret, frame = Capture.read()

    if not ret :
        print("Cann't Read Frame...")
        break
    # Object Detecate :
    result = Project(frame)

    # Detecat Draw :
    Plot = result[0].plot()
    # print(Plot)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

Capture.release()
cv2.destroyAllWindows()