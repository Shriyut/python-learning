import unittest
from unittest.mock import MagicMock

from Basics.Poker.poker.player import Player
from Basics.Poker.poker.hand import Hand
from Basics.Poker.poker.card import Card

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Gambledore", hand = hand)
        self.assertEqual(player.name, "Gambledore")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Michael Addamo", hand = mock_hand)
        player.best_hand()
        mock_hand.best_rank.assert_called()

    def test_figures_out_player_rank(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Chris MoneyMaker", hand = mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )

    def test_passes_card_from_deck_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Phil Ivey", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)


    def test_decides_to_continue_or_Drop_out_of_hand(self):
        player = Player(name = "Jungleman", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_player_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four Of A Kind", [])

        player1 = Player(name = "Olga", hand = mock_hand1)
        player2 = Player(name = "Maria Ho", hand = mock_hand2)

        players = [player1, player2]
        self.assertEqual(
            max(players),
            player1
        )