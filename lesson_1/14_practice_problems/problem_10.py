dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
print(dictionary)

# ('b', 'bear')
# popitem() returns a tuple with the key/value of the last item entered in the dictionary.
# the original dictionary is mutated