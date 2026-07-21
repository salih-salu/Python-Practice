# 68. Python program to interchange first and last elements in a list 

ls = [22, 34, 12, 50]

print('Before: ', ls)

ls[0], ls[-1] = ls[-1], ls[0]

print('After: ', ls)