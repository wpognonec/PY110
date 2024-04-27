import string as s

def word_to_digit(string: str):
    new_string = []
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word in string.split():
        if word[-1] in s.punctuation:
            new_string.append(digit_map.get(word[:-1]) + word[-1])
        else:
            new_string.append(digit_map.get(word, word))
    print(" ".join(new_string))
    return " ".join(new_string)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True