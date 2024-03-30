def reverse_number(number: int):
    return int(str(number)[::-1])

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1