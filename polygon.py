import turtle
import math
bob = turtle.Turtle()
print(bob)

def polygon(t, l, n):
	angle = 360/n
	for i in range(n):
		bob.fd(l)
		bob.lt(angle)

polygon(bob, 100, 5)
turtle.mainloop()
