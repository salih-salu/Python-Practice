# 50. Print all the perfect numbers within a range 


st = int(input('Enter the starting number: '))
ed = int(input('Enter the eding number: '))


for num in range(st, ed+1):
    total = 0
    for i in range(1, num//2 + 1):
        if  num%i == 0:
            total += i
    if total == num:
        print(num)
            
    
    