#Code for a servo to adjust the angle of the release pin
import RPi.GPIO as GPIO
import time

global pwm
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(0)


while True:
	pwm.ChangeDutyCycle(5)
	print("moving")
	time.sleep(1)
	setDirection(0)
	print("end")
