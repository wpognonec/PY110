def bubble_sort(lst: list):
    length = len(lst)
    while length > 1:
        last_swap = 0
        for i in range(1,length):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                last_swap = i
        length = last_swap

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)    # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)    # [1, 2, 4, 6, 7]

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)    # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]