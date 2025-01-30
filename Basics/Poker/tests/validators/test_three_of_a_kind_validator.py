import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        ace = Card(rank="Ace", suit="Spades")
        five =  Card(rank="5", suit="Clubs")
        self.king_of_clubs = Card(rank="King", suit="Clubs")
        self.king_of_hearts = Card(rank="King", suit="Hearts")
        self.king_of_diamonds = Card(rank="King", suit="Diamonds")

        self.cards = [
            five,
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            ace
        ]

    def test_figures_out_exactly_three_of_a_kind(self):

        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_3_of_a_kind_from_card_collection(self):

        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts
            ]
        )
