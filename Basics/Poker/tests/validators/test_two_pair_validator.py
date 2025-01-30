import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.five_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_figures_out_at_least_two_pair_is_best_hand(self):

        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )