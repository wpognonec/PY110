import math

def dms(angle: float):
    degs = math.floor(angle)
    mins = math.floor((angle % 1) * 60)
    secs = math.floor((((angle % 1) * 60) % 1) * 60)

    while degs < 0:
        degs += 360
    while degs > 360:
        degs -= 360
    return f"{degs}°{mins:02d}'{secs:02d}\""

# All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"