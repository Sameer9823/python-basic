age = 25

if age < 13:
    print("you are child")
elif age < 20:
    print("you are teenager")
elif age < 60:
    print("you are adult")
else:
    print("you are old")

marks = input("Enter your marks: ")
marks = int(marks)

if marks <= 100 and marks >= 80:
    print("A")
elif marks < 80 and marks >= 60:
    print("B")
elif marks < 60 and marks >= 40:
    print("C")
else:
    print("D")