order_size = "large"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)


password = input("Enter your password: ")

if len(password) < 8:
 print("Password is week")
elif len(password) < 12:
 print("Password is medium")
else:
 print("Password is strong")

year = 2023

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")



