# 34. Python Program to Find the Factorial of a Number 

num = int(input('Enter the number: '))
fac = 1

for i in range(1, num+1):
    fac = fac*i
print(fac)