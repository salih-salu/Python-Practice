# 51. Print all the Armstrong numbers within a range 

st = int(input('Enter the starting number: '))
ed = int(input('Enter the ending number: '))

for num in range(st, ed+1):
    rem = 0
    res = 0
    temp = num
    power = len(str(num))
    
    while temp > 0:
        rem = temp % 10
        res = res + rem**power
        temp = temp // 10
    if res == num:
        print(num)