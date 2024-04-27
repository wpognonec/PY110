def max_rotation(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        str_n = str_n[:i] + str_n[i+1:] + str_n[i]
    return int(str_n)

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845
