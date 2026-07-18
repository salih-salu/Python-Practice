# 57. Python Program to Find Factorial of Number Using Recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
    
    
num = int(input('Enter the number: '))
print(fact(num))