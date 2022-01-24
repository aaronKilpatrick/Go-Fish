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
        """Checks to see if the cards have the same suit"""
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

    def deal_hand(self, hand_size=7):
        """"Deals out a number of cards from deck"""
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
        
    def increment_score(self, score=1):
        """
        Increment self.score
        Default value = 1
        """
        self.score += score

    def pairs_in_hand(self):
        """Checks if there are any pairs in hand"""
        temp_hand = []
        while len(self.hand) > 0:
            current_card = self.hand.pop(0)
            
            for card in self.hand:
                if current_card.same_value(card):
                    self.hand.remove(card)
                    current_card = ""
                    
                    self.increment_score()

                    break

            if current_card:
                temp_hand.append(current_card)

        self.hand = temp_hand
    

    def check_for_requested_card(self, requested_card):
        """
        Checks if player has requested card in hand
        Returns true if match found
        Removes card from hand
        """
        for card in self.hand:
            if requested_card.same_value(card):
                self.hand.remove(card)
                return True
        
        return False

    def print_hand(self):
        print("\n===========================")
        print(f"Current Score: {self.score}")
        print("===========================")
        print("Cards in hand")
        
        for i, card in enumerate(self.hand):
            print(f"{i+1} - {card}")


def turn(player, bot):
    """
    One turn of play
    """
    player.pairs_in_hand()

    # Player move selection 
    player.print_hand()

    while True:
        hand_size = len(player.hand)
        try:
            players_selection = int(input("\nWhat card do you want to ask for? "))
        except ValueError:
            print(f"Please enter a number between 1 and {hand_size}")
        else:
            # Make sure player selection is within the acceptable options
            if players_selection < 1 or players_selection > hand_size:
                print(f"Please enter a number between 1 and {hand_size}")
            else:
                break
    
    # Adjust user selection for use as hand index
    players_selection -= 1 

    #Bot checks cards
    card_found = bot.check_for_requested_card(player.hand[players_selection])

    if card_found:
        del player.hand[players_selection]
        player.print_hand()
    else:
        print("Go fish")

# deck = Deck()
# deck.build_deck()
# deck.shuffle_deck()

# player = Player(deck.deal_hand())
# bot = Player(deck.deal_hand())

# turn(player, bot)


