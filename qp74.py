# 74. Reverse each words in a given String in Python 

st = input('Enter the string: ')

words = st.split()
new_words = [word[::-1] for word in words]

result = ' '.join(new_words)
print(result)