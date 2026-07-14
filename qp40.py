# 40. Python Program to Check Prime Number 

num = int(input('Enter the number: '))
prime = 0
for i in range(2, num):
    if num%i == 0:
        prime = 1
        break

if prime == 0:
    print('prime')
else:
    print('Not prime')