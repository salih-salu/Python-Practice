# 28. Python Program to Solve Quadratic Equation.

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation.")
else:
    dd = b**2 - 4*a*c

    if dd > 0:
        root1 = (-b + math.sqrt(dd)) / (2*a)
        root2 = (-b - math.sqrt(dd)) / (2*a)
        print("Two real roots:", root1, root2)

    elif dd == 0:
        root = -b / (2*a)
        print("One real root:", root)

    else:
        print("No real roots")