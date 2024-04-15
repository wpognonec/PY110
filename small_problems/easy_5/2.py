def keep_keys(d: dict, l: list):
    return {k:v for k,v in d.items() if k in l}

print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}