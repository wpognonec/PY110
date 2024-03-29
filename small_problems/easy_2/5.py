
def interleave(list1: list, list2: list):
    return [item for tup in zip(list1, list2) for item in tup]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True