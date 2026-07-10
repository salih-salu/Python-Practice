# 13. Write a program to check whether given year is leap year or not 

y = int(input('enter the year: '))
if (y %4 == 0 and y %100 != 0) or y %400 == 0:
    print(f'{y} is a leap year')
else:
    print(f'{y} is not a leap year')