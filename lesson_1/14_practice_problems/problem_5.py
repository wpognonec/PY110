ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total = 0

for age in ages.values():
    total += age

print(total)
print(sum(ages.values()))