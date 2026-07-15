# 48. Convert a binary number to decimal 
binary = input("Enter a binary number: ")

if all(bit in "01" for bit in binary):
    print(int(binary, 2))
else:
    print("Invalid binary number")

# .........................................................................


# binary = int(input('Enter the number: '))
# res = 0
# power = 0
# flag = 0

# while binary>0:
#     rem = binary%10
#     if rem == 0 or rem == 1:
#         res = res + rem * (2**power)
#     else:
#         print('The given number is not actual binary number')
#         flag = 1
#         break
#     binary = binary//10
#     power += 1

# if flag == 0:
#     print(res)


