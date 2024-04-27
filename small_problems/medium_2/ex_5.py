def featured(n: int):
    if n >= 9876543201:
        return "There is no possible number that fulfills those requirements."

    n += 1
    while not n % 2 or n % 7:
        n += 1

    while len(set(list(str(n)))) != len(str(n)):
        n += 14

    return n

print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."
