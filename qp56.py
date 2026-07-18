# 56. Write a program to print the following pattern 
# A 
# B C 
# D E F 
# G H I J 


ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

inx = 0

for i in range(1, 5):
    for j in range(i):
        print(ls[inx], end=' ')
        inx += 1
    print()