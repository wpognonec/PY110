lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
lst2 = [sorted(sub, key=str) for sub in lst]
print(lst2)