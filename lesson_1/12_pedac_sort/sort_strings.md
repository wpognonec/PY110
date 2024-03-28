## Sort Strings by Most Adjacent Consonants

Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.
Tasks

## You are provided with the problem description above. Your tasks for this step are:

- Make notes of your mental model for the problem, including:
    - inputs and outputs.
    - explicit and implicit rules.
- Write a list of clarifying questions for anything that isn't clear.

# Step 1: Understand the Problem

Input: list of strings
Output: new list of strings sorted based on highest number of adjacent consonants

Explicit rules:
- If two strings contain same highest number of adjacent consonants, retain their original order
- Consonants are considered adjacent if next to each other or if there is a space between two consonants in adjacent words

Imlicit rules:
- Strings can contain one or more words
- Strings cannot be empty
- Strings may have no adjacent consonants
- Sort in decending order
- Case is not relevant
- Single consonants do not affect sort order

Questions:
- Do we take capitalization into account?
- What are valid characters?
- Direction of the sort order?
- Can strings be empty?
- Can strings contain a single word?
- No adjacent consonants possible?

# Step 2: Examples and test cases

```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```

- Strings can contain multiple words
- Words can have no consonants
- Decending order
- Empty strings or list?
- Capitalization?

# Step 3: Data Structures

Input and output will be a list. Possibly a dict for number of consonants?

# Step 4: Step 4: Algorithm

1. Find word(s) with the most consonants
2. Add all the words found in the order they appear in original list
3. Remove words from original list
4. Repeat steps 1 and 2 until all words have been added to sorted list
