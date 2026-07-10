# 16. Perform temperature conversion based on our requirement 
# Fahrenheit to Celsius: C=(F-32) (5/9) 
# Celsius to Fahrenheit:  F=C*(9/5) +32 

f = int(input('enter the Fahrenheit: '))
c = (f - 32) * (5/9)
print(c)