# 14. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday 2 for Monday and so on. 


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thersday', 'Friday', 'Saturday']
d = int(input('Enter the number to select a day: '))

print(days[d-1])

