# 80. Reverse of a number 

num = int(input('Enter the number: '))
num_copy = num
result = 0
rem = 0

while num > 0:
    rem = num%10 
    result = (result * 10 )+ rem
    num = num//10
    
print(f'The reverse of the number {num_copy} is {result}')