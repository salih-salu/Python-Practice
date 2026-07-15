# 49. Print all the prime numbers within a range 


st = int(input("Enter the starting number: "))
ed = int(input("Enter the ending number: "))

for num in range(max(st, 2), ed + 1):
    flag = 1

    for j in range(2, num):
        if num % j == 0:
            flag = 0
            break

    if flag == 1:
        print(num)
