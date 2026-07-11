# 29. Program to print all the numbers that are divisible by both 11 and 2 within range of 100 - 500

start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))

result = [i for i in range(start, end+1) if i%11==0 and i%2 == 0]

for i in result:
    print(i)



