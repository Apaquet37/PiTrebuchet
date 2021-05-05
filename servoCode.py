from gpiozer.pins.pigpio import PiGPIOFactory
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(18)
servo2 = Servo(21)

while True:
    servo.min()
    servo2.min()
    sleep(1)
    servo.mid()
    servo2.mid()
    sleep(1)
    servo.max()
    servo2.max()
    sleep(1)
