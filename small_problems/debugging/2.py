def reverse_string(s):
    new_s = ""
    for char in s:
        new_s = char + new_s
    return new_s

print(reverse_string("hello"))