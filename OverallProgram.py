Overall Program  
import cv2 
import cvzone 
import math 
import time 
import paho.mqtt.client as mqtt 
from ultralytics import YOLO 
# MQTT Setup 
broker = "test.mosquitto.org" # Ganti dengan alamat broker MQTT Anda port = 1883 
topic = "box/detection" # Topik untuk mengirim perintah ke Arduino 
client = mqtt.Client() 
client.connect(broker, port) 
# Video Capture (gunakan webcam atau video file) 
url = "http://192.168.221.242:8080/video" 
cap = cv2.VideoCapture(url) # Untuk Video 
# Model YOLO 
model = YOLO("best 80.pt") 
classNames = ['big box', 'small box'] 
prev_frame_time = 0 
new_frame_time = 0 
while True: 
new_frame_time = time.time()
success, img = cap.read() 
if not success: 
break 
results = model(img, stream=True) 
for r in results: 
boxes = r.boxes 
for box in boxes: 
# Bounding Box 
x1, y1, x2, y2 = box.xyxy[0] 
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 
w, h = x2 - x1, y2 - y1 
cvzone.cornerRect(img, (x1, y1, w, h)) 
# Confidence 
conf = math.ceil((box.conf[0] * 100)) / 100 
cls = int(box.cls[0]) 
# Display Class Name and Confidence 
cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)),  scale=1, thickness=1) 
# If object is 'big box', send 0 degree to servo 
if classNames[cls] == 'big box': 
client.publish(topic, "0") # Perintah untuk servo 0 derajat 
elif classNames[cls] == 'small box': 
client.publish(topic, "45") # Perintah untuk servo 45 derajat 
# Hitung Frame Rate 
fps = 1 / (new_frame_time - prev_frame_time)
prev_frame_time = new_frame_time 
# Hitung Data Rate 
frame_size_bytes = img.nbytes # Ukuran frame dalam byte data_rate_bps = frame_size_bytes * fps * 8 
data_rate_kbps = data_rate_bps / 1000 
data_rate_mbps = data_rate_kbps / 1000 
# Cetak Informasi 
print(f"Frame Rate: {fps:.2f} FPS") 
print(f"Data Rate: {data_rate_mbps:.2f} Mbps") 
cv2.imshow("Image", img) 
if cv2.waitKey(1) & 0xFF == ord('q'): 
break 
cap.release() 
cv2.destroyAllWindows() 
client.disconnect() 
print("Disconnected from MQTT Broker")
