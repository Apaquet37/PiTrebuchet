import math

mCW = 1.74 #mass of cw, kg (3 washers weighing .58 each)
g = 9.81 #gravity, Newtons 
hCWI = 0.26 #initial height of cw, m
w = (7/18)*math.pi #rotational velocity (angular velocity?) in rad/sec
print(w) #printing w just to test that math.pi works
hCWF = 0.03 #final height of cw, m
userMass = float(input("Mass of projectile (in grams):")) #mass of projectile that user inputs, g
mP = userMass/1000 #converting the user inputted mass from grams to kilograms
y = 0.26 #height of projectile when released, m
i = .0223161663 #moment of inertia, kg*m^2
r = 0.12 #distance from COM of cw to COR, m

vLCW = w*r #linear velocity of cw

vPF = math.sqrt((2*((mCW*g*hCWI)-((1/2)*mCW*vLCW*vLCW)-((1/2)*i*w*w)-(mCW*g*hCWF)-(mP*g*y)))/mP) #This equation take into account all
#the energy (potential and kinetic) of all the components of the trebuchet, and is then manipulated to discover the velocity of the projectile

print(vPF) #printing the velocity


distance = float(input("Desired launch distance (in feet):")) #Getting a user input for how far they want their projectile to go
deltaX = distance*.3048 #Converting the user inputted distance from feet to meters

#theta = (math.asin((deltaX*g)/(vPF*vPF)))/2 #Range equation, simple way to find theta, but wasn't givin us good values

theta1 = math.atan((deltaX+(math.sqrt((deltaX*deltaX)-(4*((g*deltaX*deltaX)/(2*vPF))*(((g*deltaX*deltaX)/(2*vPF))+y)))))/((g*deltaX*deltaX)/vPF))

theta2 = math.atan((deltaX-(math.sqrt((deltaX*deltaX)-(4*((g*deltaX*deltaX)/(2*vPF))*(((g*deltaX*deltaX)/(2*vPF))+y)))))/((g*deltaX*deltaX)/vPF))

#Those two long equations both yield a theta, one larger and one smaller. This is because it is derived from a quadratic in terms of tan(theta)

print(theta1) #Printing the thetas (in radians)
print(theta2)

degTheta1 = ((theta1*180)/math.pi) #converting the angles into degrees
degTheta2 = ((theta2*180)/math.pi)

print(degTheta1) #Printing the thetas in degrees (easier to check)
print(degTheta2)
