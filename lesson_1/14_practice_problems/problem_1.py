fruits = ("apple", "banana", "cherry", "date", "banana")

def count_fruit(tup, fruit):
    count = 0
    for item in tup:
        if item == fruit:
            count += 1
    return count

print(count_fruit(fruits, "banana"))
print(fruits.count('banana'))