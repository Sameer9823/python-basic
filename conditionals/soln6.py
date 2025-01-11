distance = int(input("Enter the distance: "))

if distance < 10:
    print("walk")
elif distance < 20:
    print("bike")
else:
    print("car")