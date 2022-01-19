import re

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


deck = build_deck()
