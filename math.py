import math

mCW = 1.74 #mass of cw, kg (3 washers weighing .58 each)
g = 9.81 #gravity, Newtons 
hCWI = 0.26 #initial height of cw, m
w = (7/18)*math.pi #rotational velocity (angular velocity?) in rad/sec
print(w)
hCWF = 0.03 #final height of cw, m
userMass = float(input("Mass of projectile (in grams):")) #mass of projectile that user inputs, g
mP = userMass/1000
y = 0.26 #height of projectile when released, m
i = .0223161663 #moment of inertia, kg*m^2
r = 0.12 #distance from COM of cw to COR, m

vLCW = w*r #linear velocity of cw

vPF = math.sqrt((2*((mCW*g*hCWI)-((1/2)*mCW*vLCW*vLCW)-((1/2)*i*w*w)-(mCW*g*hCWF)-(mP*g*y)))/mP)

print(vPF)


distance = float(input("Desired launch distance (in feet):"))
deltaX = distance*.3048

#theta = (math.asin((deltaX*g)/(vPF*vPF)))/2

theta1 = math.atan((deltaX+(math.sqrt((deltaX*deltaX)-(4*((g*deltaX*deltaX)/(2*vPF))*(((g*deltaX*deltaX)/(2*vPF))+y)))))/((g*deltaX*deltaX)/vPF))

theta2 = math.atan((deltaX-(math.sqrt((deltaX*deltaX)-(4*((g*deltaX*deltaX)/(2*vPF))*(((g*deltaX*deltaX)/(2*vPF))+y)))))/((g*deltaX*deltaX)/vPF))

print(theta1)
print(theta2)

degTheta1 = ((theta1*180)/math.pi) #converting the angles into degrees
degTheta2 = ((theta2*180)/math.pi)

print(degTheta1)
print(degTheta2)
