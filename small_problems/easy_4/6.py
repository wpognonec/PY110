def leading_substrings(string: str):
    # return [s[:idx+1] for idx in range(len(s))]
    sub_list = []
    for i in range(1,len(string)+1):
        sub_list.append(string[:i])
    return sub_list

print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']