import RPi.GPIO as GPIO

relayPin = 4
LIGHTOFF = 0
LIGHTON = 1
relayFlag = LIGHTOFF

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.IN)

def toggle():
    global relayFlag
    if relayFlag == LIGHTOFF:
        on()
    else:
        off()

def on():
    global relayFlag
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin, 0)
    relayFlag = LIGHTON

def off():
    global relayFlag
    GPIO.setup(relayPin, GPIO.IN)
    relayFlag = LIGHTOFF

