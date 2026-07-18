# 61. Python Program to Check Whether a String is Palindrome or Not 

def palindrome(s):
    return s == s[::-1]


st = input('Enter the string to find its a palindrome or not: ')
print('Yes' if palindrome(st) == True else 'No')