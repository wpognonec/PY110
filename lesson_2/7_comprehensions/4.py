lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dct = {
    sub[0]: sub[1] for sub in lst
}

print(dct)