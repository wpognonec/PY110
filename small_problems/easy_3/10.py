def is_balanced(string: str):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '"': '"', '\'': '\''}

    for char in string:
        if char in pairs.keys() | pairs.values():
            stack.append(char)
        if len(stack) > 1 and (stack[-1] == pairs.get(stack[-2])):
            stack = stack[:-2]
    return not stack


print(is_balanced("{}") == True)
print(is_balanced("[]") == True)
print(is_balanced("()") == True)
print(is_balanced("{[({})]}") == True)
print(is_balanced("\"{[('')]}\"") == True) 
print(is_balanced("Hello [Python] (asdf).") == True)
print(is_balanced("{[()stacks]} are {kool[()]}") == True)
print(is_balanced("{[}]") == False)
print(is_balanced("({[})") == False)
print(is_balanced("][") == False)
print(is_balanced("'''") == False)
print(is_balanced("'\"'\"'") == False)

