'''
input: string
output: boolean

rules:
    - return true if string is a palindrome
        - ignore non alpha-num characters
        - ignore case
'''

def is_real_palindrome(_str: str):
    new_str = ""
    for char in _str.casefold():
        if char.isalnum():
            new_str += char
    return is_palindrome(new_str)


def is_palindrome(_str):
    while _str:
        if _str[0] != _str[-1]:
            return False
        _str = _str[1:-1]
    return True

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True