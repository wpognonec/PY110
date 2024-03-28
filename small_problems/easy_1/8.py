
def string_to_integer(string: str):
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
        number += digit_map[v] * 10 ** i
    return number

def hexadecimal_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }

    value = 0
    for char in s:
        value = (16 * value) + DIGITS[char.lower()]

    return value

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True


print(hexadecimal_to_integer('4D9f') == 19871)  # True