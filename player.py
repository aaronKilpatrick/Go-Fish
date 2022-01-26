import random

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

    def rm_card(self, card):
        """Removes card from hand"""
        self.hand.remove(card)

    def pairs_in_hand(self):
        """Checks if there are any pairs in hand"""
        # FIX
        # Show what pairs have been taken out on draw
        temp_hand = []
        while len(self.hand) > 0:
            current_card = self.hand.pop(0)
            
            for card in self.hand:
                if current_card.same_value(card):
                    self.rm_card(card)
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
                self.rm_card(card)
                return True
        
        return False

    def num_cards_hand(self):
        """return how many cards are in hand"""
        return len(self.hand)


    def print_hand(self):
        print("\n===========================")
        print(f"Current Score: {self.score}")
        print("===========================")
        print("Cards in hand")
        
        for i, card in enumerate(self.hand):
            print(f"{i+1} - {card}")

class User(Player):
    """Extends Player"""

    def __init__(self, hand):
        super().__init__(hand)
        self.name = 'You'

    def pairs_in_hand(self):
        """Checks if there are any pairs in hand"""
        # FIX
        # Show what pairs have been taken out on draw
        temp_hand = []
        while len(self.hand) > 0:
            current_card = self.hand.pop(0)
            
            for card in self.hand:
                if current_card.same_value(card):
                    print(f"You found a pair of {card.value} in your hand! Score!")
                    self.rm_card(card)
                    current_card = ""
                    
                    self.increment_score()
                    break

            if current_card:
                temp_hand.append(current_card)

        self.hand = temp_hand



class Computer(Player):
    """Class that controls computer actions"""

    def __init__(self, hand):
        super().__init__(hand)
        self.name = 'Computer'

    def choose_card(self):
        """Chooses card from hand"""
        hand_len = self.num_cards_hand()
        card_position = random.randint(0, hand_len-1)
        return self.hand[card_position]