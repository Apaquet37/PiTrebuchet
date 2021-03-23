#Code for a servo to adjust the angle of the release pin
import RPi.GPIO as GPIO
import time

servoPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
pwm.start(2.5) # Initialization

try:
  while True:
    pwm.ChangeDutyCycle(5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(10)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(10)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(5)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
