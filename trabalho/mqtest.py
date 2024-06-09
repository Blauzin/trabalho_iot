import paho.mqtt.client as mqtt
import json

# Definir o broker e os tópicos
broker = "broker.hivemq.com"
port = 1883
topic_sensor1 = "leakspy/sensor1"
topic_sensor2 = "leakspy/sensor2"
topic_actuators = "leakspy/actuators"

# Função que será chamada quando a conexão for estabelecida
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe([(topic_sensor1, 0), (topic_sensor2, 0), (topic_actuators, 0)])
    print(f"Subscribed to topics: {topic_sensor1}, {topic_sensor2}, {topic_actuators}")

# Função que será chamada quando uma mensagem for recebida
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Parsed payload: {payload}")
    except json.JSONDecodeError:
        print("Failed to decode JSON")

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao broker MQTT
client.connect(broker, port, 60)

# Iniciar o loop para processar mensagens recebidas
client.loop_forever()
