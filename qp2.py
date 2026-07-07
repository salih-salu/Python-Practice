# 2. Python Program to Make a Simple Calculator 

option = 0
while option != 5:
    print('...Simple Calculator...')
    print('1: Addition')
    print('2: Substraction')
    print('3: multiplication')
    print('4: division')
    print('5: Exit')
    
    option = int(input('enter the option you want to calculate: '))
    if option !=5:
        a = int(input('enter the number a: '))
        b = int(input('enter the number b: '))
    if option == 1:
        print(a+b)
    elif option == 2:
        print(a-b)
    elif option == 3:
        print(a*b)
    elif option == 4:
        print(a//b)
    elif option == 5:
        print('exiting...')
        break
    print('*'*100)
