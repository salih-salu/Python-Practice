# 67. Sort the elements in a list without using built in functions 

ls = [44, 32, 84, 12, 25, 60]

for i in range(len(ls) - 1):
    for j in range(len(ls) - 1 - i):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
        
print(ls)