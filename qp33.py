# 33. Python Program to Check Armstrong Number 
num = int(input('Enter the number: '))

org = num
rem = 0
res = 0
power = len(str(num))

while num>0:
    rem = num%10
    res = res + rem**power
    num = num // 10
    
if res == org:
    print('Yes')
else:
    print('No')