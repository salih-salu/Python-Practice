# 42. Python Program to Find the Sum of Natural Numbers 

n = int(input('Enter the positive ending number: '))
count = 0
result = [i for i in range(1, n+1)]
print(sum(result))