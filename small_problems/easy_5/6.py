def sum_of_sums(lst: list):
    return sum([sum(lst[:i]) for i in range(1, len(lst) + 1)])

print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35