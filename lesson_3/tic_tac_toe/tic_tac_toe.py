import random
import os

O = [" █████ ", "██   ██", "██   ██", "██   ██", " █████ "]
X = ["██   ██", " ██ ██ ", "  ███  ", " ██ ██ ", "██   ██"]
B = ["       ", "       ", "       ", "       ", "       "]
CLEAR = "cls" if os.name == "nt" else "clear"

def print_row(_l: list):
    for i in range(5):
        print(_l[0][i], " | ", _l[1][i], " | ", _l[2][i])

def print_divider():
    print("---------+-----------+---------")

def display_board(board: list):
    print('')
    print_row([board[0], board[1], board[2]])
    print_divider()
    print_row([board[3], board[4], board[5]])
    print_divider()
    print_row([board[6], board[7], board[8]])
    print('')

def init_board():
    return [B for _ in range(9)]

def is_board_full(board: list):
    return board.count(B) == 0

def is_winner(board: list):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [6,4,2]
    ]
    for combo in win_combos:
        id1, id2, id3 = combo
        if board[id1] == X and board[id2] == X and board[id3] == X:
            print("X WON")
            return True
        elif board[id1] == O and board[id2] == O and board[id3] == O:
            print("O WON")
            return True
    return False

def play_round(_board: list, _player: str):
    valid_choices = [idx for idx, val in enumerate(_board) if val == B]
    if _player[0] == O:
        choice = random.choice(valid_choices)
        _board[choice] = _player[0]
        _player[0] = X
    else:
        while True:
            print("valid choices: ", ", ".join(str(num) for num in valid_choices))
            choice = int(input("Choose an empty square: "))
            if choice in valid_choices:
                _board[choice] = _player[0]
                _player[0] = O
                break
            print("That is not a valid choice, please try again")
    
def play():
    while True:
        os.system(CLEAR)
        state = {
            "board": init_board(),
            "player": [X]
        }
        display_board(state["board"])

        while not is_board_full(state["board"]) and not is_winner(state["board"]):
            play_round(state["board"], state["player"])
            os.system(CLEAR)
            display_board(state["board"])

        answer = input("Play again? y/n: ")
        if answer != "y":
            print("Thanks for playing!")
            break


play()