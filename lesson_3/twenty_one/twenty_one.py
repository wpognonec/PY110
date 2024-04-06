# ♠ ♥ ♦ ♣
from random import choice, shuffle

SUITS = ["♠", "♥", "♦", "♣"]

VALUES = ["1", "2", "3", "4", "5", "6", "7", 
          "8", "9", "10", "J", "Q", "K", "A"]

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

deck = generate_deck()
print(len(deck))
hand = deal_cards(deck, 2)
total = total_cards(hand)
hand.extend(deal_cards(deck, 1))
total = total_cards(hand)
print(hand)
print(total)

card1 = create_card_ascii(hand[0])
card2 = create_card_ascii(hand[1])
display_cards([card1, card2])
print(len(deck))