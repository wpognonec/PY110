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

X, O, B = 1, -1, 0
ASCII = {
    -1: [b(" █████ "),
         b("██   ██"),
         b("██   ██"),
         b("██   ██"),
         b(" █████ ")],

    1: [r("██   ██"),
        r(" ██ ██ "),
        r("  ███  "),
        r(" ██ ██ "),
        r("██   ██")],

    0: [" " * 7 for _ in range(7)]
}
CLEAR = "cls" if os.name == "nt" else "clear"

def msg(message: str):
    """formats print messages"""
    return print("==> " + message)

def display_row(row: list, box_num: int):
    """prints a single row of the board"""
    for i in range(5):
        if not i:
            print(
                f"{g(box_num)} {row[0][i]}  │"+
                f"{g(box_num+1)} {row[1][i]}  │"+
                f"{g(box_num+2)} {row[2][i]}")
        else:
            print(f"  {row[0][i]}  │  {row[1][i]}  │  {row[2][i]}")

def display_board(board: list):
    """prints the whole board"""
    print('')
    display_row([ASCII[board[i]] for i in range (0,3)], 1)
    print("───────────┼───────────┼───────────")
    display_row([ASCII[board[i]] for i in range (3,6)], 4)
    print("───────────┼───────────┼───────────")
    display_row([ASCII[board[i]] for i in range (6,9)], 7)
    print('')

def init_board():
    """returns an empty board"""
    return [B for _ in range(9)]

def is_board_full(board: list):
    """returns True if board is full, False otherwise"""
    return not board.count(B)

def join_or(choices: list, sep: str = ", ", end="or"):
    """returns a formated string with the valid choices"""
    match len(choices):
        case 0:
            return ""
        case 1:
            return f"Valid choice: {g(choices[0]+1)}"
        case _:
            joined = sep.join(g(str(num+1)) for num in choices[:-1])
            return f"Valid choices: {joined}{sep}{end} {g(choices[-1]+1)}"

def get_winner(board: list):
    """returns the winner or 0 if there is no winner"""
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
    return 0

def get_valid_choices(board: list):
    """returns a list of valid moves to make on the board"""
    return [idx for idx, val in enumerate(board) if val == B]

def minimax(board, depth, player):
    """returns the best possible move using minimax algorithm"""
    best = [-1, -10 * player]

    if depth == 9:
        return best

    winner = get_winner(board)
    if depth == 0 or (is_board_full(board) or winner):
        return [-1, winner]

    for choice in get_valid_choices(board):
        board[choice] = player
        score = minimax(board, depth - 1, -player)
        board[choice] = B
        score[0] = choice

        if player == O:
            if score[1] < best[1]:
                best = score
        else:
            if score[1] > best[1]:
                best = score

    return best

def get_easy_move(valid_choices: list):
    """returns an easy difficulty move"""
    return random.choice(valid_choices)

def get_medium_move(board: list):
    """returns a medium difficulty move"""
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

def get_hard_move(board: list, depth):
    """returns a hard difficulty move"""
    return minimax(board, depth, O)[0]

def play_round(state: dict):
    """plays a round of tic tac toe"""
    valid_choices = get_valid_choices(state["board"])
    if state["player"] == O:
        match state["difficulty"]:
            case "easy":
                choice = get_easy_move(valid_choices)
            case "medium":
                choice = get_medium_move(state["board"])
            case "hard":
                choice = get_hard_move(state["board"], len(valid_choices))

        state["board"][choice] = state["player"]
        state["player"] = X
    else:
        while True:
            msg(join_or(valid_choices))
            choice = int(input("==> Choose an empty square: "))-1
            if choice in valid_choices:
                state["board"][choice] = state["player"]
                state["player"] = O
                break
            os.system(CLEAR)
            display_board(state["board"])
            msg("That is not a valid choice, please try again")

def is_game_done(state: dict):
    """returns True if the game is done, False otherwise"""
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

def play_again(state):
    """returns True is user wants to play again, False otherwise"""
    while state["game_number"] > 0:
        msg("Play again?")
        msg(f"{g(1)}: Yes")
        msg(f"{g(2)}: No")
        answer = input("==> ")
        if answer == "2":
            msg("Thanks for playing!")
            return False
        if answer == "1":
            return True
        os.system(CLEAR)
        display_board(state["board"])
        msg("That was not a valid choice.")
    return True

def get_difficulty():
    """asks user for game difficulty"""
    while True:
        diff = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }
        msg("Please choose the game difficulty:")
        msg(f"{g(1)}: Easy")
        msg(f"{g(2)}: Medium")
        msg(f"{g(3)}: Hard")
        choice = input("==> ")
        if choice in diff:
            return diff[choice]
        os.system(CLEAR)
        msg("That was not a valid choice.")

def display_stats(state: dict):
    """displays the wins and losses at the end of the match"""
    os.system(CLEAR)
    msg(f"You played {state["game_number"]} games!")
    msg(f"You won {state["x_wins"]} games!")
    msg(f"Computer won {state["o_wins"]} games!")

def init_state():
    """initializes and returns the starting state of the game"""
    state = {
        "difficulty": get_difficulty(),
        "board": [],
        "player": X,
        "game_number": 0,
        "x_wins": 0,
        "o_wins": 0
    }
    return state

def play():
    """main game loop"""
    os.system(CLEAR)
    msg("Welcome to Tic Tac Toe")
    state = init_state()

    while play_again(state):
        os.system(CLEAR)
        state["board"] = init_board()
        state["player"] = X
        display_board(state["board"])

        while not is_game_done(state):
            play_round(state)
            os.system(CLEAR)
            display_board(state["board"])

        state["game_number"] += 1

    display_stats(state)

play()
