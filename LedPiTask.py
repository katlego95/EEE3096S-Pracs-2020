import RPi.GPIO as GPIO
import time

#def main():
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

	#turning LED on and Off
        GPIO.output(LEDPin,True)
        print ("LED ON")
        time.sleep(2)
        GPIO.output(LEDPin,False)
        print ("LED OFF")
  
        print ("Ready! you can press the button")
        while True:
		#Push button toggles LED
                GPIO.output(LEDPin, not GPIO.input(buttonPin))
                time.sleep(.1)
  
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
