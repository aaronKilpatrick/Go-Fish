from deck import Card, Deck
from player import User, Computer

class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.build_deck()
        self.deck.shuffle_deck()
        
        self.user = User(self.deck.deal_hand())
        self.com = Computer(self.deck.deal_hand())

    def is_game_over(self):
        """
        Game is over if there are no cards in either hand left.
        Prints game over text
        Returns boolean
        """
        user_hand_len = self.user.num_cards_hand()
        com_hand_len = self.com.num_cards_hand()

        if user_hand_len <= 0 or com_hand_len <= 0:
            print(f"Score:\n You - {self.user.score} Com - {self.com.score}")
            if self.user.score > self.com.score:
                print("\nYou win!")
            elif self.user.score < self.com.score:
                print("\nYou lose!")
            else:
                print("\nIt's a draw!")
        
            return True

        return False

    def card_selection_menu(self):        

        while True:
            hand_size = self.user.num_cards_hand()

            try:
                users_selection = int(input("\nWhat card do you want to ask for? "))
            except ValueError:
                print(f"Please enter a number between 1 and {hand_size}")
            else:
                # Make sure user selection is within the acceptable options
                if users_selection < 1 or users_selection > hand_size:
                    print(f"Please enter a number between 1 and {hand_size}")
                else:
                    break

        # Adjust user selection for use as hand index
        return self.user.hand[users_selection-1]

    def player_turn(self, active_player, other_player, requested_card):
        """Facilitates the turn of each player"""
        print(f"{active_player.name}: Do you have any {requested_card}?")

        if other_player.check_for_requested_card(requested_card):
            print(f"{other_player.name}: Yes I have a {requested_card}")
            active_player.rm_card(requested_card)
            active_player.increment_score()

        else:
            print(F"\n{other_player.name}: Go fish!\n")
            drawn_card = self.deck.deal_top_card()

            if active_player.name == 'You':
                print(f"{active_player.name} drew a {drawn_card}")

            active_player.hand.append(drawn_card)
            active_player.pairs_in_hand()

    def play_game(self):
        print("Let's play go fish\n")
        
        # Game loop
        while True:
            #Check both users hands for pairs
            self.user.pairs_in_hand()
            self.com.pairs_in_hand()

            # Check if game over
            if self.is_game_over():
                break

            # Show users cards
            self.user.print_hand()
            print("Com")
            self.com.print_hand()

            # Users turn
            requested_card = self.card_selection_menu()
            self.player_turn(self.user, self.com, requested_card)
            if self.is_game_over():
                break

            # computers turn
            requested_card = self.com.choose_card()
            self.player_turn(self.com, self.user, requested_card)
            if self.is_game_over():
                break

game = Game()
game.play_game()