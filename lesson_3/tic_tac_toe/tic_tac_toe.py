import random
import os
from copy import deepcopy

def b(text: str):
    """returns string in blue"""
    return f"\x1b[0;34;1m{text}\x1b[0m"

def r(text: str):
    """returns string in red"""
    return f"\x1b[0;31;1m{text}\x1b[0m"

def g(text: str):
    """returns string in green"""
    return f"\x1b[0;32;1m{text}\x1b[0m"

O = [b(" █████ "), b("██   ██"), b("██   ██"), b("██   ██"), b(" █████ ")]
X = [r("██   ██"), r(" ██ ██ "), r("  ███  "), r(" ██ ██ "), r("██   ██")]
B = ["       ", "       ", "       ", "       ", "       "]
CLEAR = "cls" if os.name == "nt" else "clear"

def msg(message: str, user_input=False):
    if user_input:
        return input("==> " + message)
    return print("==> " + message)


def display_row(row: list, box_num: int):
    for i in range(5):
        if not i:
            print(
                f"{g(box_num)} {row[0][i]}  |"+
                f"{g(box_num+1)} {row[1][i]}  |"+
                f"{g(box_num+2)} {row[2][i]}")
        else:
            print(f"  {row[0][i]}  |  {row[1][i]}  |  {row[2][i]}")

def display_board(board: list):
    print('')
    display_row([board[0], board[1], board[2]], 1)
    print("-----------+-----------+-----------")
    display_row([board[3], board[4], board[5]], 4)
    print("-----------+-----------+-----------")
    display_row([board[6], board[7], board[8]], 7)
    print('')

def join_or(choices: list, sep: str = ", ", end="or"):
    match len(choices):
        case 0:
            return ""
        case 1:
            return f"Valid choice: {g(choices[0]+1)}"
        case _:
            joined = sep.join(g(str(num+1)) for num in choices[:-1])
            return f"Valid choices: {joined}{sep}{end} {g(choices[-1]+1)}"

def init_board():
    return [B for _ in range(9)]

def is_board_full(board: list):
    return not board.count(B)

def get_winner(board: list):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [6,4,2]
    ]
    for combo in win_combos:
        if all(board[i] == X for i in combo if board[i]):
            return "X"
        if all(board[i] == O for i in combo if board[i]):
            return "O"
    return False

def get_valid_choices(board: list):
    return [idx for idx, val in enumerate(board) if val == B]

def find_best_move(board: list):
    valid_choices = get_valid_choices(board)

    for choice in valid_choices:
        test_board = deepcopy(board)
        test_board[choice] = O
        if get_winner(test_board) == "O":
            return choice

    for choice in valid_choices:
        test_board = deepcopy(board)
        test_board[choice] = X
        if get_winner(test_board) == "X":
            return choice

    if 4 in valid_choices:
        return 4

    choice = random.choice(valid_choices)
    return choice

def play_round(state: dict):
    valid_choices = get_valid_choices(state["board"])
    if state["player"] == O:
        if state["difficulty"] == "easy":
            choice = random.choice(valid_choices)
        elif state["difficulty"] == "medium":
            choice = find_best_move(state["board"])
        state["board"][choice] = state["player"]
        state["player"] = X
    else:
        while True:
            msg(join_or(valid_choices))
            choice = int(msg("Choose an empty square: ", user_input=True))-1
            if choice in valid_choices:
                state["board"][choice] = state["player"]
                state["player"] = O
                break
            msg("That is not a valid choice, please try again")

def is_game_done(state: dict):
    winner = get_winner(state["board"])
    if winner:
        msg(f"{winner} has won the game!")
        state[f"{"x" if winner == "X" else "o"}_wins"] += 1
        return True

    if is_board_full(state["board"]):
        msg("The game is a tie!")
        return True

    return False

def play_again(game_number):
    if game_number > 0:
        answer = msg("Play again? y/n: ", user_input=True)
        if answer != "y":
            msg("Thanks for playing!")
            return False
    return True

def get_difficulty():
    while True:
        choice = msg(
            "What difficulty would you like? (E)asy / (M)edium: " ,
            user_input=True
            )
        match choice.lower():
            case "e" | "easy":
                return "easy"
            case "m" | "medium":
                return "medium"
        msg("That was not a valid choice.")


def play():
    state = {
        "difficulty": "medium",
        "board": [],
        "player": X,
        "game_number": 0,
        "x_wins": 0,
        "o_wins": 0
    }

    state["difficulty"] = get_difficulty()

    while play_again(state["game_number"]):

        os.system(CLEAR)
        state["board"] = init_board()
        display_board(state["board"])

        while not is_game_done(state):

            play_round(state)
            os.system(CLEAR)
            display_board(state["board"])

        state["game_number"] += 1

    msg(f"You played {state["game_number"]} games!")
    msg(f"You won {state["x_wins"]} games!")
    msg(f"Computer won {state["o_wins"]} games!")


play()
