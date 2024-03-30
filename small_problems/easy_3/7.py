# def swap_name(name: str):
#     return ", ".join(name.split()[::-1])

def swap_name(name: str):
    name_split = name.split()
    return f"{name_split[-1]}, {" ".join(name_split[:-1])}"

print(swap_name('Joe Roberts'))    # "Roberts, Joe"
print(swap_name('Karl Oskar Henriksson Ragvals'))    # "Ragvals, Karl Oskar Henriksson"