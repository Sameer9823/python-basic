# username = "sameer"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()


# x = 88

# # def func1(y):
# #     z = x + y
# #     return z

# # print(func1(9))


# # def func2():
# #     global x
# #     x = 99
    
# # func2()
# # print(x)

# def f1():
#     x = 77
#     def f2():
#         print(x)
#     return f2
# myresukt = f1()
# myresukt()


def chai(n):
    def sameer(x):
        return x ** n
    return sameer

res = chai(2)
res1 = chai(3)
print(res1(5))
print(res(3))