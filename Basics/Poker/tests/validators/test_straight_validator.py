import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    # TODO: add test case to check if its able to figure out higher straight between two players
    def setUp(self):
        two = Card(rank="2", suit="Spades")
        six = Card(rank="6", suit="Hearts")
        self.seven = Card(rank="7", suit="Diamonds")
        self.eight =  Card(rank="8", suit="Spades")
        self.nine = Card(rank="9", suit="Clubs")
        self.ten = Card(rank="10", suit="Clubs")
        self.jack = Card(rank="Jack", suit="Spades")

        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_determines_five_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_higher_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack
            ]
        )

    def test_does_not_deem_two_consecutive_card_as_Straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]
        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )
