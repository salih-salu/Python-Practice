# 11. Write a program to accept the total mark (out of 500) of a student. Then calculate the 
# percentage of marks. Calculate the grade based on the following criteria 

# Marks           Grade
# >=80            A 
# >=70 and <80    B
# >=60 and <70    C 
# >=50 and <60    D 
# Below 50        Failed 


mark = int(input('Enter the mark: '))
percent = (mark * 100)//500

if percent >= 80:
    print(f'Grade A with {percent}%')
elif 80 > percent >= 70:
    print(f'Grade B with {percent}%')
elif 70 > percent >= 60:
    print(f'Grade C with {percent}%')
elif 60 > percent >= 50:
    print(f'Grade D with {percent}%')
else:
    print('Failed')