def string_to_signed_integer(string: str):
    digit_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    number = 0
    for i,v in enumerate(string[::-1]):
        if v == "-":
            number *= -1
        elif v != '+':
            number += digit_map[v] * 10 ** i
    return number

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True