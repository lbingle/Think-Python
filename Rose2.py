import turtle
import math
bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def arc(t, angle, pedal):
	radius = 200
	arc_length = 2*math.pi*radius*angle/360
	n = 50
	step_length = arc_length/n
	step_angle = angle/n
	outer_angle = 180-angle
	for i in range(10):
		polyline(t, n, step_length, step_angle)
		t.lt(outer_angle)
		polyline(t, n, step_length, step_angle)
		t.lt(angle)

def rose(t, pedal):
    angel = 180/pedal
    arc(t, angel, pedal)

rose(bob, 5)

turtle.mainloop()
