import paho.mqtt.client as mqtt
broker_adress = "broker.hivemq.com"
client = mqtt.Client("team!")
client.connect(broker_adress)
print('Connected to %s MQTT broker' % broker_adress)
client.subscribe("ME35")

# client.publish("ME35","Hi")

def game(number):
    if number == 1:
        print ("Hooray!")
    else:
        print("Wrong")

#testing 123
'''
sdfsdlkj aslkdfjs;df
asdfad'[osfja
sd[pfos
GKJAKSFDJG
PFSOJG
PSD]]'''

def __init__():
    print("Hello world")

def verifySentence(user, correct):
    if user == correct:
        value = True
    else:
        value = False
    return value

#helllllloooooo
