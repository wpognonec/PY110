data = [1, 2, 3, 2, 4, 3]
unique_data = list(dict.fromkeys(data))
print(unique_data)  # The order is not guaranteed to be [1, 2, 3, 4]