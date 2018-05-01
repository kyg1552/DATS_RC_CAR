import RPi.GPIO as IO
import time

pwmPin = 23
dirPin = 24

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pwmPin,IO.OUT)
IO.setup(dirPin,IO.OUT)

p = IO.PWM(pwmPin, 100)
p.start(0)

while 1:
   IO.output(dirPin, True)
   for x in range(100) :
      p.ChangeDutyCycle(x)
      time.sleep(0.1)
   time.sleep(0.5)
   for x in range(100,0,-1) :
      p.ChangeDutyCycle(x)
      time.sleep(0.1)
   time.sleep(0.5)
   IO.output(dirPin,False)
   for x in range(100):
      p.ChangeDutyCycle(x)
      time.sleep(0.1)
   time.sleep(0.5)
   for x in range(100,0,-1):
      p.ChangeDutyCycle(x)
      time.sleep(0.1)
