class FlushValidator:
    def __init__(self, cards):
        self.cards = cards,
        self.name = "Flush"

    def is_valid(self):
        return len(self._suit_that_occur_5_or_more_times) == 1

    def valid_cards(self):

        # TODO: [0] added because of below error
        cards = [card for card in self.cards[0] if card.suit in self._suit_that_occur_5_or_more_times.keys()]
        return cards[-5:]

    @property
    def _suit_that_occur_5_or_more_times(self):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }

    @property
    def _card_suit_counts(self):
        # print(self.cards[0])
        # print(str(type(self.cards))+" from property")
        # TODO: In previous logic from hand.py self.cards was list but here its tuple hence [0] in loop, figure out whats causing this for same logic
        card_suit_counts = {}
        for card in self.cards[0]:
            print(card)
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts