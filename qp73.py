# 73. Python program to check whether the string is Symmetrical or Palindrome 

st = input('Enter the string: ')

rev = st[::-1]

if st == rev:
    print('Palindrome')
else:
    print('Not Palindrome')