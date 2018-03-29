import os

def click():
    os.system("aplay click.wav")

def failure():
    os.system("aplay failure.wav")

def shutdown():
    os.system("aplay shutdown.wav")

def startup():
    os.system("aplay startup.wav")
