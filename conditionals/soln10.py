animal = input()
age = 2

if animal == "cat":
    if (age <= 2):
        print("You are a kitten")
    else:
        print("You are a cat")
elif animal == "dog":
    if(age > 2):
        print("You are a dog")
    else:
        print("You are a puppy")
else:
    print("You are not a cat or a dog")