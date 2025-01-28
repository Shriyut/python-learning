import unittest
from unittest.mock import MagicMock, call
from Basics.Poker.poker.game_round import GameRound
from Basics.Poker.poker.card import Card

class GameRoundTest(unittest.TestCase):
    def setUp(self):

        self.first_two_cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Clubs")
        ]

        self.next_two_cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "4", suit = "Spades")
        ]

        self.flop_cards = [
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "10", suit = "Spades")
        ]

        self.turn_card = [
            Card(rank = "9", suit = "Hearts")
        ]

        self.river_card = [
            Card(rank = "Queen", suit = "Clubs")
        ]


    def test_stores_deck_and_player(self):
        deck = MagicMock()
        players = [
            MagicMock(), MagicMock()
        ]

        game_round = GameRound(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game_round.deck,
            deck
        )

        self.assertEqual(
            game_round.players,
            players
        )

    def test_gameplay_shuffles_deck(self):
        deck = MagicMock()
        players = [
            MagicMock(), MagicMock()
        ]

        game_round = GameRound(
            deck = deck,
            players = players
        )

        game_round.play()
        deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_to_each_player(self):
        deck = MagicMock()

        mock_player_1 = MagicMock()
        mock_player_2 = MagicMock()
        players = [
            mock_player_1, mock_player_2
        ]

        deck.remove_cards.side_effect = [self.first_two_cards,
                                         self.next_two_cards,
                                         self.flop_cards,
                                         self.turn_card,
                                         self.river_card]

        game_round = GameRound(
            deck = deck,
            players = players
        )

        game_round.play()
        deck.remove_cards.assert_has_calls([
            call(2), call(2) # once for each player
        ])

        # mock_player_1.add_cards.assert_called_with(self.first_two_cards)
        mock_player_1.add_cards.assert_has_calls([call(self.first_two_cards)])
        # mock_player_2.add_cards.assert_called_with(self.next_two_cards)
        mock_player_2.add_cards.assert_has_calls([call(self.next_two_cards)])

    def test_removes_player_if_wants_to_fold(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False

        players = [player1, player2]
        game_round = GameRound(deck = deck, players = players)
        game_round.play()

        self.assertEqual(
            game_round.players,
            [player2]
        )

    def test_deals_3_flop_cards_1_turn_and_1_river_card(self):
        mock_player1 = MagicMock()
        # mock_player1_wants_to_fold returns a magic mock
        # any method or attribute on a magic mock will return a magic mock by default
        # and magic mock is considered as true so the player will automatically fold if not considered
        mock_player1.wants_to_fold.return_value = False

        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        game_round = GameRound(deck = mock_deck, players = players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(3),
            call(1),
            call(1)
        ])

        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)

        # mock_player1.add_cards.assert_called_with(self.flop_cards)
        # mock_player2.add_cards.assert_called_with(self.flop_cards)


