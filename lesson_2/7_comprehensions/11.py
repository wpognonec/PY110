dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

vowels = "aeiou"

# list_of_vowels = []
# for item in dict1.values():
#     for word in item:
#         for char in word:
#             if char in vowels:
#                 list_of_vowels.append(char)

list_of_vowels = [char for item in dict1.values() 
                       for word in item
                       for char in word
                       if char in vowels]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']