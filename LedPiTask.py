import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LEDPin = 22
buttonPin = 5

# setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)
# setup the push button
GPIO.setup(buttonPin, GPIO.IN,pull_up_down= GPIO.PUD_UP)

#initial state of LED and push button
LEDState = False
ButtonState = True

#turning LED on and Off
LEDState = True
GPIO.output(LEDPin, LEDState)
time.sleep(2)
LEDState = False
GPIO.output(LEDPin,LEDState)





