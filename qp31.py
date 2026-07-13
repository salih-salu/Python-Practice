# 31. Check a given number is a perfect number or not( perfect number means the sum of factors equal to the same number 6=1+2+3) 

num = int(input('Enter the number: '))

result = 0
for i in range(1, num):
    if num%i == 0:
        result += i
if num == result:
    print(f'Yes, {num} is a perfect number')
else:
    print(f'No, {num} is not a perfect number')
