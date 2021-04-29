import math

mCW = 1.74 #mass of cw, kg
g = 9.81 #gravity, Newtons
hCWI = #initial height of cw
w = #rotational velocity (angular velocity?) in rad/sec
hCWF = #final height of cw
mP = input("Mass of projectile:")#mass of projectile
y = #height of projectile when released
i = #moment of inertial
r = #distance from COM of cw to COR

vLCW = w*r #linear velocity of cw

vPF = math.sqrt((2((mCW*g*hCWI)-((1/2)*mCW*vLCW*vLCW)-((1/2)*i*w*w)-(mCW*g*hCWF)-(mP*g*y)))/mP)
