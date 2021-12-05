import numpy as np
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = plt.axes(projection='3d')

def cross(v1, v2):
	x1, y1, z1 = v1
	x2, y2, z2 = v2
	return np.array([y1*z2-z1*y2, -(x1*z2-z1*x2), x1*y2-y1*x2])

E = np.array([1, 4, 7])
B = np.array([10, 20, 0])

m = 5
q = -3

def acc(q, E, v, B, m):
	return np.array((E + cross(v, B)))*q/m

x, y, z = 100, 50, 100
v = np.array([0, 0, 0])
dt = 0.01
t = 0

coords = []
while t < 15:
	x += v[0]*dt
	y += v[1]*dt
	z += v[2]*dt
	a  = acc(q, E, v, B, m)
	v = v + a*dt
	t += dt
	coords.append([x, y, z])

coords = np.array(coords)
ax.plot3D(coords[:, 0], coords[:, 1], coords[:, 2], 'gray')
plt.show()




