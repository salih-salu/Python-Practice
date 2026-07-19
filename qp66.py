# 66. Create a program to enter two lists. Display True if the lists contains at least one common element.

def check(ls1, ls2):
    for i in ls1:
        if i in ls2:
            return True
    return False
            
ls1 = [4, 5, 8, 3]
ls2 = [2, 7, 5, 1]

print(check(ls1, ls2))