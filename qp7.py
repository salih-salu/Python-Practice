# Perform swapping of two numbers 
# A=3, B=4     
# After swapping A=4 and B=3 

n1 = int(input('enter the number1: '))
n2 = int(input('enter the number2: '))

print(f'Before swapping: {n1, n2}')
temp = n1
n1 = n2
n2 = temp
print(f'after swapping: {n1, n2}')