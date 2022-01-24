import unittest
from deck import Player, Card

class TestPlayerClass(unittest.TestCase):
    """Tests for Player class"""

    def setUp(self):
        """Create player class attributes"""
        self.hand = [
            Card('Ace', 'Hearts'),
            Card('Ace', 'Diamons'),
            Card('2', 'Hearts'),
            Card('3', 'Hearts'),
            Card('2', 'Clubs'),
            Card('Jack', 'Spades'),
            Card('3', 'Spades'),
        ]

        self.player = Player(self.hand)


    def test_pairs_in_hand_removes_all_pairs(self):
        """
        Tests if pairs_in_hand removes all pairs
        """
        self.player.pairs_in_hand()
        expected_hand = ['Jack']
        current_hand = []
        for card in self.player.hand:
            current_hand.append(card.get_value())

        self.assertListEqual(current_hand, expected_hand)

    def test_check_for_requested_card_pass(self):
        """
        Tests is requested card returns true if card value matches
        """
        requested_card = Card('Jack', 'Spades')
        test_function = self.player.check_for_requested_card(requested_card)
        message = "check_for_requested_card() - Pass"
        self.assertTrue(test_function, message)

    def test_check_for_requested_card_fail(self):
        """
        Tests is requested card returns true if card value matches
        """
        requested_card = Card('Queen', 'Clubs')
        test_function = self.player.check_for_requested_card(requested_card)
        message = "check_for_requested_card() - Fail"
        self.assertFalse(test_function, message)


if __name__ == '__main__':
    unittest.main()
    