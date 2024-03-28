statement = "The Flintstones Rock"

freq = {}

for char in statement.replace(" ", ""):
    freq[char] = freq.get(char, 0) + 1

print(freq)


# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }