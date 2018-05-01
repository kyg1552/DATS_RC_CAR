import RPi.GPIO as GP
import time

GP.setmode(GP.BOARD)
GP.setup(7,GP.OUT)
SERVO = GP.PWM(7,50)
SERVO.start(0)

while True:
	SERVO.ChangeDutyCycle(11)
	time.sleep(1.5)
GP.cleanup()
