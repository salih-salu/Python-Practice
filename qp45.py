# 45. Python Program to Find the Factors of a Number 

n = int(input('Enter the number: '))
print([x for x in range(1, n+1) if n%x == 0])