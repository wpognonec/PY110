def triangle(s1, s2, s3):
    sides = sorted([s1, s2, s3])
    if 0 in sides or sum(sides[:2]) < sides[2]:
        return "invalid"
    match len(set(sides)):
        case 1:
            return "equilateral"
        case 2:
            return "isosceles"
        case 3:
            return "scalene"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True