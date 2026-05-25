Servo Motor Testing  
#include <ESP8266WiFi.h> 
#include <PubSubClient.h> 
#include <Servo.h> 
// WiFi credentials 
const char* ssid = "UNAND 2"; // Ganti dengan SSID Wi-Fi const char* password = "HardiknasDiAndalas"; // Ganti dengan password Wi-Fi 
// MQTT broker 
const char* mqtt_server = "test.mosquitto.org"; // Ganti jika pakai broker lokal 
WiFiClient espClient; 
PubSubClient client(espClient); 
Servo myServo; 
const int servoPin = D4; // Pin servo (D1 di NodeMCU) 
// Callback untuk menerima pesan MQTT 
void callback(char* topic, byte* payload, unsigned int length) { String message; 
for (int i = 0; i < length; i++) { 
message += (char)payload[i]; 
} 
Serial.print("Message arrived: "); 
Serial.println(message); 
// Pastikan pesan dapat dikonversi menjadi angka valid 
if (message.toInt() || message == "0") {
int angle = message.toInt(); // Konversi pesan menjadi angka if (angle >= 0 && angle <= 180) { 
myServo.write(angle); // Putar servo sesuai nilai Serial.print("Servo moved to: "); 
Serial.println(angle); 
} else { 
Serial.println("Invalid angle (out of range)."); 
} 
} else { 
Serial.println("Invalid message received (not a number)."); } 
} 
// Setup WiFi 
void setup_wifi() { 
delay(10); 
Serial.println(); 
Serial.print("Connecting to "); 
Serial.println(ssid); 
WiFi.begin(ssid, password); 
while (WiFi.status() != WL_CONNECTED) { 
delay(500); 
Serial.print("."); 
} 
Serial.println(""); 
Serial.println("WiFi connected"); 
Serial.println("IP address: "); 
Serial.println(WiFi.localIP());
} 
// Setup program 
void setup() { 
Serial.begin(9600); 
setup_wifi(); 
client.setServer(mqtt_server, 1883); 
client.setCallback(callback); 
myServo.attach(servoPin); 
myServo.write(0); // Inisialisasi servo di posisi 0 
Serial.println("Servo initialized at 0 degrees"); 
} 
void reconnect() { 
while (!client.connected()) { 
Serial.print("Attempting MQTT connection..."); 
if (client.connect("ESP8266Client")) { 
Serial.println("connected"); 
client.subscribe("servo/angle"); // Ganti dengan topik yang diinginkan Serial.println("Subscribed to topic: servo/angle"); 
} else { 
Serial.print("failed, rc="); 
Serial.print(client.state()); 
Serial.println(" try again in 5 seconds"); 
delay(5000); 
} 
} 
}
void loop() { 
if (!client.connected()) { reconnect(); 
} 
client.loop(); 
}
