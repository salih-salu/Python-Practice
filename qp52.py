# 52. Programs for printing pyramid patterns in Python 

rows = 5

for i in range(1, rows * 2, 2):
    print(" " * ((rows * 2 - 1 - i) // 2), end="")
    print("*" * i)