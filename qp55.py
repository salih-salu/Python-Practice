# 55. Create following six patterns 

# 12345
# 1234
# 123
# 12
# 1

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()
    
# ....................................................................

# 12345
# 2345
# 345
# 45
# 5

rows = 5
for i in range(1, rows+1):
    for j in range(i, rows+1):
        print(j, end='')
    print()

# ....................................................................

# 54321
# 4321
# 321
# 21
# 1

rows = 5
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# ....................................................................

# 5
# 54
# 543
# 5432
# 54321

rows = 5
for i in range(1, rows+1):
    for j in range(rows, rows-i, -1):
        print(j, end='')
    print()


# ....................................................................

# 1
# 21
# 321
# 4321
# 54321

row = 5
for i in range(1, row+1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('')


# ....................................................................

# 5
# 54
# 543
# 5432
# 54321

rows = 5
for i in range(rows, 0, -1):
    for j in range(rows, i-1, -1):
        print(j, end='')
    print()

# ....................................................................