#This code is relatively twitchy, but it just moves a single servo back and forth in increments of varying angles and speeds.

import RPi.GPIO as GPIO
import time

P_SERVO = 12 # look at a pin map, it's 12 if counting but labelled #18 on the T-cobbler
fPWM = 50  # Hz (not higher with software PWM)
a = 10
b = 2

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)
    time.sleep(1) # allow to settle
   
print("starting")
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
GPIO.cleanup() 
print("done")
