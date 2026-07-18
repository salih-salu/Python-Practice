# 59. Python Program to Find Sum of Natural Numbers Using Recursion 

def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n-1)

num = int(input('Enter the number of elements: '))
n_sum = 0
print(sum_num(num))