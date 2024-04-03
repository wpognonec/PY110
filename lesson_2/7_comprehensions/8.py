dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
def extract(v):
    if v["type"] == "fruit":
        return [color.title() for color in v["colors"]]
    if v["type"] == "vegetable":
        return v["size"].upper()
    return v["colors"], v["size"]
lst = [extract(v) for v in dict1.values()]
print(lst)