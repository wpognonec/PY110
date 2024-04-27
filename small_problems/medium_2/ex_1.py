def letter_percentages(string: str):
    lower = 0
    upper = 0
    length = len(string)
    for char in string:
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
    lower = lower / length * 100
    upper = upper / length * 100
    stats = {
        "lowercase": lower,
        "uppercase": upper,
        "neither": 100 - (lower + upper)
    }
    return stats

print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }