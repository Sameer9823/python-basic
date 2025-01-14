# def square(x):
#     return x ** 2

# result = square(5)
# # print(result)

# # //multiple parameters

# def add(x, y):
#     return x + y

# result = add(3, 7)
# # print(result)

# # polymorphism

# def add(x, y):
#     return x * y
# print(add(3, 4))
# print(add('d', 4))

# import math

# def circle(radius):
#     area = math.floor(math.pi * radius ** 2 * 100) / 100
#     circumference = math.floor(2 * math.pi * radius * 100) / 100
#     return area, circumference
    
# a, c = circle(2)
# print("area", a, "cicumference", c)


# def greet(name = "stranger"):
#     print("hello", name)

# greet()
# greet("sameer")

# # //lamda functions

# square = lambda x: x ** 3
# result = square(5)
# print(result)


# def sum_all(*args):
#     return sum(args)


# print(sum_all(1, 2,))
# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4))


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
  
# print_kwargs(name="shakitmaan", age=20)

# def even_generator(limit):
    
#     for i in range(2, limit + 1, 2):
#        yield i

# for num in even_generator(10):
#     print(num)


# recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

