numbers = [1,2,3,4,-5,-7,-8,10]
positiv_number = 0

for num in numbers:
    if num > 0:
        positiv_number += 1
# print("number of positive numbers",positiv_number)


n = int(input("Enter the number: "))
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += 1
# print(sum)

table = int(input("Enter the number: "))

for i in range(1, 11):
    if (i == 5):
        continue
    # print(table, "*", i, "=", table * i)


name = "sameer"
reversed_str = ""

for char in name:
    reversed_str = char + reversed_str
# print(reversed_str)


string = "teetere"

for char in string:
    if string.count(char) == 1:
    #  print(char)
     break


# //factorial of a number

num = int(input("Enter the number: "))  
factorial = 1

while num > 0:
    factorial *= num
    num -= 1
    print(factorial)
   
# print(factorial)




while True:
    number = int(input("Enter the number: "))
    if 1 <= number <= 10:
        print("thanks")
        break
    else:
        print("try again")


nume = 28
prime = True

if number > 1:
    for i in range(2, nume):
        if (nume % i) == 0:
            prime = False
            break

print(prime)


items = ["apple", "banana", "cherry", "date", "elderberry", "apple", "banana", "cherry", "date", "elderberry"]

unique = set()

for item in items:
    if item in unique:
        print("duplicate")
        break
    else:
        unique.add(item)
        print("unique")


