def order_by_value(d):
    return sorted(d, key=lambda x: d[x])

print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']