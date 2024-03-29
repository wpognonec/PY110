
def digit_list(number: int):
    num_list = []
    while number:
        num_list.insert(0, number % 10)
        number //= 10
    return num_list


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True