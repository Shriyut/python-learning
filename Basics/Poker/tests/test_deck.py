import unittest

from Basics.Poker.poker.card import Card
from Basics.Poker.poker.deck import Deck

class DeckTest(unittest.TestCase):
    def test_stores_no_cards(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_add_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit="Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )