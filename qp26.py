# 26. Python Program to Find the Largest Among Three Numbers

largest = 0

largest = sorted([int(input(f"Enter number {i}: ")) for i in range(1, 4)])
print(largest[-1])