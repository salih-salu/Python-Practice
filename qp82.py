# 82. Enter a string with more than 3 characters. Then find reverse

string = input('Enter the string: ')


st = ''
for i in range(len(string)-1, -1, -1):
    st = st + string[i]
print(st)



# version 2......................................................................

print(string[::-1])