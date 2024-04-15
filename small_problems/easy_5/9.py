def staggered_case(s: str):
    b = True
    string = ""
    for char in s:
        if char.isalpha():
            string += char.upper() if b else char.lower()
            b = not b
        else:
            string += char
    return string


print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")