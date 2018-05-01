import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

while True:
	GPIO.output(18, True)
	GPIO.output(27, True)
	time.sleep(5)
	GPIO.cleanup()


