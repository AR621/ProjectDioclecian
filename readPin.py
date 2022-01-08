import RPi.GPIO as GPIO
import time

def readPin(datapin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(datapin, GPIO.IN)
    state = GPIO.input(datapin)
    return state

print(readPin(21))
