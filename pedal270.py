import turtle
import math
bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def arc(t, radius, angle):
	arc_length = 2*math.pi*radius*angle/360
	n = 50
	step_length = arc_length/n
	step_angle = angle/n
	for i in range(2):
		polyline(t, n, step_length, step_angle)
		t.lt(270)
	t.lt(180)
	for i in range(2):
		polyline(t, n, step_length, step_angle)
		t.lt(270)

arc(bob, 100, 90)

turtle.mainloop()

