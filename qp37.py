# 37. Python Program to Display the multiplication Table 

num = int(input('Enter the number to display the multiplication table: '))

for i in range(1, 11):
    print(f'{i}X{num}: {i*num}')

# print([i*num for i in range(1, 11)])