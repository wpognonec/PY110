def multiply_elements(l1: list, l2: list):
    return [a * b for a, b in zip(l1, l2)]

print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]