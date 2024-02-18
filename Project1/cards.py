import random as rand
import numpy as np

SUIT = ["♣", "♦", "♥", "♠"]
NUM_SUIT = 4
NUM_RANK = 13

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank

class Deck:
    def __init__(self):
        self.deck = np.empty([NUM_SUIT, NUM_RANK], dtype=Card)

        # Iterate suits
        for index, suit in enumerate(SUIT):
            # Iterate ranks
            for rank in np.arange(1, NUM_RANK, 1):
                self.deck[index] = Card(suit, rank)

    def get(self):
        return self.deck

    def getCard(self):
        return np.random.choice(self.deck)       

        
