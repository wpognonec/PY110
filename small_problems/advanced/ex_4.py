def merge(lst1: list, lst2: list):
    sorted_list = []
    l1, l2 = lst1[:], lst2[:]

    while l1 and l2:
        if l1[0] < l2[0]:
            sorted_list.append(l1.pop(0))
        else:
            sorted_list.append(l2.pop(0))

    return sorted_list + l1 + l2

print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
print(merge([], [1, 4, 5]))             # [1, 4, 5]
print(merge([1, 4, 5], []))             # [1, 4, 5]