def unique_sequence(nums):
    return list(dict.fromkeys(nums))

print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
print(unique_sequence([]))
# [1, 2, 3, 4, 5, 6]