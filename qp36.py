# 36. Print first n terms of Fibonacci series


n = int(input('Enter the number of terms: '))
n1 = 0
n2 = 1
p = 0
while p != n:
    print(n1)
    n1, n2 = n2, n1 + n2
    p += 1