# 23. Accept the age, sex(M/F), number of days and display the wages accordingly 

# Age              Sex          Wage/Day 
# >=18 and <30     M            700 
#                  F            750 
# >=30 and <=40    M            800 
#                  F            850 
# If age does not fall in any range then display the following message: “Enter appropriate age” 


age = int(input('enter the age: '))
gender = input('enter the Gender(male or female): ')
sex = 'M' if gender == 'male' else 'F'
days = int(input('enter the number of days: '))

if age >= 18 and age < 30:
    if sex == 'M':
        print(700*days)
    else:
        print(750*days)
elif age >= 30 and age <= 40:
    if sex == 'M':
        print(800*days)
    else:
        print(850*days)
else:
    print('Enter the appropriate age!!!')