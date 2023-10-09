#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "MIMSLAB_STUDIO";
const char* password = "MimsLAAB";
const char* mqtt_server = "34.41.169.80"; // O URL del servidor MQTT
const char* mqtt_user = "awsom-user";
const char* mqtt_password = "Hb5Rj9qL";
const char* mqtt_function_topic = "device/function";

const int ledPin = 2;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conexión WiFi establecida");
  Serial.println("Dirección IP obtenida: ");
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
  // Convierte el payload en una cadena de caracteres
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  // Verifica si el mensaje proviene del tema "led/control" y actúa en consecuencia
  if (String(topic) == mqtt_function_topic) {
    if (message == "ON") {
      digitalWrite(ledPin, HIGH);
      
      client.publish("device/function/response", "Function ON executed");
    } else if (message == "OFF") {
      digitalWrite(ledPin, LOW);
      
      client.publish("device/function/response", "Function OFF executed");
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Conectando al servidor MQTT...");
    if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      Serial.println("Conexión exitosa");
      client.subscribe(mqtt_function_topic); // Suscríbete al tema MQTT
      client.publish("device/check", "Device conneted");
    } else {
      Serial.print("Fallo en la conexión, código de retorno=");
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