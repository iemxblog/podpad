import paho.mqtt.client as mqtt

OPEN = 1
CLOSE = 0
DOOR = 0
BEDROOM = 1

def publishMessage(topic, payload):
    client = mqtt.Client()
    client.connect("iemxblog.fr", 1883, 60)
    client.loop_start()
    client.publish(topic, payload, 2)
    client.loop_stop()
    client.disconnect()

def openDoor():
    publishMessage("/shutter/door", OPEN)

def closeDoor():
    publishMessage("/shutter/door", CLOSE)

def openBedroom():
    publishMessage("/shutter/bedroom", OPEN)

def closeBedroom():
    publishMessage("/shutter/bedroom", CLOSE)
