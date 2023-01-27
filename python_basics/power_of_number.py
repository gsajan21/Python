num = (input("Enter a number: "))

for i, c in enumerate(reversed(num)):
    print(c, 10**i, 10**i * int(c))
