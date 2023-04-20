import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)



count = 2 
for i in range(count):
	# Turn on each LED in sequence
	GPIO.output(17, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(22, GPIO.LOW)

# Clean up GPIO pins
GPIO.cleanup()
