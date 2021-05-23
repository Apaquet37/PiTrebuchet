import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo1 = Servo(18)
servo2 = Servo(21)


while True:
  angle = float(input("Angle (between 1 and -1):"))
  if GPIO.input(13) == GPIO.HIGH and buttonState == 0:
    print("Button pressed")
    buttonState = 1
    servo1.value = angle
    servo2.value = -1
  if GPIO.input(13) == GPIO.LOW:
    servo1.value = 0
    servo2.value = 1
    buttonState = 0
