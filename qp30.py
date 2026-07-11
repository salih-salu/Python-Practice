# 30. Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3 

st = int(input('Enter the starting number: '))
ed = int(input('Enter the ending number: '))

result = [i for i in range(st, ed+1) if i%2 != 0 and i %3 != 0]
print(result)