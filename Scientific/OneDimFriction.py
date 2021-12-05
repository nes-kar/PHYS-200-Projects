import matplotlib.pyplot as plt
from math import sqrt
h = 40
v = 6

c = 0.3

g = -9.8
m = 1

dt = 0.01
t = 0

height = [h]
vel = [v]
time = [t]

while h >= 0:
	if v < 0: # If it's moving downwards, upward drag
		drag = (c*(v)**2) / (2*m)
	else:
		drag = -(c*(v)**2) / (2*m) # Downward drag
	h += v*dt
	v += (g + drag)*dt
	t += dt
	height.append(h)
	vel.append(v)
	time.append(t)
print(sqrt((2*m*abs(g) / c))) # Terminal velocity

plt.plot(time, height, time, vel)
plt.show()