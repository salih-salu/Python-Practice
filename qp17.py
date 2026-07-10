# 17. Write a program to check whether the last digit of a given number is divisible by three or not 

digit = int(input('Enter the digit: '))
dt = str(digit)

if int(dt[-1])%3 == 0:
    print('Yes')
else:
    print('No')