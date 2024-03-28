def swap(_str: str):
    word_list = _str.split()
    for idx, word in enumerate(word_list):
        if len(word) == 1:
            word_list[idx] = word
        else:
            new_word = word[-1] + word[1:-1] + word[0]
            word_list[idx] = new_word
    return " ".join(word_list)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True