def recurse(n, s):
    """Prints value of s if n = 0. If n != 0 will take 1 from n and add n to s.
    Continues until n = 0. Infinite recursion if n is negative."""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(5, 2)
