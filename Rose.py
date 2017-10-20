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
	polyline(t, n, step_length, step_angle)

def rose(t, pedal, angle):
	radius = 100
	arc_length = 2*math.pi*radius*angle/360
	pedal = 50
	for i in range(pedal):
		arc(t, radius, angle)
		for i in range(pedal):
			angel_x = (360-angle)/2
			angle_y = (360-angle)/2
			step_length = arc_length/n
			step_angle = angle/n
			polyline(t, pedal, step_length, step_angle)
			t.lt(angle_x)
			polyline(t, pedal, step_length, step_angle)
			t.lt(angle_y)

rose(bob, 4, 90)

turtle.mainloop()
