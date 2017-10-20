import turtle
import math
bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def arc(t, angle):
	radius = 100
	arc_length = 2*math.pi*radius*angle/360
	n = 50
	step_length = arc_length/n
	step_angle = angle/n
	outer_angle = 180-angle
	for i in range(5):
		polyline(t, n, step_length, step_angle)
		t.lt(outer_angle)
		polyline(t, n, step_length, step_angle)
		t.lt(angle)

arc(bob, 67.5)

turtle.mainloop()

