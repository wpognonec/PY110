def staggered_case(s: str):
    return "".join(c.lower() if i % 2 == 1 else c.upper() for i, c in enumerate(s))


print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"