from Basics.Poker.poker.validators import RankValidator

class PairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Pair"

    def is_valid(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2)
        valid_cards = [
            card for card in self.cards if card.rank in ranks_with_pairs.keys()
        ]
        return valid_cards