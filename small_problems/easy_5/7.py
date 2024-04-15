def sum_digits(num: int):
    return sum([int(digit) for digit in str(num)])

print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45