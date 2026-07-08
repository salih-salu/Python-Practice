# Write a program to display “Hello” if the number entered is divisible by 9 else print “Bye” 

num = int(input('Enter the number: '))
if num%9 == 0:
    print('Hello')
else:
    print('Bye')