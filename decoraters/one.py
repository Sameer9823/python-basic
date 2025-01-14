import time

# # def timer(func):
# #     def wrapper(*args, **kwargs):
# #         start_time = time.time()
# #         result =func(*args, **kwargs)
# #         end_time = time.time()
# #         print(f"Function {func.__name__} took {end_time - start_time} seconds")
# #         return result
# #     return wrapper


# # @timer
# # def example(n):
# #     time.sleep(n)

# # example(2)
# # #

# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{key}={value}" for key, value in kwargs.items())
#         print(f"Calling {func.__name__} with args: {args_value} kwargs: {kwargs_value}")
#         return func(*args, **kwargs)
    
#     return wrapper
    

# @debug
# def hello():
#     print("Hello, world!")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{name}, {greeting}!")

# hello()
# greet("Sameer", greeting= "Hi")


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    
    return wrapper
    

@cache
def long_running_function(a, b):
    time.sleep(3)
    return a + b


print(long_running_function(1, 2))
print(long_running_function(4, 2))
