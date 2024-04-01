def leading_substrings(s: str):
    return [s[:idx+1] for idx in range(len(s))]

def substrings(s: str):
    matrix = [leading_substrings(s[i:]) for i in range(len(s))]
    return [item for row in matrix for item in row]

print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]