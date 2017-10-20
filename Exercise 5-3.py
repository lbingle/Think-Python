def is_triangle():
    """Decides if you can form a triangle given two line lengths."""
    
    #User inputs
    a_in = input("Learn if you can form a triangle with three lines.\n Enter the length of the first line.\n")
    b_in = input("Enter the length of the second line.\n")
    c_in = input("Enter the length of the third line.\n")

    #Integers of user inputs
    a = int(a_in)
    b = int(b_in)
    c = int(c_in)

    #Responses
    y = "You can form a triangle with these three lines."
    n = "You cannot form a triangle with these three lines."

    #Calculated values
    bc = (b + c)
    ac = (a + c)
    ab = (a + b)

    if a > bc or b > ac or c > ab:
        print(n)
    elif a <= bc or b <= ac or c <= ab:
        print(y)

is_triangle()

    
