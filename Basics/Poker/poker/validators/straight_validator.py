from Basics.Poker.poker.validators import RankValidator


class StraightValidator(RankValidator):
    # TODO: Bug where it considers duplicates cards as straight
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]




