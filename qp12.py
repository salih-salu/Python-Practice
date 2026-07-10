# Write a program to accept the cost price of a bike and display the road tax to be paid

price = int(input("Enter the bike price: "))

if price > 100000:
    tax = (price * 15) / 100
    print(f"Road tax amount is: {tax}")

elif price > 50000 and price <= 100000:
    tax = (price * 10) / 100
    print(f"Road tax amount is: {tax}")

else:
    tax = (price * 5) / 100
    print(f"Road tax amount is: {tax}")