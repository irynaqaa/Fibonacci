import paho.mqtt.client as mqtt

MQTT_BROKER = 'mqtt_broker_address'
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('iot/data')

def on_message(client, userdata, msg):
    # Process incoming MQTT message
    print(msg.topic + ' ' + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()
