def calculate_leftover_blocks(leftover_blocks: int):
    layer = 0
    layer_blocks = 0
    while layer_blocks <= leftover_blocks:
        leftover_blocks -= layer_blocks
        layer += 1
        layer_blocks = layer ** 2
    return leftover_blocks



print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True