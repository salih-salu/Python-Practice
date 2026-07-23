# 71. Maximum of two numbers in Python without using max 


num1 = int(input('Enter the number 1: '))
num2 = int(input('Enter the number 2: '))

if num1>num2:
    print('Largest: ', num1)
elif num2 > num1:
    print('Largest: ', num2)
else:
    print('Both numbers are same')