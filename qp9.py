# Write a program to calculate the electricity bill. Accept the number of units consumed by the user 
# Unit               Price                    
# First 100 units    No charge 
# Next 100 units     Rs 5 per unit 
# After 200 units    Rs 10 per unit

# For example, if the input unit is 350 then the total bill amount is Rs 2000


units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

print("Electricity Bill = Rs", bill)