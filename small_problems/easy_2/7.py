
def multiply_list(l1: list, l2: list):
    for i in range(len(l1)):
        l1[i] *= l2[i]
    return l1

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True