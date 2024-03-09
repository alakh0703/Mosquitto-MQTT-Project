import paho.mqtt.client as mqtt
import json
from data_generator import print_data
from util import create_data,print_data2

# broker_address = "localhost"
# topic = "Temperature Sensor"
topic= "Util Dictionary"


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data = json.loads(payload)
    print_data2(data)

client = mqtt.Client()
client.on_message = on_message
client.connect('localhost',1883)

# client.connect(broker_address)
client.subscribe(topic)

print("Subscribed to topic:", topic)

client.loop_forever()