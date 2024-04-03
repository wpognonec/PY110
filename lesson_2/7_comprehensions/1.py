munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_age = 0

for member in munsters.values():
    if member["gender"] == "male":
        total_age += member["age"]

print(total_age)

print(sum([item["age"] for item in munsters.values() if item["gender"] == "male"]))