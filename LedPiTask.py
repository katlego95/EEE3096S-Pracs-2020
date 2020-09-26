import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

LEDPin = 22

# setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)
