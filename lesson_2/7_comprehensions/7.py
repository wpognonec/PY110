def get_mult_3(_list):
    return [num for num in _list if num % 3 == 0]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
lst2 = [get_mult_3(_list) for _list in lst]
print(lst2)