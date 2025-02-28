species = input("Enter the name of a species: ")
age = int(input("Enter the age of the species: "))

if species == "cat" and age <= 2:
    print("You are a kitten")
elif species == "cat":
    print("You are a cat")
elif species == "dog" and age > 2:
    print("You are an old dog")
elif species == "dog":  
    print("You are a dog")      
else:
    print("You are not a cat or a dog")