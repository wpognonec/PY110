def is_even(l):
    for lst in l.values():
        if [val for val in lst if val % 2 == 1]:
            return False
    return True

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
lst2 = [l for l in lst if is_even(l)]
print(lst2)
