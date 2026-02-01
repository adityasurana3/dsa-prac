a = int(input("Enter 1st number"))
b = int(input("Enter 2st number"))

# Let's say a is 10 and b is 5
a = a ^ b  # a = 10 ^ 5 = 15
b = a ^ b  # b = 15 ^ 5 = 10
a = a ^ b  # a = 15 ^ 10 = 5

print(a, b)
