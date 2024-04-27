def rotate_rightmost_digits(n: int, c: int):
    str_n = str(n)
    l = len(str_n)
    new_num = str_n[:l-c] + str_n[l-c+1:] + str_n[l-c]
    return int(new_num)

print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917
