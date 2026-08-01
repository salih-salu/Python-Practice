# 86. Print the largest word in a given string 


st = input('Enter the string: ')
ls = st.split()
print(max(ls, key=len))
