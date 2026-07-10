# 19. Write a program to check whether a character is a vowel or not. 

v = 'aeiou'
st = input('Enter the charecter: ')
if st.lower() in v:
    print(f'{st} is a vowel charecter')
else:
    print(f'{st} is not a vowel charecter')