def kwarg(**kwargs):
    return kwargs

print(kwarg(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
print(kwarg(name='John', age=25))  # {'name': 'John', 'age': 25}
print(kwarg(name='John', age=25, city='New York'))  # {'name': 'John', 'age': 25, 'city': 'New York'}