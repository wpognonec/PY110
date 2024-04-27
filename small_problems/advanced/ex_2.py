def transpose(matrix: list):
    return [list(row) for row in zip(*matrix)]

print(transpose([[1, 2, 3, 4]]))            # [[1], [2], [3], [4]]
print(transpose([[1], [2], [3], [4]]))      # [[1, 2, 3, 4]]
print(transpose([[1]]))                     # [[1]]

print(transpose([[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [3, 7, 8, 6, 2]]))
# [[1, 4, 3], [2, 3, 7], [3, 2, 8], [4, 1, 6], [5, 0, 2]]