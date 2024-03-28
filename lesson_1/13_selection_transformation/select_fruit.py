produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(lst: list):
    selected_fruit = {}
    for k,v in lst.items():
        if v == "Fruit":
            selected_fruit[k] = v
    return selected_fruit


print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }