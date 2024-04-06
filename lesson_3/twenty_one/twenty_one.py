from random import shuffle
import os
import time

CLEAR = "cls" if os.name == "nt" else "clear"
SUITS = ["♠", "♥", "♦", "♣"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def msg(message: str):
    print("==>", message)

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

def generate_deck():
    deck = [[suit, value] for value in VALUES for suit in SUITS]
    shuffle(deck)
    return deck

def total_cards(cards: list):
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

def deal_cards(deck: list, num: int):
    cards = []
    for _ in range(num):
        cards.append(deck.pop())
    return cards

def hit_or_stay():
    while True:
        choice = input("==> Would you like to hit or stay? ").strip().lower()
        if choice in ["hit", "h"]:
            return True
        if choice in ["stay", 's']:
            return False
        msg("Incorrect input")

def display_totals(player, dealer):
    player_total = total_cards(player)
    dealer_total = total_cards(dealer)
    msg(f"The dealer has {dealer_total}")
    msg(f"You have {player_total}")

def display_round(player, dealer, hidden=False):
    os.system(CLEAR)
    msg("Dealer Cards:")
    display_hand(dealer, hidden=hidden)
    msg("Player Cards:")
    display_hand(player)
    if hidden:
        display_totals(player, dealer[:-1])
    else:
        display_totals(player, dealer)

def display_winner(player, dealer):
    if total_cards(dealer) > 21:
        msg("Dealer busted! You Win!")
    elif total_cards(dealer) == total_cards(player):
        msg("This round is a tie!")
    elif total_cards(dealer) > total_cards(player):
        msg("Dealer Wins!")
    else:
        msg("You Win!")

def play_again(game_number):
    if game_number:
        return input("==> Would you like to play again? (y / n)") == "y"
    return True

def game():
    game_number = 0
    while play_again(game_number):
        deck = generate_deck()
        player = {"hand": deal_cards(deck, 2)}
        dealer = {"hand": deal_cards(deck, 2)}

        display_round(player["hand"], dealer["hand"], hidden=True)
        player_total = total_cards(player["hand"])
        if total_cards(player["hand"]) == 21:
            msg("You win!")
        else:
            while hit_or_stay():
                player["hand"].extend(deal_cards(deck, 1))
                display_round(player["hand"], dealer["hand"], hidden=True)
                player_total = total_cards(player["hand"])
                if player_total > 21:
                    msg("You busted! Dealer wins!")
                    break
                if player_total == 21:
                    msg("You win!")
                    break

        if total_cards(player["hand"]) < 21:
            time.sleep(1)
            display_round(player["hand"], dealer["hand"])

            while total_cards(dealer["hand"]) < 17:
                time.sleep(1)
                dealer["hand"].extend(deal_cards(deck, 1))
                display_round(player["hand"], dealer["hand"])

            display_winner(player["hand"], dealer["hand"])
        game_number += 1

game()
