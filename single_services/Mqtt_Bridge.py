import paho.mqtt.client as mqtt

mqtt_cli = mqtt.Client()

broker_address = "34.41.169.80"
port = 1883
username = "awsom-user"
password = "Hb5Rj9qL"

led_status = False

mqtt_cli.username_pw_set(username, password) 

def on_connect(mqtt_cli, userdata, flags, rc):
    if rc == 0:
        print()
        mqtt_cli.subscribe("device/function/response")
    else:
        print(f"Fallo en la conexión al servidor MQTT, código de retorno: {rc}")

# def on_message(mqtt_cli, userdata, msg):
	# print(f"Mensaje recibido en el tema '{msg.topic}': {msg.payload.decode()}")

mqtt_cli.on_connect = on_connect
print("Conexión exitosa al servidor MQTT")

mqtt_cli.connect(broker_address, port, 60)
mqtt_cli.loop_start()

user_input = ""
while user_input != "exit":
  user_input = input("Type 'on', 'off' or 'exit'': ")

  if user_input == "on":
  	mqtt_cli.publish("device/function", "ON")

  if user_input == "off":
  	mqtt_cli.publish("device/function", "OFF")

print()
input("Presiona Enter para detener el cliente MQTT...")

mqtt_cli.loop_stop()
mqtt_cli.disconnect()