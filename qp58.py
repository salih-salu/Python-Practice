# 58. Python Program to Display Fibonacci Sequence Using Recursion 


def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
num = int(input('Enter the number of elements to print the fibonacci sequence: '))
for i in range(0, num+1):
    print(fib(i), end=' ')