class GameRound:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        # shuffle the deck
        self._shuffle_deck()
        # hand out 2 cards to each player
        self._deal_initial_two_cards_to_each_player()
        # ask for wagers
        self._make_bets()


        self._deal_flop_cards()
        self._make_bets()
        self._deal_turn_card()
        self._make_bets()
        self._deal_river_card()
        self._make_bets()


    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _deal_flop_cards(self):
        community_cards = self.deck.remove_cards(3)
        for player in self.players:
            player.add_cards(community_cards)

    def _deal_turn_card(self):
        community_card = self.deck.remove_cards(1)
        for player in self.players:
            player.add_cards(community_card)

    def _deal_river_card(self):
        community_card = self.deck.remove_cards(1)
        for player in self.players:
            player.add_cards(community_card)