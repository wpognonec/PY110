def sum_square_difference(n: int):
    x = sum(range(n + 1)) ** 2
    y = sum(num ** 2 for num in range(n + 1))
    return x - y

print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150