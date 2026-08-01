# 84. Write a python function that takes two lists and returns True if they have at least one common number 

def input_list(st, ls1, ls2):
    print('Elements in List 1: ')
    for i in range(st):
        n = int(input())
        ls1.append(n)
    print('Elements in List 2: ')
    for i in range(st):
        n = int(input())
        ls2.append(n)
    
def fun(ls1, ls2):
    for i in ls1:
        if i in ls2:
            return True
    return False

st = int(input('enter the number of elements both list: '))

ls1 = []
ls2 = []
input_list(st, ls1, ls2)
print(fun(ls1, ls2)) 