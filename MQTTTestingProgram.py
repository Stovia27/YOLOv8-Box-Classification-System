MQTT Testing  
import paho.mqtt.client as mqtt 
# Konfigurasi MQTT 
broker_address = "test.mosquitto.org" # Ganti dengan broker lokal jika ada port = 1883 
topic = "servo/angle" # Topik untuk komunikasi dengan NodeMCU 
# Callback ketika terhubung ke broker 
def on_connect(client, userdata, flags, rc): 
if rc == 0: 
print("Connected to MQTT Broker!") 
else: 
print("Failed to connect, return code %d\n", rc) 
# Inisialisasi client MQTT 
client = mqtt.Client() 
client.on_connect = on_connect 
client.connect(broker_address, port, 60) 
# Fungsi untuk mengirimkan nilai derajat 
def send_angle(angle): 
if 0 <= angle <= 180: # Validasi input 
client.publish(topic, str(angle)) 
print(f"Sent angle: {angle}°") 
else: 
print("Invalid angle. Please enter a value between 0 and 45.") 
# Main program 
client.loop_start() # Start MQTT loop
try: 
while True: 
user_input = input("Enter angle (0 or 45): ") if user_input.isdigit(): 
angle = int(user_input) 
send_angle(angle) 
else: 
print("Invalid input. Please enter a number.") 
except KeyboardInterrupt: 
print("Program terminated.") 
client.loop_stop()
