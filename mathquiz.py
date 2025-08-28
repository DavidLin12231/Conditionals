import random

#picks 2 random numbers
a = random.randint(0, 12)
b = random.randint(0, 12)

c = input("Press A for addition and M for multiplication")
if c == 'M':
    x = input(f"What is {a} * {b}? ")
    if int(x) == a*b:
        print("You are correct!")
    else:
        print("Study your times tables")
if c == 'A':
    x = input(f"What is {a} + {b}? ")
    if int(x) == a+b:
        print("You are correct!")
    else:
        print("Study your addition")
