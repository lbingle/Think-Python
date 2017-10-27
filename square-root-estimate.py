'''returns an approximation for the square root of a
given an estimate x'''
def sqr(a, x):
    while True:
        print(x)
        epsilon = .0000001
        y = (x + a/x) / 2
        if abs(x-y) < epsilon:
            break
        x = y

sqr(4, 3)

    
