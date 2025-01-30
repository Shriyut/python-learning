import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):

    def setUp(self):
        self.three_of_clubs = Card(rank="3", suit="Clubs")
        self.three_of_hearts = Card(rank="3", suit="Hearts")
        self.three_of_spades = Card(rank="3", suit="Spades")
        self.three_of_diamonds = Card(rank="3", suit="Diamonds")
        self.nine_of_spades = Card(rank="9", suit="Spades")

        self.cards = [
            Card(rank = "2", suit = "Spades"),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank = "7", suit = "Clubs"),
            self.nine_of_spades
        ]

    def test_figures_out_four_of_a_kind(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank="3", suit="Hearts"),
            Card(rank="3", suit="Spades"),
            Card(rank="3", suit="Diamonds"),
            Card(rank="9", suit="Spades")
        ]

        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_figures_out_returns_valid_cards(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades
            ]
        )