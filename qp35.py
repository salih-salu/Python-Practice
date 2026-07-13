# 35. Python Program to Print the Fibonacci sequence less than a given number 

ending = int(input('Enter the ending number: '))
n1 = 0
n2 = 1
while n1 < ending:
    print(n1)
    n1, n2 = n2, n1 + n2
    