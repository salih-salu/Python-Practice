# 60. Python Program To Display Powers of 2 Using Anonymous Function 

num = int(input('Enter the number: '))

power = lambda x: 2 ** x

for i in range(num+1):
    print(power(i))


