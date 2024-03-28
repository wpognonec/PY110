def double_numbers(numbers):
    doubled_nums = []

    for current_num in numbers:
        doubled_nums.append(current_num * 2)

    return doubled_nums

def double_numbers_mutate(numbers):

    for i,_ in enumerate(numbers):
        numbers[i] *= 2

    return numbers

def double_odd_numbers(numbers):
    doubled = []
    for i,v in enumerate(numbers):
        if i % 2 == 0:
            doubled.append(v * 2)
        else:
            doubled.append(v)
    return doubled

def multiply(numbers, multiplier):
    multiplied = []
    for num in numbers:
        multiplied.append(num * multiplier)
    return multiplied

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers_mutate(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [2, 8, 6, 14, 4, 12]

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_numbers(my_numbers))  # [2, 4, 6, 14, 2, 6]
print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]