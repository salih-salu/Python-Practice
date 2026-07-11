# 27. Check a given number is a perfect square.(16,25, 36… are perfect squares 4*4=16,5*5=25,6*6=36) 

num = int(input('Enter the number: '))

if num == int(num**0.5)**2:
    print(f'Yes, The number {num} is a Perfect squares')
else:
    print(f'No, The number {num} is not a Perfect squares')
