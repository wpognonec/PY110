from random import shuffle
import os
import time

CLEAR = "cls" if os.name == "nt" else "clear"
SUITS = ["♠", "♥", "♦", "♣"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def msg(message: str):
    print("==>", message)

def create_card_ascii(card: list, hidden=False):
    if hidden:
        return ["┌─────────┐", "│ ?       │",
                "│         │", "│    ?    │",
                "│         │", "│       ? │",
                "└─────────┘"]
    if card[1] == "10":
        return ["┌─────────┐", f"│ {card[1]}      │",
                "│         │", f"│    {card[0]}    │",
                "│         │", f"│      {card[1]} │",
                "└─────────┘"]
    return ["┌─────────┐", f"│ {card[1]}       │",
            "│         │", f"│    {card[0]}    │",
            "│         │", f"│       {card[1]} │",
            "└─────────┘"]

def display_hand(cards: list, hidden=False):
    ascii_cards = []
    for card in cards:
        if card == cards[-1] and hidden:
            ascii_cards.append(create_card_ascii(card, hidden=True))
        else:
            ascii_cards.append(create_card_ascii(card))

    for i in range(7):
        ascii_line = " ".join(card[i] for card in ascii_cards)
        print(ascii_line)

def display_cards(player, dealer, hidden=False):
    os.system(CLEAR)
    msg("Dealer Cards:")
    display_hand(dealer, hidden=hidden)
    msg("Player Cards:")
    display_hand(player)
    if hidden:
        display_totals(player, dealer[:-1])
    else:
        display_totals(player, dealer)

def display_totals(player, dealer):
    player_total = get_hand_total(player)
    dealer_total = get_hand_total(dealer)
    msg(f"The dealer has {dealer_total}")
    msg(f"You have {player_total}")

def display_winner(player, dealer):
    dealer_total = get_hand_total(dealer["hand"])
    player_total = get_hand_total(player["hand"])

    if dealer_total > 21:
        msg("Dealer busted! You Win!")
        player["money"] += player["bet"] * 1.5
    elif player_total > 21:
        msg("You busted! Dealer Wins!")
        player["money"] -= player["bet"]
    elif dealer_total == player_total:
        msg("This round is a tie!")
    elif dealer_total > player_total:
        msg("Dealer Wins!")
        player["money"] -= player["bet"]
    else:
        msg("You Win!")
        player["money"] += player["bet"] * 1.5

def init_deck():
    deck = [[suit, value] for value in VALUES for suit in SUITS]
    shuffle(deck)
    return deck

def get_hand_total(cards: list):
    total = 0
    aces = 0
    for card in cards:
        if card[1] in ["J", "Q", "K", "10"]:
            total += 10
        elif card[1] in "123456789":
            total += int(card[1])
        elif card[1] == "A":
            aces += 1
    for _ in range(aces):
        if total < 12 - aces:
            total += 11
        else:
            total += 1
    return total

def reset_hands(hands: list[list]):
    for hand in hands:
        hand.clear()


def deal_cards(hand: list, deck: list, num: int):
    for _ in range(num):
        hand.append(deck.pop())

def input_hit_or_stay():
    while True:
        choice = input("==> Would you like to hit or stay? ").strip().lower()
        if choice in ["hit", "h"]:
            return True
        if choice in ["stay", 's']:
            return False
        msg("Incorrect input")

def input_play_again(game_number):
    if game_number:
        return input("==> Would you like to play again (y / n)? ") == "y"
    return True

def input_bet(money: int):
    while True:
        bet = int(input(
            f"==> You have {money}$. How much would you like to bet? "
            ))
        if bet <= money:
            return bet
        msg("You do not have enough for that bet.")

def is_player_turn(player):
    player_total = get_hand_total(player["hand"])
    if player_total > 20 or not input_hit_or_stay():
        return False
    return True

def main():
    game_number = 0
    player = {
        "hand": [],
        "money": 500,
        "bet": 0
        }
    dealer = {
        "hand": []
        }
    while input_play_again(game_number):
        deck = init_deck()
        reset_hands([player["hand"], dealer["hand"]])
        player["bet"] = input_bet(player["money"])
        deal_cards(player["hand"], deck, 2)
        deal_cards(dealer["hand"], deck, 2)
        display_cards(player["hand"], dealer["hand"], hidden=True)

        while is_player_turn(player):
            deal_cards(player["hand"], deck, 1)
            display_cards(player["hand"], dealer["hand"], hidden=True)

        if get_hand_total(player["hand"]) < 21:
            time.sleep(1)
            display_cards(player["hand"], dealer["hand"])

            while get_hand_total(dealer["hand"]) < 17:
                time.sleep(1)
                deal_cards(dealer["hand"], deck, 1)
                display_cards(player["hand"], dealer["hand"])

        display_winner(player, dealer)
        game_number += 1

main()
