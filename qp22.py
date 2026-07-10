# 22. Accept three sides of a triangle and check whether it is an equilateral, isosceles, or 
# scalene triangle 
# An equilateral triangle is a triangle in which all three sides are equal 
# A scalene triangle is a triangle that has three unequal sides 
# An isosceles triangle is a triangle that has any two sides equal 


side1 = int(input('Enter the side 1: '))
side2 = int(input('Enter the side 2: '))
side3 = int(input('Enter the side 3: '))

if side1 == side2 == side3:
    print('Equilateral')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('isosceles')
elif (side1 != side2) and (side2 != side3):
    print('scalene')