'''
input: string
output: boolean

rules:
    - return true if string is a palindrome (reads same backwards and forwards)
    - palindrome is case sensitive.
    - all characters matter

algorithm:
    - compare 1st character to last character
        - if equal, remove the characters
        - if not equal return false
    - repeat step 1 until 0 characters are left
    - return true
'''



def is_palindrome(_str):
    while _str:
        if _str[0] != _str[-1]:
            return False
        _str = _str[1:-1]
    return True


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)