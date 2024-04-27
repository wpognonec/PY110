# def binary_search(lst, search_item):
#     high = len(lst) - 1
#     low = 0

#     while low <= high:
#         mid = low + (high - low) // 2
#         if lst[mid] == search_item:
#             return mid
#         elif lst[mid] < search_item:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

def binary_search(lst: list, string: str):
    l = lst[:]
    while True:
        center = l[len(l)//2]
        if string == center:
            return lst.index(center)
        if string < center:
            l = l[:len(l)//2]
        if string > center:
            l = l[len(l)//2:]
        if len(l) == 1 and string != l[0]:
            return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)