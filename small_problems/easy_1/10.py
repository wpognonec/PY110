
def integer_to_string(num: int):
    digits = "0123456789"
    num_str = ""
    while num:
        num_str += digits[num%10]
        num = num // 10
    return num_str[::-1] or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True