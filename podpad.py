import os
import time
import sound
import feeds
import streams
import shutters
import RPi.GPIO as GPIO

relayPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.IN)

LIGHTOFF = 0
LIGHTON = 1
relayFlag = LIGHTOFF

stack = []

sound.startup()

while True:
    l = input("> ")
    try:
        if l.isdecimal():
            sound.click()
            stack.append(int(l))
        elif l == "/":
            sound.click()
            cmd = stack.pop()
            if cmd == 0:
                sound.shutdown()
                os.system("sudo reboot") 
            elif cmd == 1:
                action = stack.pop()
                shutter = stack.pop()
                if action == shutters.OPEN:
                    if shutter == shutters.DOOR:
                        shutters.openDoor()
                    elif shutter == shutters.BEDROOM:
                        shutters.openBedroom()
                    else:
                        raise RuntimeError("No such shutter.")
                if action == shutters.CLOSE:
                    if shutter == shutters.DOOR:
                        shutters.closeDoor()
                    elif shutter == shutters.BEDROOM:
                        shutters.closeBedroom()
                    else:
                        raise RuntimeError("No such shutter.")
            elif cmd == 2:
                shutters.openDoor()
                time.sleep(1)
                shutters.openBedroom()
            elif cmd == 3:
                if relayFlag == LIGHTOFF:
                    print("Turning light on")
                    GPIO.setup(relayPin, GPIO.OUT)
                    GPIO.output(relayPin, 0)
                    relayFlag = LIGHTON
                else:
                    print("Turning light off")
                    GPIO.setup(relayPin, GPIO.IN)
                    relayFlag = LIGHTOFF
            else:
                raise RuntimeError("No such command.")

        elif l == "*":
            sound.click()
            stream_number = stack.pop()
            streams.queue_stream(stream_number)
        elif l == "**":
            sound.click()
            feed_number = stack.pop()
            feeds.queue_last_episode(feed_number)
            sound.click()
        elif l == "***":
            sound.click()
            feed_number = stack.pop()
            feeds.download_and_queue_last_episode(feed_number)
            sound.click()
        elif l == ".":
            sound.click()
            os.system("mpc toggle")
        elif l == "..":
            sound.click()
            os.system("mpc clear")
            stack = []
        elif l == "...":
            sound.click()
            playlist_number = stack.pop()
            os.system("mpc load playlist{0}".format(playlist_number)) 
        elif l == "+":
            sound.click()
            os.system("mpc volume +5")
        elif l == "-":
            sound.click()
            os.system("mpc volume -5")
        elif l == "++":
            sound.click()
            os.system("mpc seek +1%")
        elif l == "--":
            sound.click()
            os.system("mpc seek -1%")
        elif l == "---":
            sound.click()
            os.system("mpc prev")
        elif l == "+++":
            sound.click()
            os.system("mpc next")
        elif l == "+-" or l == "-+":
            sound.click()
            amount = stack.pop()
            os.system("mpc seek {0}%".format(amount))
        else:
            sound.failure()
    except Exception as e:
        sound.failure()
        print(e)
