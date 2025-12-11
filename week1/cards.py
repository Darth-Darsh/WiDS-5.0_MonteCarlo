from enum import Enum

class suit(Enum):
    spades = "♠"
    hearts = "♥"
    diamonds = "♦"
    clubs = "♣"

class Card():
    def __init__(self, value, suit: suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return f"{self.value}{self.suit.value}"
    
class Deck():
    values_list = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(value, suit)
                       for suit in suit
                       for value in self.values_list]        

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def reset(self):
        self.cards = [Card(value, suit)
                        for suit in suit
                        for value in self.values_list] 
        
class Hand():
    def add_card(self, card: Card):
        self.cards.append(card)
    
    def flush(self):
        self.cards = []

    def value(self):
        total = 0
        aces = 0

        for c in self.cards:
            if c.value == "A":
                total += 11
                aces += 1
            elif c.value in ["K", "Q", "J"]:
                total += 10
            else:
                total += int(c.value)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

