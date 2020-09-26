import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO pins
LEDPin = 22
buttonPin = 5

# setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)
# setup the push button pin
GPIO.setup(buttonPin, GPIO.IN,pull_up_down= GPIO.PUD_UP)
#LED defualt state
GPIO.output(LEDPin,False)

try:
	#turning LED on and Off
	GPIO.output(LEDPin,True)
	print ("LED ON")
	time.sleep(2)
	GPIO.output(LEDPin,False)
	Print ("LED OFF")
        
	print ("Ready you can press the button")
	while True:
		#Push button toggles LED 
		GPIO.output(LEDPin, not GPIO.input(buttonPin))
		time.sleep(.1)
		
finally:
	#Reset the GPIO pins to a safe state
	GPIO.output(LEDPin,False)
	GPIO.cleanup()
