import cv2
import os
from datetime import datetime
from ultralytics import YOLO

# load YOLO model
model = YOLO("yolov8n.pt")

# open laptop camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kaamerat ei saanud avada")
    exit()

# create folder for results
os.makedirs("results", exist_ok=True)

print("Programm töötab")
print("vajuta 's' pildi salvestamiseks")
print("vajuta 'q' väljumiseks")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO webcam", annotated_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        filename = datetime.now().strftime("results/result_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, annotated_frame)
        print("salvestatud:", filename)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()