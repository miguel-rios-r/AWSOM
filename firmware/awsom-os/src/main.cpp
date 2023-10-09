#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = env.wifi.ssid;
const char* password = env.wifi.pass;
const char* mqtt_server = env.mqtt.server;
const char* mqtt_user = env.mqtt.user;
const char* mqtt_password = env.mqtt.pass;
const char* mqtt_function_topic = env.mqtt.topic;

const int ledPin = 2;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connected to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");;
  Serial.println(WiFi.localIP());

  digitalWrite(ledPin, HIGH);
  
  delay(500);
  digitalWrite(ledPin, LOW);
  
  delay(200);
  digitalWrite(ledPin, HIGH);
  
  delay(500);
  digitalWrite(ledPin, LOW);
  

}

void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  if (String(topic) == mqtt_function_topic) {
    if (message == "ON") {
      digitalWrite(ledPin, HIGH);
      
      client.publish(env.mqtt.responseTopic, "Function ON executed");
    } else if (message == "OFF") {
      digitalWrite(ledPin, LOW);
      
      client.publish(env.mqtt.responseTopic, "Function OFF executed");
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      client.subscribe(mqtt_function_topic);
      client.publish(env.mqtt.checkTopic, "Device conneted");
    } else {
      Serial.println(client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}