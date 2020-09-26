import RPi.GPIO as GPIO
import time

#GPIO Pins
LEDPin = 22
buttonPin = 5

#variable to hold last known state of LED
last_LED_state = False

#call back funtion when falling edge is detected on push button
#def my_callback(buttonPin):
	print("Button Pressed")
	global last_LED_state
    	GPIO.output(LEDPin, not last_LED_state)
	if last_LED_state:
		print ("LED OFF")
	else:
		print ("LED ON")
    	last_LED_state = not last_LED_state

#def main():
	GPIO.setmode(GPIO.BCM)
	# setup the pin the LED is connected to
	GPIO.setup(LEDPin, GPIO.OUT)
	# setup the push button pin
	GPIO.setup(buttonPin, GPIO.IN,pull_up_down= GPIO.PUD_UP)
	#LED defualt state
	GPIO.output(LEDPin,False)

	#turning LED on and Off
        GPIO.output(LEDPin,True)
        print ("LED ON")
        time.sleep(2)
        GPIO.output(LEDPin,False)
        print ("LED OFF")
  
        print ("Ready! you can press the button")
        while True:
		#waiting for falling edge detection
		GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=my_callback, bouncetime=200)
                time.sleep(.2)
  
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        GPIO.cleanup()
    except e:
        print("Some other error occurred: {}".format(e.message)})
        GPIO.cleanup()
