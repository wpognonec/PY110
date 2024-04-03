lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
lst2 = sorted(lst, key=lambda x: sum([num for num in x if num % 2 == 1]))
print(lst2)