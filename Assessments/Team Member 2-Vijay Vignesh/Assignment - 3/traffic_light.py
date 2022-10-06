import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
red=11
yellow=13
green=15
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

while True:
    GPIO.output(red, True) 
    time.sleep(3)
    GPIO.output(yellow, True) 
    time.sleep(1)
    GPIO.output(red, False) 
    GPIO.output(yellow, False) 
    GPIO.output(green, True)
    time.sleep(5)
    GPIO.output(green, False) 
    GPIO.output(yellow, True) 
    time.sleep(2)
    GPIO.output(yellow, False)
