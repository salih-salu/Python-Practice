# 54. Print an Inverted pyramid Star Pattern 

rows = 5

for i in range(1, rows+1):
    print(' '*(i-1),'*'*(2*(rows-i)-1))