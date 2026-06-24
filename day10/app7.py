
import ultralytics
from ultralytics import YOLO
import cv2
from pprint import pprint

ultralytics.checks()

model = YOLO("yolov8n.pt")
pprint(f"Model Architecture Task: {model.task}")

results = model("day10/road.jpeg")
pprint("Inference step complete.")