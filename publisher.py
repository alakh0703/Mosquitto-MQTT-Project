import paho.mqtt.client as mqtt
import time
import json
from data_generator import create_data2
from util import create_data


# broker_address = "localhost"
# topic = "Temperature Sensor"
topic= "Util Dictionary"


client = mqtt.Client()

client.connect('localhost',1883)

while True:
    data = create_data()
    # data = create_data2((18, 3),(1, 0.0001),(10,2))
    payload = json.dumps(data)
    client.publish(topic, payload)
    print("Sent message:", payload)
    time.sleep(5)

client.disconnect()