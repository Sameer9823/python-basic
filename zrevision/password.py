password = "Secure@1234"

password_length = len(password)

if password_length < 8:
    print("Password must be at least 8 characters long.")
elif password_length > 16:
    print("Password must be at most 16 characters long.")
else:
    print("Password is valid.")