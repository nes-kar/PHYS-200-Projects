import matplotlib.pyplot as plt 
from math import *

vel = 30
angle = 45

vx = vel*cos(radians(angle))
vy = vel*sin(radians(angle))

x, y = 0,0

c = 0.1

g = 9.8
m = 2

dt = 0.001

velx = [vx]
vely = [vy]
xs, ys = [x], [y]

ax = -c*vx**2/m
ay = -g - c*vy**2/m

while y >= 0:
	x += vx*dt
	y += vy*dt
	vx += (-c*vx**2/m)*dt
	vy += (-g - c*vy**2/m)*dt
	xs.append(x)
	ys.append(y)
print(xs)
plt.plot(xs, ys)
plt.show()