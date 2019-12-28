import RPi.GPIO as GPIO

relayPin = 4
LIGHTOFF = 0
LIGHTON = 1
relayFlag = LIGHTOFF

client = None

def init(c):
    global client
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.IN)
    client = c
    client.on_connect = on_connect
    client.on_message = on_message

def toggle():
    global relayFlag
    if relayFlag == LIGHTOFF:
        client.publish("/light/bedroom", payload = "1", qos = 0, retain = True)
    else:
        client.publish("/light/bedroom", payload = "0", qos = 0, retain = True)

def on(c):
    global relayFlag
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin, 0)
    relayFlag = LIGHTON
    c.publish("/light/bedroom/status", payload = "1", qos = 0, retain = True)


def off(c):
    global relayFlag
    GPIO.setup(relayPin, GPIO.IN)
    relayFlag = LIGHTOFF
    c.publish("/light/bedroom/status", payload = "0", qos = 0, retain = True)

def on_connect(c, userData, flags, rc):
    c.subscribe("/light/bedroom")

def on_message(c, userData, msg):
    if msg.topic == "/light/bedroom" and int(msg.payload) == 0:
        off(c)
    elif msg.topic == "/light/bedroom" and int(msg.payload) == 1:
        on(c)

