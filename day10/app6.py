import cv2
from pprint import pprint
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

cap=cv2.VideoCapture(0)
#pprint(cap)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    result=model(frame)
    annotated_frame = result[0].plot()
    cv2.imshow("LiveCamera",annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break