# 10. Write a program to check the last digit of a given number is divisible by 3 

num = int(input('Enter the number: '))
last_dt = num%10

if last_dt%3 == 0:
    print(f'Yes, The Last digit {last_dt} from then number {num} is divisible by 3')
else:
    print(f'No, The Last digit {last_dt} from then number {num} is not divisible by 3')
    



