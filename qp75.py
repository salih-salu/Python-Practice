# 75. remove i’th character from string in Python 


st = "Hello World"
print("Original String:", st)

ch_no = int(input("Enter the character position: "))

new_st = st[:ch_no-1] + st[ch_no:]

print("New String:", new_st)