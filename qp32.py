# 32. Python Program to Find Armstrong Number in an Interval

st = int(input('Enter the starting number: '))
ed = int(input('Enter the Ending number: '))

for num in range(st, ed+1):
    org = num
    rem = 0
    res = 0
    power = len(str(num))

    while num>0:
        rem = num%10
        res = res + rem**power
        num = num // 10
        
    if res == org:
        print(org)