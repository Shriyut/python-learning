import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ten_of_clubs = Card(rank="10", suit="Clubs")
        self.jack_of_clubs = Card(rank="Jack", suit="Clubs")
        self.queen_of_clubs = Card(rank="Queen", suit="Clubs")
        self.king_of_clubs = Card(rank="King", suit="Clubs")
        self.ace_of_clubs = Card(rank="Ace", suit="Clubs")

        self.cards = [
            self.ten_of_clubs,
            self.jack_of_clubs,
            self.queen_of_clubs,
            self.king_of_clubs,
            self.ace_of_clubs
        ]

    def test_figures_out_royal_flush(self):
        cards = [
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Clubs")
        ]

        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_determines_not_royal_flush(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_valid_cards(self):

        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
            self.ten_of_clubs,
            self.jack_of_clubs,
            self.queen_of_clubs,
            self.king_of_clubs,
            self.ace_of_clubs

            ]
        )


