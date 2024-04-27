def triangle(s1, s2, s3):
    sides = [s1, s2, s3]
    if 0 in sides or sum(sides) != 180:
        return "invalid"
    if 90 in sides:
        return  "right"
    if all(side < 90 for side in sides):
        return "acute"
    return "obtuse"


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
