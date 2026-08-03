# 87. Print largest words in a given string (needs to print if more than one word with same length) 

st = input('Enter the string: ')

ls = st.split()
large = len(max(ls, key=len))
for i in ls:
    if len(i) == large:
        print(i)