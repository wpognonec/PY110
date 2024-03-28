'''
input: list of numbers
output: new list of numbers with running totals

rules:
    - new list has same number of elements
    - each element is the running total from original list

algorithm:
    - set total to 0
    - set new empty list
    - for each num in original list
        - append num + total
        - set total = total + num
    - return new_list
'''

def running_total(_list: list):
    total = 0
    new_list = []
    for num in _list:
        new_list.append(num + total)
        total += num
    return new_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True