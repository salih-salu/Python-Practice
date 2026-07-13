# 39. Python Program to Check if a Number is Positive, Negative or 0 

ls = [3, -5, 6, -10, 0, 4]

for i in ls:
    if i > 0:
        print(f'{i} : Positive')
    elif i < 0:
        print(f'{i} : Negative')
    else:
        print('Zero')