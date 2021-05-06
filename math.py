import math

mCW = 1.16 #mass of counterweight in kg (2 washers weighing .58 each)
g = 9.81 #gravity in Newtons 
hCWI = 0.26 #initial height of counterweight in m
w = #rotational velocity (angular velocity?) in rad/sec
hCWF = 0.03 #final height of counterweight in m
mP = input("Mass of projectile:")#mass of projectile
y = #height of projectile when released
i = #moment of inertia
r = 0.12 #distance from COM of counterweight to COR in m

vLCW = w*r #linear velocity of counterweight

vPF = math.sqrt((2((mCW*g*hCWI)-((1/2)*mCW*vLCW*vLCW)-((1/2)*i*w*w)-(mCW*g*hCWF)-(mP*g*y)))/mP)]

print(vPF)


distance = input("Desired launch distance (in feet):")
deltaX = distance*.3048

theta = (math.asin((deltaX*g)/(vPF*vPF)))/2
