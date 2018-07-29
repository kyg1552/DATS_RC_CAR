import RPi.GPIO as GPIO
from time import sleep
from tkinter import *
from dats.core.client import streamer
MOTOR1A = 22 # Front_back Motor PIN number
MOTOR1B = 24 # Front_back Motor PIN number

MOTOR2A = 23 # left_right Motor PIN number
MOTOR2B = 25 # left_right Motor PIN number
#--------------------------------------------

pwmpin1 = 12
pwmpin2 = 13
pwm_freq = 20*1000  # PWM frequence
duty1 = 0
duty2 = 0
#--------------------------------------------

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)
GPIO.setup(pwmpin1, GPIO.OUT)	#PWM_ control PIN1
GPIO.setup(pwmpin2, GPIO.OUT)   #PWM_ control PIN2
p1 = GPIO.PWM(pwmpin1,  pwm_freq) # pwmPin1_frequence setting
p1.start( duty1 )
p2 = GPIO.PWM(pwmpin2,  pwm_freq) # pwmPin2_frequence setting
p2.start( duty2 )
tm = 0.02
left = 0
right = 0
#-------------------------------------------------------------------------#
def response(streamer, recv_data):
	print('enter-------------------------------------------------')
	if recv_data == bytearray([0,1,0]):
		print('forward')
		duty1 = 10
		p1.ChangeDutyCycle(duty1 )
		GPIO.output(MOTOR1A, 1)
		GPIO.output(MOTOR1B, 0)
#		sleep(tm)
#		stop()

#	def back(duty):
#		duty1 = duty
#		p1.ChangeDutyCycle(duty1 )
#		GPIO.output(MOTOR1A, 1)
#		GPIO.output(MOTOR1B, 1)
#		sleep(tm)
#		stop()

	if recv_data == bytearray([1,0,0]):
		print('left')
		left = 1
		duty2 = 10
		p2.ChangeDutyCycle(duty2)
		GPIO.output(MOTOR2A,1)
		GPIO.output(MOTOR2B,0)
#		sleep(tm)
#		stop()

	if recv_data == bytearray([0,0,1]):
		print('right')
		right = 1
		duty2 = 10
		p2.ChangeDutyCycle(duty2)
		GPIO.output(MOTOR2A,1)
		GPIO.output(MOTOR2B,1)
#		sleep(tm)
#		stop()

#	def stop() :
#		p1.ChangeDutyCycle(0)

#		p2.ChangeDutyCycle(0)
#		GPIO.output(MOTOR1A,0)
#		GPIO.output(MOTOR1B,0)
#		GPIO.output(MOTOR2A,0)
#		GPIO.output(MOTOR2B,0)
#		duty1 = 0
#		duty2 = 0
	
# 	if left == 1:
#    		for n in range(3):
#			 right(100)
#	    right = 0
#	    letf = 0
#	elif right == 1:
#	    for n in range(3):
#		 left(100)
#	    right = 0
#	    left = 0

#-----------------------------------------------------------------------#

#def key_input(event):
#	print('Key',event.char)
#	key_press = event.char

#	if key_press.lower() == 'w':
#		forward(100)
#	elif key_press.lower() =='s':
#		back(100)
#	elif key_press.lower() =='d':
#		right(80)
#	elif key_press.lower() == 'a':
#		left(80)
#	elif key_press.lower() == 'x':
#		stop()

#------------------------------------------------------------------#
#command = Tk()
#command.bind('<KeyPress>', key_input)
#command.mainloop()
s = streamer(remote_model_url = '192.168.0.2')
s.set_ffmpeg_flag(streamer.MACOS_FACETIME_PRESET)
s.set_model_respones_callback(response)
s.start()
