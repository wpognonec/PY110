def sequence(count: int, start: int):
    return [i * start for i in range(1, count + 1)]


print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []