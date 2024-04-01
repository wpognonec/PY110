def transactions_for(_id: int, _list: list):
    return [item for item in _list if item["id"] == _id]

def is_item_available(_id: int, _list: list):
    items = transactions_for(_id, _list)
    ins = sum(item["quantity"] for item in items if item["movement"] == "in")
    outs = sum(item["quantity"] for item in items if item["movement"] == "out")
    return (ins - outs) > 0

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True