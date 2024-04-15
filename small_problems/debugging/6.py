def append_to_list(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1))        # Expected: [1]
print(append_to_list(2))        # Expected: [2]