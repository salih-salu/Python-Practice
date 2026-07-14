# 41. Python Program to Print all Prime Numbers in an Interval 

st = int(input('Enter the starting number: '))
ed = int(input('Enter the ending number: '))

for i in range(st, ed+1):
    prime = 0
    if i <2:
        continue
    for j in range(2, i):
        if i%j == 0:
            prime = 1
            break
    if prime == 0:
        print(i)