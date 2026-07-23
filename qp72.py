# 72. Minimum of two numbers in Python without using min 

n1 = int(input('Enter the number 1: '))
n2 = int(input('Enter the number 2: '))

if n1 > n2:
    print('minimum number: ', n2)
elif n1 < n2:
    print('minimum number: ', n1)
else:
    print('Numbers are equal.')