def sum_all(*args):
    print(args)
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(1, 2, 3, 4, 5, 6))  # 21
