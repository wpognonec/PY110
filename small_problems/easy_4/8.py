def leading_substrings(s: str):
    return [s[:idx+1] for idx in range(len(s))]

def substrings(s: str):
    matrix = [leading_substrings(s[i:]) for i in range(len(s))]
    return [item for row in matrix for item in row]

def palindromes(string: str):
    return [s for s in substrings(string) if s == s[::-1] and len(s) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True