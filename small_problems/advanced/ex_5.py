def merge(lst1: list, lst2: list):
    sorted_list = []
    l1, l2 = lst1[:], lst2[:]

    while l1 and l2:
        if l1[0] < l2[0]:
            sorted_list.append(l1.pop(0))
        else:
            sorted_list.append(l2.pop(0))

    return sorted_list + l1 + l2

def merge_sort(lst: list):

    if len(lst) == 1:
        return lst
    
    l1 = merge_sort(lst[:len(lst)//2])
    l2 = merge_sort(lst[len(lst)//2:])

    return merge(l1,l2)


print(merge_sort([9, 5, 7, 1]))           # [1, 5, 7, 9]
print(merge_sort([5, 3]))                 # [3, 5]
print(merge_sort([6, 2, 7, 1, 4]))        # [1, 2, 4, 6, 7]

print(merge_sort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']))
# ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

print(merge_sort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]))
# [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]