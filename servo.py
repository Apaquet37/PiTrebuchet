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
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18,GPIO.LOW)
	time.sleep(1)
	print("end")
