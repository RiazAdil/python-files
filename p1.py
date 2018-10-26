import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PirPin=6
GPIO.setup(PirPin,GPIO.IN)
counter=1
time.sleep(4)

while True:
    if GPIO.input(PirPin):
        print("Motion Detected")

        time.sleep(1)
        counter=counter+1
        print('True')
    else:
        print("no motion ")
