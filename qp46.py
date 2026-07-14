# 46. Python Program to Find LCM 

n1 = int(input('Enter the number 1: '))
n2 = int(input('Enter the number 2: '))

maxm = max(n1, n2)

while True:
    if maxm%n1 == 0 and maxm%n2 == 0:
        print(maxm)
        break
    maxm += 1


