def transactions_for(_id: int, _list: list):
    return [item for item in _list if item["id"] == _id]


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

print(transactions_for(101, transactions))
# prints
# [ {"id": 101, "movement": "in",  "quantity":  5},
#   {"id": 101, "movement": "in",  "quantity": 12},
#   {"id": 101, "movement": "out", "quantity": 18} ]