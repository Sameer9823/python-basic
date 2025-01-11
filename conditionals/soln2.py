age = 22
day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2

print(price)


marks = int(input("Enter your marks: "))

if marks >= 101:
    print("plz verify your marks")
    exit()

if marks >= 80 :
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("D")