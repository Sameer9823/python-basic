# from hello import chai

# chai(9)


a = 29
for i in range(9):
    print(i)
    
# use recursion example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    
print(factorial(5))

