# Import Python STD Library modules
import random as rand
from typing import List

# Constants
SUITS = ["♣", "♦", "♥", "♠"]
NUM_SUIT = 4
NUM_RANK = 13

class Card:
    """
    A class that represents a card with 4 suits and 13 ranks.

    Attributes:
        suit (str): The suit of the card, see SUITS in Constants
        rank (int): Card rank from 1-13
    
    Methods:
        __repr__: Used for printing suit and rank in debugging 
        getSuit : Return the suit of the card
        getRank : Return the rank of the card
    """

    # Construct by suit and rank
    def __init__(self, suit: str, rank: int) -> bool:
        """
        Default constructor. Returns False if suit and rank are not valid.

        Parameters:
            suit (str): Suit of card
            rank (int): Rank of card

        Returns:
            bool: True if card construction was successful
        """

        # If suit and rank valid, initialize and return true
        if (suit in SUITS) and (rank in range(1, NUM_RANK + 1)):
            self.suit = suit
            self.rank = rank
            return True

        # Return False if suit and rank check fail 
        return False

    def __repr__(self) -> str:
        """
        Method used for printing suit and rank in debugging.

        Parameters:
            None

        Returns:
            str: Concatenated suit and rank
        """

        return f"{self.suit}, {self.rank}"

    def getSuit(self) -> str:
        """
        Get suit of card.

        Parameters:
            None

        Returns:
            str: Suit of card, as a symbol
        """

        return self.suit
    
    def getRank(self) -> int:
        """
        Get rank of card.

        Parameters:
            None

        Returns:
            int: Rank of card
        """

        return self.rank


class Deck:
    def __init__(self):
        """
        A class that represents a standard 52 card deck.

        Attributes:
            deck (List[Card]): An array of 52 cards.
        
        Methods:
            get     : Return the deck
            drawCard: Randomly draw a card and update the deck
        """

        # Create empty deck of 52 cards
        self.deck = [[] for _ in range(NUM_SUIT)]

        # Populate deck with 4 suits, 13 ranks each
        for suitIndex, suit in enumerate(SUITS):
            for rank in range(NUM_RANK):
                self.deck[suitIndex].append(Card(suit, rank + 1))

    def get(self) -> List[Card]:
        """
        Get deck; an array of cards.

        Parameters:
            None

        Returns:
            List[Card]: An array of cards
        """

        return self.deck

    def drawCard(self) -> Card:
        """
        Return a random card. Removes the card from the deck when drawn.

        Parameters:
            None

        Returns:
            Card: A random card
        """

        # Get suits that aren't empty
        nonEmptySuits = [suit for suit in self.deck if suit]

        if nonEmptySuits:
            # Randomly select suit
            randSuit = rand.choice(nonEmptySuits)

            # Randomly pop card
            return randSuit.pop(rand.randint(0, len(randSuit) - 1))

        # If deck is empty, return none
        else:
            return None