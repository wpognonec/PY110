import random
import os

def b(text: str):
    """returns string in blue"""
    return f"\x1b[0;34;1m{text}\x1b[0m"

def r(text: str):
    """returns string in red"""
    return f"\x1b[0;31;1m{text}\x1b[0m"

def g(text: str):
    """returns string in green"""
    return f"\x1b[0;32;1m{text}\x1b[0m"

O, X, B = 1, -1, 0
ASCII = {
    1: [b(" █████ "),
        b("██   ██"),
        b("██   ██"),
        b("██   ██"),
        b(" █████ ")],

    -1: [r("██   ██"),
         r(" ██ ██ "),
         r("  ███  "),
         r(" ██ ██ "),
         r("██   ██")],

    0: [" " * 7 for _ in range(7)]
}
CLEAR = "cls" if os.name == "nt" else "clear"

def msg(message: str, user_input=False):
    if user_input:
        return input("==> " + message)
    return print("==> " + message)

def display_row(row: list, box_num: int):
    for i in range(5):
        if not i:
            print(
                f"{g(box_num)} {row[0][i]}  │"+
                f"{g(box_num+1)} {row[1][i]}  │"+
                f"{g(box_num+2)} {row[2][i]}")
        else:
            print(f"  {row[0][i]}  │  {row[1][i]}  │  {row[2][i]}")

def display_board(board: list):
    print('')
    display_row([ASCII[board[0]], ASCII[board[1]], ASCII[board[2]]], 1)
    print("───────────┼───────────┼───────────")
    display_row([ASCII[board[3]], ASCII[board[4]], ASCII[board[5]]], 4)
    print("───────────┼───────────┼───────────")
    display_row([ASCII[board[6]], ASCII[board[7]], ASCII[board[8]]], 7)
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
        if all(board[i] == X for i in combo):
            return X
        if all(board[i] == O for i in combo):
            return O
    return False

def get_valid_choices(board: list):
    return [idx for idx, val in enumerate(board) if val == B]

def minimax(board, depth, player):

    if player == O:
        best = [-1, +10]
    else:
        best = [-1, -10]

    if depth == 9:
        return best

    winner = get_winner(board)
    if depth == 0 or (is_board_full(board) or winner):
        if winner == X:
            score = 1
        elif winner == O:
            score = -1
        else:
            score = 0
        return [-1, score]

    for choice in get_valid_choices(board):
        board[choice] = player
        score = minimax(board, depth - 1, X if player == O else O)
        board[choice] = B
        score[0] = choice

        if player == O:
            if score[1] < best[1]:
                best = score
        else:
            if score[1] > best[1]:
                best = score

    return best

def find_easy_move(valid_choices: list):
    return random.choice(valid_choices)

def find_medium_move(board: list):
    valid_choices = get_valid_choices(board)

    for choice in valid_choices:
        board[choice] = O
        if get_winner(board) == O:
            return choice
        board[choice] = B

    for choice in valid_choices:
        board[choice] = X
        if get_winner(board) == X:
            return choice
        board[choice] = B

    if 4 in valid_choices:
        return 4

    choice = random.choice(valid_choices)
    return choice

def find_hard_move(board: list, depth):
    return minimax(board, depth, O)[0]

def play_round(state: dict):
    valid_choices = get_valid_choices(state["board"])
    if state["player"] == O:
        match state["difficulty"]:
            case "easy":
                choice = find_easy_move(valid_choices)
            case "medium":
                choice = find_medium_move(state["board"])
            case "hard":
                choice = find_hard_move(state["board"], len(valid_choices))

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
        sym = "X" if winner == X else "O"
        msg(f"{sym} has won the game!")
        state[f"{"x" if winner == X else "o"}_wins"] += 1
        return True

    if is_board_full(state["board"]):
        msg("The game is a tie!")
        return True

    return False

def play_again(game_number):
    while game_number > 0:
        msg("Play again?")
        msg(f"{g(1)}: Yes")
        msg(f"{g(2)}: No")
        answer = msg("", user_input=True)
        if answer == "2":
            msg("Thanks for playing!")
            return False
        if answer == "1":
            return True
        msg("Wrong input, please enter 1 or 2")
    return True

def get_difficulty():
    while True:
        msg(f"{g(1)}: Easy")
        msg(f"{g(2)}: Medium")
        msg(f"{g(3)}: Hard")
        choice = msg("Please choose the game difficulty: " ,
            user_input=True
            )
        match choice.lower():
            case "1" | "easy":
                return "easy"
            case "2" | "medium":
                return "medium"
            case "3" | "hard":
                return "hard"
        msg("That was not a valid choice.")

def display_stats(state: dict):
    os.system(CLEAR)
    msg(f"You played {state["game_number"]} games!")
    msg(f"You won {state["x_wins"]} games!")
    msg(f"Computer won {state["o_wins"]} games!")

def init_state():
    state = {
        "difficulty": "medium",
        "board": [],
        "player": X,
        "game_number": 0,
        "x_wins": 0,
        "o_wins": 0
    }
    state["difficulty"] = get_difficulty()
    return state

def play():
    os.system(CLEAR)
    state = init_state()

    while play_again(state["game_number"]):

        os.system(CLEAR)
        state["board"] = init_board()
        display_board(state["board"])

        while not is_game_done(state):

            play_round(state)
            os.system(CLEAR)
            display_board(state["board"])

        state["game_number"] += 1

    display_stats(state)

play()
