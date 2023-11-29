password = input("Enter a new password: ")

# Check the length of the password
if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")