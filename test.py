'''returns an approximation for the square root of a
given an estimate x'''
import math

def sqr(a, x):
    while True:
        epsilon = .0000001
        y = (x + a/x) / 2
        if abs(x-y) < epsilon:
            return x
            break
        x = y

def mysqrt(a):
    x = a/2
    return sqr(a, x)

def math(a):
    import math
    return math.sqrt(a)

def table():
    print('a  ','mysqrt(a)     ','math.sqrt(a)  ','diff')
    print('-  ','---------     ','------------  ','----')
    print('1  ',mysqrt(1),'    ',math(1),'      ','llll')
    print('2  ',mysqrt(2),'    ',math(2),'      ','llll')

table()












