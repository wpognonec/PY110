# 1. Find word(s) with the most consonants
# 2. Add all the words found in the order they appear in original list
# 3. Remove words from original list
# 4. Repeat steps 1 and 2 until all words have been added to sorted list

def sort_by_consonant_count(_list: list):
    sorted_list = []
    while _list:
        new_word = get_highest(_list)
        sorted_list.append(new_word)
        _list.remove(new_word)
    return sorted_list

def get_highest(_list: list):
    new_str = _list[0]
    for string in _list:
        if get_consonants(string) > get_consonants(new_str):
            new_str = string
    return new_str

def get_consonants(string: str):
    max_cons = 0
    current_cons = 0
    for char in string.replace(" ", ""):
        if char in 'aeiou':
            current_cons = 0
        else:
            current_cons += 1
            if (current_cons > max_cons) and (current_cons > 1):
                max_cons = current_cons

    return max_cons


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']