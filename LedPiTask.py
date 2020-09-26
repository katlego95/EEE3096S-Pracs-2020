import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

LEDPin = 22
buttonPin = 5

# setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)

# setup the push button
GPIO.setup(buttonPin, GPIO.IN,pull_up_down= GPIO.PUD_UP)

buttonState= True
ledState = False
