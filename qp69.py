# 69. Python program to swap two elements in a list 

ls = [10, 20, 30, 50, 100]

pos1 = int(input('Enter the position1: '))
pos2 = int(input('Enter the position2: '))
if 1 <= pos1 <= len(ls) and 1 <= pos2 <= len(ls):
    ls[pos1-1], ls[pos2-1] = ls[pos2-1], ls[pos1-1]
    print(ls)
else:
    print('Invalid Position!')

