# 53. Program to print the diamond shape 
rows = 5

for i in range(1, rows+1):
    print(' '*(rows-i), '*'*((2*i)-1))
    
for j in range(rows-1, 0, -1):
    print(' '*(rows-j), '*'*((2*j)-1))