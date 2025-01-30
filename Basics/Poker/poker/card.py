class Card:

    SUITS = ("Hearts", "Spades", "Clubs", "Diamonds")

    RANKS = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    )

    @classmethod
    def create_standard_52_cards(cls):

        return [
            cls(rank = rank, suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

        # cards = []
        # for suit in cls.SUITS:
        #     for rank in cls.RANKS:
        #         # cards.append(1)
        #         cards.append(cls(rank = rank, suit = suit))
        # return cards



    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank, it should be {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit, it should be {self.SUITS}")

        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', {self.suit})"

    def __eq__(self, other_card_object):
        return self.rank == other_card_object.rank and self.suit == other_card_object.suit

    # adding dunder less than to sort the card objects
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit # based on first char of string
        return self.rank_index < other.rank_index
        # current_card_rank_index = self.RANKS.index(self.rank)
        # other_card_rank_index = self.RANKS.index(other.rank)
        # return current_card_rank_index < other_card_rank_index