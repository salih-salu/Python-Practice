# 64. Create a new list the does not contain the duplicate elements in a list 

num = int(input('Enter the total number of elements: '))
ls = []
for i in range(1, num+1):
    n = int(input(f'Enter the number {i}: '))
    if n not in ls:
        ls.append(n)
        print('inserted')
    else:
        print('Entered number already exist!')
print(ls)