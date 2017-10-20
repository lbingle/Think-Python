import turtle
import math
bob = turtle.Turtle()
print(bob)

def koch(t, n):
    m = n/3
    bob.fd(m)
    bob.lt(60)
    bob.fd(m)
    bob.rt(120)
    bob.fd(m)
    bob.lt(60)
    bob.fd(m)

koch(bob, 100)




