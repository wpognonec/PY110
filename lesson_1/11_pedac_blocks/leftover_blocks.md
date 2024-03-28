
Leftover Blocks

You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

    The building blocks are cubes.
    The structure is built in layers.
    The top layer is a single block.
    A block in an upper layer must be supported by four blocks in a lower layer.
    A block in a lower layer can support more than one block in an upper layer.
    You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.
Tasks

You are provided with the problem description above. Your tasks for this step are:

    Make notes of your mental model for the problem, including:
        inputs and outputs.
        explicit and implicit rules.
    Write a list of clarifying questions for anything that isn't clear.

## Step 1: Understand the Problem

Input: integer representing a number of blocks
Output: integer respresending a leftover blocks

### Rules:
#### Explicit:
- Structure built in layers
- Top layer is a single block
- A block in an upper layer must be supported by four blocks in a lower layer
- A block in a lower layer can support more than one block in an upper layer
- No gaps between blocks

#### Implicit:
- Layer number correlates with blocks in a layer
- Number of blocks in a layer is layer number ** 2

### Questions:
- Is a lower layer valid if it has more blocks than it needs?
- Will there always be left over blocks?

## Step 2: Examples and test cases

```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

- Left over blocks can be zero
- Lower layer cannot have more blocks than it needs

### Step 3: Data Structures

- The structure is a list of layers
- layers are integers representing the number of cubes in the layer


### Step 4: Algorithm

1. create empty list
2. add layer to list
3. reduce number of blocks
4. repeat steps 2 and 3 until a new layer cannot be created
5. return left over blocks