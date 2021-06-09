#Incomplete, but the start of combining all the code for our project, just servo set up right now

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(18)
servo2 = Servo(21)

while True:

