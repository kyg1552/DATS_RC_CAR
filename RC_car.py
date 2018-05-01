import RPi.GPIO as GPIO
import time
from tkinter import *

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
def forward(tf):
	init()
	
	GPIO.output(18, 1)
	GPIO.output(27, 0)
	
	time.sleep(tf)
	GPIO.cleanup()
def back(tf):
	init()
	GPIO.output(18, 0)
	GPIO.output(27, 1)
	time.sleep(tf)
	GPIO.cleanup()
def left(self):
	init()
	GPIO.output(22, 1)
	GPIO.output(23, 0)
	time.sleep(0.03)
	GPIO.cleanup()
def right(self):
	init()
	GPIO.output(22, 0)
	GPIO.output(23,1)
	time.sleep(0.03)
	GPIO.cleanup()
	

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

command = Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()	
