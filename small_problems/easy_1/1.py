numbers = []

for _ in range(6):
    numbers.append(input("Provide a number: "))

b = "is in" if numbers[-1] in numbers[0:-1] else "is not in"
print(f"{numbers[-1]} {b} {", ".join(numbers[0:-1])}")