
def signed_integer_to_string(num: int):
    digits = "0123456789"
    num_str = ""
    while num:
        num_str += digits[num%10]
        num = num // 10
    return num_str[::-1] or '0'


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True