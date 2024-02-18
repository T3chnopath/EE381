import random as rand
import numpy as np

SUITS = ["♣", "♦", "♥", "♠"]
NUM_SUIT = 4
NUM_RANK = 13

class Card:
    # Construct by suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Printing for debug
    def __repr__(self):
        return f"{self.suit}, {self.rank}"

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank

class Deck:
    def __init__(self):
        # Create empty deck
        self.deck = [[] for _ in range(NUM_SUIT)]

        # Populate deck
        for suitIndex, suit in enumerate(SUITS):
            for rank in range(NUM_RANK):
                self.deck[suitIndex].append(Card(suit, rank + 1))

    def get(self):
        return self.deck

    def drawCard(self):
        # Get suits that aren't empty
        nonEmptySuits = [suit for suit in self.deck if suit]

        if nonEmptySuits:
            # Randomly select suit
            randSuit = rand.choice(nonEmptySuits)

            # Randomly pop card
            return randSuit.pop(rand.randint(0, len(randSuit) - 1))

        else:
            return None