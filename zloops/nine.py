items = ["banana", "cherry", "apple", "strawberry", "kiwi", "apple", "cherry",  "kiwi", "apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print(item, "is a duplicate item.")
        break
    unique_item.add(item)