fruit = "banana"
color = "yellow"

if fruit == "banana":
    if color == "green":
        print("The banana is not ripe yet.")
    elif color == "yellow":
        print("The banana is ripe.")
    elif color == "brown":
        print("The banana is overripe.")
    else:
        print("The banana is not a banana.")
else:
    print("The fruit is not a banana.")