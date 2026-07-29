# 81. Check two strings are anagram or not (eg: secure & rescue ,battle & tablet) 


string1 = input('Enter the string 1: ').lower()
string2 = input('Enter the string 2: ').lower()

lst1 = list(string1)
lst2 = list(string2)

lst1.sort()
lst2.sort()

if lst1 == lst2:
    print('Anagram')
else:
    print('Not Anagram')

