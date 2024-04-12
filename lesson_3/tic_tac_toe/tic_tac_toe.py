import random
import os

def blue(text: str):
    """returns string in blue"""
    return f"\x1b[0;34;1m{text}\x1b[0m"

def red(text: str):
    """returns string in red"""
    return f"\x1b[0;31;1m{text}\x1b[0m"

def green(text: str):
    """returns string in green"""
    return f"\x1b[0;32;1m{text}\x1b[0m"

X, O, EMPTY = 1, -1, 0
ASCII = {
    -1: [blue(" █████ "),
         blue("██   ██"),
         blue("██   ██"),
         blue("██   ██"),
         blue(" █████ ")],

    1: [red("██   ██"),
        red(" ██ ██ "),
        red("  ███  "),
        red(" ██ ██ "),
        red("██   ██")],

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
                f"{green(box_num)} {row[0][i]}  │"+
                f"{green(box_num+1)} {row[1][i]}  │"+
                f"{green(box_num+2)} {row[2][i]}")
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

def display_winner(state: dict):
    """display the winner of the game and update score"""
    winner = get_winner(state["board"])
    if winner:
        sym = "X" if winner == X else "O"
        state[f"{"x" if winner == X else "o"}_wins"] += 1
        if state[f"{"x" if winner == X else "o"}_wins"] == 5:
            msg(green(f"{sym} has won the match!"))
        else:
            msg(f"{sym} has won the game!")
    else:
        msg("The game is a tie!")
    display_stats(state)

def display_stats(state: dict):
    """displays the wins and losses at the end of the match"""
    msg(f"You played {state["game_number"]} games!")
    msg(f"You won {state["x_wins"]} games!")
    msg(f"Computer won {state["o_wins"]} games!")

def is_game_done(state: dict):
    winner = get_winner(state["board"])
    if winner or is_board_full(state["board"]):
        return True

    return False

def is_board_full(board: list):
    return not board.count(EMPTY)

def join_or(choices: list, sep=", ", end="or"):
    """returns a formated string with the valid choices"""
    match len(choices):
        case 0:
            return ""
        case 1:
            return f"Valid choice: {green(choices[0]+1)}"
        case _:
            joined = sep.join(green(str(num+1)) for num in choices[:-1])
            return f"Valid choices: {joined}{sep}{end} {green(choices[-1]+1)}"

def get_winner(board: list):
    """returns the winner or 0 if there is no winner"""
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [6,4,2]
    ]
    for player in [X, O]:
        if any(all(board[i] == player for i in combo) for combo in win_combos):
            return player
    return 0

def get_valid_choices(board: list):
    """returns a list of valid moves to make on the board"""
    return [idx for idx, val in enumerate(board) if val == EMPTY]

def minimax(board: list, player: int):
    """finds the best possible move using minimax algorithm"""
    best = [-1, -player]

    winner = get_winner(board)
    if is_board_full(board) or winner:
        return [-1, winner]

    for choice in get_valid_choices(board):
        board[choice] = player
        score = minimax(board, -player)
        board[choice] = EMPTY
        score[0] = choice

        get = min if player == O else max
        best = get(score, best, key=lambda x: x[1])

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
        board[choice] = EMPTY

    for choice in valid_choices:
        board[choice] = X
        if get_winner(board) == X:
            return choice
        board[choice] = EMPTY

    if 4 in valid_choices:
        return 4

    choice = random.choice(valid_choices)
    return choice

def get_hard_move(board: list):
    """returns a hard difficulty move"""
    return minimax(board, O)[0]

def get_computer_choice(valid_choices: list, state: dict):
    """returns a move for the computer"""
    match state["difficulty"]:
        case "easy":
            choice = get_easy_move(valid_choices)
        case "medium":
            choice = get_medium_move(state["board"])
        case "hard":
            choice = get_hard_move(state["board"])
    return choice

def input_player_choice(valid_choices: list, board: list):
    """returns a move for the player"""
    while True:
        msg(join_or(valid_choices))
        choice = input("==> Choose an empty square: ")
        if choice.isdigit() and int(choice) - 1 in valid_choices:
            return int(choice) - 1
        os.system(CLEAR)
        display_board(board)
        msg("That is not a valid choice, please try again")

def input_play_again():
    """returns True if user wants to play again"""
    os.system(CLEAR)
    while True:
        msg("Would you like to play another match?")
        msg(f"{green(1)}: Yes")
        msg(f"{green(2)}: No")
        answer = input("==> ")
        if answer == "2":
            return False
        if answer == "1":
            return True
        os.system(CLEAR)
        msg("Invalid input. Please choose 1 or 2.")

def input_difficulty():
    """asks user for game difficulty"""
    while True:
        diff = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }
        msg("Please choose the game difficulty:")
        msg(f"{green(1)}: Easy")
        msg(f"{green(2)}: Medium")
        msg(f"{green(3)}: Hard")
        choice = input("==> ")
        if choice in diff:
            return diff[choice]
        os.system(CLEAR)
        msg("That was not a valid choice.")

def init_board():
    """returns an empty board"""
    return [EMPTY for _ in range(9)]

def init_state():
    """returns the starting state of the game"""
    state = {
        "difficulty": input_difficulty(),
        "board": [],
        "player": X,
        "game_number": 0,
        "x_wins": 0,
        "o_wins": 0
    }
    return state

def reset_game_state(state: dict):
    """reset state for new game"""
    state["game_number"] += 1
    state["board"] = init_board()
    state["player"] = X

def play_round(state: dict):
    """plays a round of tic tac toe"""
    valid_choices = get_valid_choices(state["board"])
    if state["player"] == O:
        choice = get_computer_choice(valid_choices, state)
        state["board"][choice] = state["player"]
        state["player"] = X
    else:
        choice = input_player_choice(valid_choices, state["board"])
        state["board"][choice] = state["player"]
        state["player"] = O

def play_game(state: dict):
    """play a single game of tic tac toe"""
    while not is_game_done(state):
        play_round(state)
        os.system(CLEAR)
        display_board(state["board"])

def play_match(state: dict):
    """play a match of tic tac toe"""
    while state["x_wins"] != 5 and state["o_wins"] != 5:
        os.system(CLEAR)
        reset_game_state(state)
        display_board(state["board"])
        play_game(state)
        display_winner(state)
        input("Press enter to continue")

def main():
    """main game loop"""
    while True:
        os.system(CLEAR)
        msg("Welcome to Tic Tac Toe")
        msg("First to win 5 games wins!")

        state = init_state()
        play_match(state)

        if not input_play_again():
            msg("Thank you for playing!")
            break

main()
