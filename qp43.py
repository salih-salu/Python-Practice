# 43. Find the sum of all the odd numbers below n 

n = int(input('Enter the nth number: '))

result = sum([i for i in range(1, n+1) if i%2 != 0])
print(result)