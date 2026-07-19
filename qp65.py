# 65. Create a program to split a list into two list. Here one list contains all the elements 
#     greater than 5 and other list contains all the elements less than 5

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lss_ls, grt_ls = [i for i in ls if i<5], [j for j in ls if j>5]
print(f'Less than 5: {lss_ls}')
print(f'Greater than 5: {grt_ls}')