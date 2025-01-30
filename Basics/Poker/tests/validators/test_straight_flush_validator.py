import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank="3", suit="Clubs")
        self.four_of_clubs = Card(rank="4", suit="Clubs")
        self.five_of_clubs = Card(rank="5", suit="Clubs")
        self.six_of_clubs = Card(rank="6", suit="Clubs")
        self.seven_of_clubs = Card(rank="7", suit="Clubs")

        self.cards = [
            self.three_of_clubs,
            self.four_of_clubs,
            self.five_of_clubs,
            self.six_of_clubs,
            self.seven_of_clubs,
            Card(rank = "Jack", suit = "Hearts")
        ]

    def test_figures_out_straight_flush(self):
        validator = StraightFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_determines_not_straight_flush(self):
        cards = [
                Card(rank = "3", suit = "Clubs"),
                Card(rank="4", suit="Clubs"),
                Card(rank="5", suit="Clubs"),
                Card(rank="6", suit="Clubs"),
                Card(rank="7", suit="Diamonds"),
                Card(rank = "King", suit = "Clubs"),
                Card(rank = "Ace", suit = "Diamonds")
            ]
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_valid_cards(self):
        cards = [
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
            Card(rank="6", suit="Clubs"),
            Card(rank="7", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds")
        ]
        validator = StraightFlushValidator(cards=cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                Card(rank="3", suit="Clubs"),
                Card(rank="4", suit="Clubs"),
                Card(rank="5", suit="Clubs"),
                Card(rank="6", suit="Clubs"),
                Card(rank="7", suit="Clubs")
            ]
        )