import random
import os
from copy import deepcopy
from color import b,r,g

O = [b(" █████ "), b("██   ██"), b("██   ██"), b("██   ██"), b(" █████ ")]
X = [r("██   ██"), r(" ██ ██ "), r("  ███  "), r(" ██ ██ "), r("██   ██")]
B = ["       ", "       ", "       ", "       ", "       "]
CLEAR = "cls" if os.name == "nt" else "clear"

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

def init_board():
    return [B for _ in range(9)]

def is_board_full(board: list):
    return not board.count(B)

def is_winner(board: list):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [6,4,2]
    ]
    for combo in win_combos:
        if len([board[i] for i in combo if board[i] == X]) == 3:
            return "X"
        if len([board[i] for i in combo if board[i] == O]) == 3:
            return "O"
    return False

def find_best_move(board: list):
    valid_choices = [idx for idx, val in enumerate(board) if val == B]

    for choice in valid_choices:
        temp = deepcopy(board)
        temp[choice] = O
        if is_winner(temp) == "O":
            return choice

    for choice in valid_choices:
        temp = deepcopy(board)
        temp[choice] = X
        if is_winner(temp) == "X":
            return choice

    if 4 in valid_choices:
        return 4
    choice = random.choice(valid_choices)
    return choice

def play_round(board: list, player: str, difficulty="Easy"):
    valid_choices = [idx for idx, val in enumerate(board) if val == B]
    if player[0] == O:
        if difficulty == "Easy":
            choice = random.choice(valid_choices)
        elif difficulty == "Medium":
            choice = find_best_move(board)
        board[choice] = player[0]
        player[0] = X
    else:
        while True:
            print("valid choices: ", ", ".join(g(str(num+1)) for num in valid_choices))
            choice = int(input("Choose an empty square: "))-1
            if choice in valid_choices:
                board[choice] = player[0]
                player[0] = O
                break
            print("That is not a valid choice, please try again")

def is_game_done(board: list):
    winner = is_winner(board)
    if winner:
        print(f"{winner} has won the game!")
        return True

    if is_board_full(board):
        print("The game is a tie!")
        return True

def play_again(game_number):
    if game_number > 0:
        answer = input("Play again? y/n: ")
        if answer != "y":
            print("Thanks for playing!")
            return False
    return True

def play():
    game_number = 0
    difficulty = "Medium"
    while play_again(game_number):
        os.system(CLEAR)

        board = init_board()
        player = [X]

        display_board(board)

        while True:
            if is_game_done(board):
                break

            play_round(board, player, difficulty)
            os.system(CLEAR)
            display_board(board)

        game_number += 1
    print(f"You played {game_number} games!")


play()
