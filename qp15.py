# 15. Create a simple calculator. Perform the calculations by entering the operands and operator 

print('Simple calculator')
op = 0
while op != 5:
    print('.................................')
    print('1: Addition')
    print('2: Subtraction')
    print('3: Multiplication')
    print('4: Division')
    print('5: Exit')
    op = int(input('enter the oprator: '))
    if op == 5:
        print('Exiting!!!')
        break
    a = int(input('enter the a: '))
    b = int(input('enter the b: '))
    if op == 1:
        print(f'sum: {a+b}')
    elif op == 2:
        print(f'sub: {a-b}')
    elif op == 3:
        print(f'mull: {a*b}')
    elif op == 4:
        print(f'div: {a//b}')
