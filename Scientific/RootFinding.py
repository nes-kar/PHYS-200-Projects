""" Round complex?
round(x.real, 3) + round(x.imag, 3)
"""

def find_root(a, b, c):
	d = abs(b**2) - (4*a*c)
	if d > 0:
		x11 = (-b + d**(1/2)) / (2*a)
		x12 = (-b - d**(1/2)) / (2*a)
		print("The roots are real: {}, {}".format(x11,x12))
	elif d == 0:
		x = (-b + d**(1/2)) / (2*a)
		print("There is a single root: {}".format(x))
	else:
		x21 = (-b + d**(1/2)) / (2*a)
		x22 = (-b - d**(1/2)) / (2*a)
		print("The roots are imaginary: {}, {}".format(x21,x22))
		
while True:
	i = input("Enter coefficients: ")
	if i == "q":
		break
	if len(i.rsplit(",")) != 3:
		print("You must enter three coefficients.")
		continue
	a, b, c = [int(x) for x in i.rsplit(",")]
	if a == 0:
		print("Not a quadratic polynomial.")
		continue
	find_root(a,b,c)