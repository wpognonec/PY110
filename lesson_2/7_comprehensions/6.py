lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
lst2 = [{k: v+1 for k,v in _dict.items()} for _dict in lst]
print(lst2)