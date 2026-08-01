# 85. Write a function to get a new string from a given string where “Is” has been added to 
# the front.If the given string already begins with “Is” then return the string unchanged. 
# Eg: good morning 
# o/p : Is good morning 


def is_string(st):
    if st[0:2].lower() == 'is':
        return st
    else:
        return 'Is ' + st

st = input('Enter the string: ')
print(is_string(st))




# version2 ............................................................................

def is_string(st):
    if st.lower().startswith('is'):
        return st
    else:
        return 'Is ' + st

st = input('Enter the string: ')
print(is_string(st))