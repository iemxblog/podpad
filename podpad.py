import os
import sound
import feeds
import streams

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
                os.system("reboot") 
        elif l == "*":
            sound.click()
            stream_number = stack.pop()
            streams.queue_stream(stream_number)
        elif l == "**":
            sound.click()
            feed_number = stack.pop()
            feeds.queue_last_episode(feed_number)
            sound.click()
        elif l == ".":
            sound.click()
            os.system("mpc toggle")
        elif l == "..":
            sound.click()
            os.system("mpc clear")
            stack = []
        else:
            sound.failure()
    except Exception as e:
        sound.failure()
        print(e)
