# 44. Find the sum of all even numbers and odd numbers separately up to a given number  

n = int(input('Enter the nth number: '))

result = ['Even number: ',sum([x for x in range(1, n+1) if x%2 == 0]), 'Odd number: ',sum([x for x in range(1, n+1) if x%2 != 0])]
print(result)