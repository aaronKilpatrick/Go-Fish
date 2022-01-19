import re
from random import randint

##############################
# Basic Card Functions
##############################

def build_deck():
    """returns a list containing a standard deck of cards"""

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = []

    for suit in suits:
        for value in range(1, 14):
            if value == 1:
                deck.append(f'Ace of {suit}')
                continue
            if value == 11:
                deck.append(f'Jack of {suit}')
                continue
            if value == 12:
                deck.append(f'Queen of {suit}')
                continue
            if value == 13:
                deck.append(f'King of {suit}')
                continue

            deck.append(f"{value} of {suit}")
    
    return deck


def get_suit(card):
    """Returns the suit of the card"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    for suit in suits:
        if suit in card:
            return suit
    
    return "Error - No suit found"


def get_value(card):
    """Returns the value of the given card"""
    named_cards = {
        'Ace': 'A',
        'Jack': 'J',
        'Queen': 'Q',
        'King': 'K'
        }

    # Check if card is face and return value if so
    for face, value in named_cards.items():
        if face in card:
            return value
    
    # Card is not a face so return numeric value of card
    card_value = re.findall(r'\d+', card)
    return card_value[0]


def same_value(card_1, *cards):
    """
    Checks to see if cards have the same value
    Returns boolean
    """
    card_1 = get_value(card_1)
    for card in cards:
        card = get_value(card)
        if card_1 != card:
            return False

    return True


def same_suit(card_1, *cards):
    """
    Checks to see if cards have the same suit
    Returns boolean
    """
    card_1_suit = get_suit(card_1)
    for card in cards:
        other_card_suit = get_suit(card)

        if card_1_suit != other_card_suit:
            return False
        
    return True


##############################
# Basic Deck Functions
##############################

def deal_top_card(deck):
    """
    Removes and returns top card from deck 
    Top card is in place 0
    """
    return deck.pop(0)

def get_random_card(deck):
    """Removes and returns a random card from deck"""
    random_card = randint(0, len(deck)-1)
    return deck.pop(random_card)

def shuffle_deck(deck):
    """Shuffles and returns deck"""
    deck_length = len(deck)
    counter = 0

    # iterate card shuffle 5000 times
    while  counter < 5000:
        counter += 1
        random_card = get_random_card(deck)
        insert_position = randint(0, deck_length-1)

        deck.insert(insert_position, random_card)
    
    return deck


def deal_hands(deck, number_of_hands, hand_size):
    """
    Deals out hands
    removes dealt cards from deck
    """
    hands = []
    
    while number_of_hands > 0:
        current_hand = []
        card_count = 0

        while card_count < hand_size:
            card = deal_top_card(deck)
            current_hand.append(card)
            
            card_count += 1

        hands.append(current_hand)
        number_of_hands -= 1
        
    return hands

# GROSS Revisit this - Terrible, hacky code
def pairs_in_hand(hand):
    """Checks to see if hand has any pairs"""
    for index in range(0, len(hand)+1):
        current_card = hand.pop(index)
        pair_found = False

        # Check if card matches the popped current_card
        for card in hand:
            if same_value(current_card, card):
                hand.remove(card)
                pair_found = True
                break
        
        # replace unpaired card into hand
        if not pair_found:
            hand.insert(index, current_card)

        if index >= len(hand)-1:
            break