import random

class Card:
    """A class for functionality of a card"""

    def __init__(self, value, suit):
        """"Initialise card with suit and value"""
        self.value = value
        self.suit = suit

    def __str__(self):
        """Returns formatted name of card"""
        return f"{self.value} of {self.suit}"

    def get_suit(self):
        """Returns the suit of the card"""
        return self.suit

    def get_value(self):
        """Returns the value of the card"""
        return self.value

    def same_value(self, other_card):
        """Checks to see if the cards have the same value"""
        return self.value == other_card.get_value()

    def same_suit(self, other_card):
        """Checls to see if the cards have the same suit"""
        return self.suit == other_card.get_suit()



class Deck:
    """A class for a deck of cards"""

    def __init__(self):
        """initialise deck class"""
        self.cards = []

    def build_deck(self):
        """creates a list containing a standard deck of cards"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace', '2', '3', '4',
                    '5', '6', '7', '8',
                    '9', '10', 'Jack', 
                    'Queen', 'King']
        
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)
    
    def shuffle_deck(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)
    
    def deal_top_card(self):
        """
        Removes and returns top card from deck
        Top card is at index 0
        """
        return self.cards.pop(0)

    def get_random_card(self):
        """Removes and returns a random card from the deck"""
        random_card = random.randint(0, len(self.cards)-1)
        return self.cards.pop(random_card)

    def deal_hand(self, hand_size):
        """"Deals out a numbner of cards from deck"""
        hand = []

        while hand_size > 0:
            hand.append(self.deal_top_card())    

            hand_size -= 1
        
        return hand


class Player:
    """Class representing a player of Go Fish"""

    def __init__(self, hand):
        """Initialise a Player"""
        self.hand = hand
        self.score = 0
        