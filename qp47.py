# 47. Convert a decimal number to binary 

num = int(input('Enter the number: '))

if num == 0:
    print('0')
else:
    res = ''
    while num > 0:
        rem = num%2
        res = str(rem)+res
        num = num // 2
    print(int(res))
    