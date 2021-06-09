from gpiozero.pins.pigpio import PiGPIOFactory #All the necessary imports for the servos
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(18) #Two servos, one on pin 18 and one on 21
servo2 = Servo(21)

while True: #Forever loop
  angle = float(input("Angle (between 1 and -1):")) #Prompt the user to input an angle and convert it to a float
  print(angle) #Print the angle just to make sure the code is working
  servo.value = angle #Move the first servo to the angle
  sleep(3) #Wait for 3 seconds
  servo.value = 0 #Move the servo back to zero (the middle, 90ish degrees)
  sleep(1) #Wait for 1 second before starting the loop again
 
