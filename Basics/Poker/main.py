from poker.game_round import GameRound
from poker.deck import Deck
from poker.card import Card
from poker.hand import Hand
from poker.player import Player

# card1 = Card(rank="2", suit="Spades")
# card2 = Card(rank="Ace", suit="Hearts")

# from main import card1, card2

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# deck.cards.extend(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Doug Polk", hand = hand1)
player2 = Player(name = "Tony G", hand = hand2)
players = [player1, player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()

print(player1.hand.cards)
print(player2.hand.cards)
print(len(deck.cards))
print(len(deck))

print(player1.best_hand())
print(player2.best_hand())