from Basics.Poker.poker.card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    # def create_cards(self):
    #     cards = []
    #     for suit in Card.SUITS:
    #         for rank in Card.RANKS:
    #             Card()
    #
    #     self.add_cards(cards)