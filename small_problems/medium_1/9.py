import math

def find_fibonacci_index_by_length(i: int):
    fibs = [1,1]
    idx = 2
    while True:
        if int(math.log10(fibs[-1]))+1 == i:
            return idx
        fibs.append(fibs[-1] + fibs[-2])
        idx += 1

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
print(find_fibonacci_index_by_length(10000) == 47847)