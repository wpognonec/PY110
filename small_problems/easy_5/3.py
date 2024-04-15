def remove_vowels(lst: list):
    new_list = [devowel(string) for string in lst]
    return new_list

def devowel(string: str):
    return "".join([c for c in string if c.lower() not in "aeiou"])

print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']