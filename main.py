import paho.mqtt.client as mqtt
broker_adress = "broker.hivemq.com"
client = mqtt.Client("team!")
client.connect(broker_adress)
print('Connected to %s MQTT broker' % broker_adress)
client.subscribe("ME35")

# client.publish("ME35","Hi")


