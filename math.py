import math

mCW = 1.16 #mass of cw, kg
g = 9.81 #gravity, Newtons
hCWI = 21 #initial height of cw, cm
w = #rotational velocity (angular velocity?) in rad/sec
hCWF = 7 #final height of cw, cm
mP = input("Mass of projectile:")#mass of projectile
y = #height of projectile when released
i = #moment of inertial
r = 7 #distance from COM of cw to COR, cm

vLCW = w*r #linear velocity of cw

vPF = math.sqrt((2((mCW*g*hCWI)-((1/2)*mCW*vLCW*vLCW)-((1/2)*i*w*w)-(mCW*g*hCWF)-(mP*g*y)))/mP)
