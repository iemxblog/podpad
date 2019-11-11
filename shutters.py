import paho.mqtt.client as mqtt

OPEN = 1
CLOSE = 0
DOOR = 0
BEDROOM = 1

QOS = 2

client = None

def init(c):
    global client
    client = c

def publishMessage(topic, payload):
    client = mqtt.Client()
    client.connect("iemxblog.fr", 1883, 60)
    client.loop_start()
    client.publish(topic, payload, 2)
    client.loop_stop()
    client.disconnect()

def openDoor():
    global client
    client.publish("/shutter/door", OPEN, QOS)

def closeDoor():
    global client
    client.publish("/shutter/door", CLOSE, QOS)

def openBedroom():
    global client
    client.publish("/shutter/bedroom", OPEN, QOS)

def closeBedroom():
    global client
    client.publish("/shutter/bedroom", CLOSE, QOS)
