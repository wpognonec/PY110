def unique_from_first(list1: list, list2: list):
    # return set(list1) - set(list2)
    return set([i for i in list1 if i not in list2])

print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}