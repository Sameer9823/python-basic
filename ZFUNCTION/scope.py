username = "sameer"

def sam():
    username= 'fvdkjdfv'
    print(username)
    
print(username)
sam()


x = 99
def func2(y):
    z = x+ y
    return z

# result = func2(1)
# print(result)

# def funct3():
    # global x
    # x = 88
    
# funct3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
result =f1()
result()

def chaicode(num):
    def ac(d):
        return d ** num
    return ac

f = chaicode(2)
g = chaicode(3)

print(f(8))
print(g(3))


    