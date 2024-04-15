def invert_dict(dict: dict):
    return {val: key for key, val in dict.items()}


print(invert_dict({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}))
# {'fruit': 'apple', 'vegetable': 'broccoli', 'fish': 'salmon'}