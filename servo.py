#This code should theoretically move two servos back and forth, but it currently only adjusts one, and it is pretty twitchy

#Code for a servo to adjust the angle of the release pin
import RPi.GPIO as GPIO
import time

servoPin = 18
servoPin2 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)

pwm = GPIO.PWM(servoPin, 50)
pwm2 = GPIO.PWM(servoPin2, 50)
pwm.start(2.5) # Initialization

try:
  while True:
    pwm.ChangeDutyCycle(5)
    pwm2.ChangeDutyCycle(5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.5)
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(10)
    pwm2.ChangeDutyCycle(10)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(12.5)
    pwm2.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(10)
    pwm2.ChangeDutyCycle(10)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.5)
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(5)
    pwm2.ChangeDutyCycle(5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(2.5)
    pwm2.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  pwm.stop()
  pwm2.stop()
  GPIO.cleanup()
