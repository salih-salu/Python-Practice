# 77. Python program to print even length words in a string 

st = 'Python is good and simple programmimg language.'
ls = st.split()

for i in ls:
    if len(i)%2 == 0:
        print(i, len(i))