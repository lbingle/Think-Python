import turtle
import math
bob = turtle.Turtle()
print(bob)

def pie(length):
    half = (length/2)
    length_b = ((half)*math.sin(math.radians(54)))/math.sin(math.radians(36))
    length_in = math.sqrt((half**2)+(length_b**2))
    for i in range(5):
        bob.rt(36)
        bob.fd(length_in)
        bob.rt(126)
        bob.fd(length)
        bob.rt(126)
        bob.fd(length_in)

pie(200)














