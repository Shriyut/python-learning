from poker.deck import Deck
from poker.card import Card

# card1 = Card(rank="2", suit="Spades")
# card2 = Card(rank="Ace", suit="Hearts")

# from main import card1, card2

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)
