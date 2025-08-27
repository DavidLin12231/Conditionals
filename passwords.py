# Step 1: Get password from user
password = input("Enter your password: ")

# Step 2: Check Conditions (DON'T EDIT THIS!!!)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_length = len(password) >= 8

#Step 3: (YOU DO THIS PART)
