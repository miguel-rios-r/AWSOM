import paho.mqtt.client as mqtt
import time

mqtt_cli = mqtt.Client()

broker_address = env.mqtt.server
port = env.mqtt.port
username = env.mqtt.user
password = env.mqtt.pass

led_status = False

mqtt_cli.username_pw_set(username, password) 

print("connecting...")

def sendAlerts():
    print("Sending alerts...")

def turnOffIOT():
    print("Turn off IOT systems...")
    time.sleep(1)
    mqtt_cli.publish("device/function", "OFF")


def on_connect(mqtt_cli, userdata, flags, rc):
    if rc == 0:
        print()
        print("Conneted to mqtt real time server")
        mqtt_cli.subscribe("device/function/response")
    else:
        print(f"Fallo en la conexión al servidor MQTT, código de retorno: {rc}")

def on_message(mqtt_cli, userdata, msg):
	print(f"'{msg.topic}': {msg.payload.decode()}")
    if msg == "{status: INTENSE, range: 7}":
        sendAlerts()
        turnOffIOT()

def connect_to_data_analysis():
    print("Conneted to data analyst")

mqtt_cli.on_connect = on_connect
print("Conexión exitosa al servidor MQTT")

mqtt_cli.connect(broker_address, port, 60)
mqtt_cli.loop_start()

mqtt_cli.publish("device/function", "ON")

print("")
time.sleep(1)

# TESTING ONLY :D
# user_input = ""
# while user_input != "exit":
#   user_input = input("Type 'on', 'off' or 'exit'': ")

#   if user_input == "on":
#   	mqtt_cli.publish("device/function", "ON")

#   if user_input == "off":
#   	time.sleep(15)
#   	mqtt_cli.publish("device/function", "OFF")

print()
input("Presiona Enter para detener el cliente MQTT...")

mqtt_cli.loop_stop()
mqtt_cli.disconnect()
