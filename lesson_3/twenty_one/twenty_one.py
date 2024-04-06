# ♠ ♥ ♦ ♣
from random import choice, shuffle

SUITS = ["♠", "♥", "♦", "♣"]

VALUES = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [1, 11]
}

def display_cards(cards: list):
    for i in range(7):
        print(cards[0][i], cards[1][i])

def create_card_ascii(card: list):
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
    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append([suit, value])
    shuffle(deck)
    return deck

deck = generate_deck()

card1 = create_card_ascii(deck.pop())
card2 = create_card_ascii(deck.pop())
display_cards([card1, card2])
