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
  if GPIO.input(13) == GPIO.HIGH and buttonState == 0: #Has the button been pressed?
    print("Button pressed") #Print to the screen so I know
    angle = float(input("Angle (between 1 and -1):")) #Ask the user to input an angle, convert that angle to a float
    buttonState = 1 #A condition to make sure the loop only happens once per press
    servo1.value = angle #Move the servo to the user inputted angle
    servo2.value = -1 #Move a second servo to the other side
  if GPIO.input(13) == GPIO.LOW: #When the button is not being pressed
    print("Button off") #Print button off
    servo1.value = 0 #Reset the servo
    servo2.value = 1 #Move the other servo to the otehr side
    buttonState = 0 #Reset the buttonstate
