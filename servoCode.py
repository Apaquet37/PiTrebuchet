#This code works really well. It rotates two servos in sync and is incredibly smooth.

from gpiozero.pins.pigpio import PiGPIOFactory #gpiozero to reduce servo jitter
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(18) #The first servo is in pin 18 (on the t-cobbler)
servo2 = Servo(21) #The second servo is i npin 21 (on the t-cobbler)

while True:
    servo.min() #Put both servos to 0 ish degrees
    servo2.min()
    sleep(1) #Wait a second
    servo.mid() #Move the servos to a mid range angle
    servo2.mid()
    sleep(1) #Wait a second
    servo.max() #Move the servos to their max value (not quite 180 degrees)
    servo2.max()
    sleep(1) #Wait a second before resetting
