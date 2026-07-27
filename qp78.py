# 78. Check a given string is pangram or not(contains all the alphabets at least one time) 

alp = 'abcdefghijklmnopqrstuvwxyz'
st = 'The quick brown fox jumps over the lazy dog'
flag = False
for ch in alp:
    if ch not in st.lower():
        flag = True
        break

if flag == False:
    print('Yes')
else:
    print('No')
        
