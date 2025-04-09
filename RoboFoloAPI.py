from roboflow import Roboflow
rf = Roboflow(api_key="3205MH29k2z3u5Ejc3HU") # THIS API KEY IS REVOKED. PLEASE USE YOUR OWN API KEY
project = rf.workspace("roboflow-bee").project("football-players-detection-3zvbc")
version = project.version(1)
dataset = version.download("yolov5")
import cv2
import requests
import json


video_path = "videoFootball.mp4" 
cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("خطأ في فتح الفيديو")
    exit()

frame_count = 0 


while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break  

    # take 1 frame from every 5
    if frame_count % 5 == 0:
        frame_path = "temp_frame.jpg"
        cv2.imwrite(frame_path, frame)

        response = model.predict(frame_path, confidence=40, overlap=30).json()

        for obj in response['predictions']:
            x, y, w, h = int(obj['x']), int(obj['y']), int(obj['width']), int(obj['height'])
            label = obj['class']

            cv2.rectangle(frame, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Football Analysis', frame)

    frame_count += 1  

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()