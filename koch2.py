import turtle
import math
bob = turtle.Turtle()
print(bob)

def koch(t, n):
    if n < 10:
        bob.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

koch(bob, 100)
