import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

MOTOR1_1 = 0 # Front Motor PIN number
MOTOR1_2 = 0 # Front Motor PIN number
MOTOR2_1 = 0 # back Motor PIN number
MOTOR2_2 = 0 # back Motor PIN number
Servo = 0    #ServoMotor PIN number
pwm_duty = 0 # PWM duty rate
pwm_frequence = 0 # PWM frequence
pwm_leftsignal = 0 # left PWM _ServoMotor
pwm_rightsignal = 0  # right PWM _ServoMotor

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(MOTOR1_1, GPIO.OUT)
	GPIO.setup(MOTOR1_2, GPIO.OUT)
	GPIO.setup(MOTOR2_1, GPIO.OUT)
	GPIO.setup(MOTOR2_2, GPIO.OUT)
	GPIO.setup(Servo, GPIO.OUT)	#PWM _ ServoMotor control PIN
	p=GPIO.PWM(Servo,pwm_frequence) # pwmPin_frequence setting
#-------------------------------------------------------------------------#	
def forward(tf):
	init()
	GPIO.output(MOTOR1_1, 1)
	GPIO.output(MOTOR1_2, 0)
	sleep(tf)
	GPIO.cleanup()

def back(tf):
	init()
	GPIO.output(MOTOR2_1, 1)
	GPIO.output(MOTOR2_2, 0)
	sleep(tf)
	GPIO.cleanup()

def left(tf):
	init()
	p.ChangeDutyCycle(pwm_leftsignal)
	sleep(tf)
	GPIO.cleanup()

def right(tf):
	init()
	p.ChangeDutyCycle(pwm_rightsignal)
	sleep(tf)
	GPIO.cleanup()
#-----------------------------------------------------------------------#
def for_right(tf):
        init()
        GPIO.output(MOTOR1_1, 1)
        GPIO.output(MOTOR1_2, 0)
	p.ChangeDutyCycle(pwm_rightsignal)
        sleep(tf)
        GPIO.cleanup()

def for_left(tf):
        init()
        GPIO.output(MOTOR1_1, 1)
        GPIO.output(MOTOR1_2, 0)
	p.ChangeDutyCycle(pwm_leftsignal)
        sleep(tf)
        GPIO.cleanup()

def back_right(tf):
        init()
        GPIO.output(MOTOR2_1,1)
        GPIO.output(MOTOR2_2,0)
	p.ChangeDutyCycle(pwm_rightsignal)
        sleep(tf)
        GPIO.cleanup()

def back_left(tf):
        init()
        GPIO.output(MOTOR2_1, 1)
        GPIO.output(MOTOR2_2, 0)
	p.ChangeDutyCycle(pwm_leftsignal)
        sleep(tf)
        GPIO.cleanup()
#---------------------------------------------------------------------#	

def key_input(event):
	init()
	print('Key',event.char)
	key_press = event.char
	sleep_time = 0.03

	if key_press.lower() == 'w':
		forward(sleep_time)
	elif key_press.lower() =='a':
		left(sleep_time)
	elif key_press.lower() =='d':
		right(sleep_time)
	elif key_press.lower() == 's':
		back(sleep_time)
	elif key_press.lower() == 'wa':
		for_left(sleep_time)
	elif key_press.lower() == 'wd':
                for_right(sleep_time)
	elif key_press.lower() == 'sa':
                back_left(sleep_time)
	elif key_press.lower() == 'sd':
		back_right(sleep_time)

#------------------------------------------------------------------#
command = Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()	
