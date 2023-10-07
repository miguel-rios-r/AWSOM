import paho.mqtt.client as mqtt

mqtt_cli = mqtt.Client()

# Broker info
broker_address = "34.41.169.80"
port = 1883

#Broker credentials
username = "awsom-user"
password = "Hb5Rj9qL"

mqtt_cli.username_pw_set(username, password) 

def on_connect(mqtt_cli, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa al servidor MQTT")
        mqtt_cli.subscribe("test")
    else:
        print(f"Fallo en la conexión al servidor MQTT, código de retorno: {rc}")

# Callback que se ejecuta cuando se recibe un mensaje en el tema al que estás suscrito
def on_message(mqtt_cli, userdata, msg):
    print(f"Mensaje recibido en el tema '{msg.topic}': {msg.payload.decode()}")
    mqtt_cli.publish("response", "Message received in Python client") 

# Configura los callbacks
mqtt_cli.on_connect = on_connect
mqtt_cli.on_message = on_message

# Conéctate al servidor MQTT
mqtt_cli.connect(broker_address, port, 60)

# Inicia el bucle para mantener la conexión
mqtt_cli.loop_forever()