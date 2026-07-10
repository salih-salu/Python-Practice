# 24. Accept three different numbers then display the second largest number.

ls = []
for i in range(1, 4):
    n = int(input(f'Enter the number {i}: '))
    ls.append(n)

res = sorted(ls)
print(res[1])

