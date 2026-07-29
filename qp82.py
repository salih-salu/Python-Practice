# 82. Enter a string with more than 3 characters. Then find reverse without changing first and last character 
# eg:python--->pohtyn 

st = input('Enter the string: ')
result = st[0]+st[1:-1][::-1]+st[-1]

print(result)