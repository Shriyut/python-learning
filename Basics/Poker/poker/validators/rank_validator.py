class RankValidator:
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self.cards) - 1
        collections_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index:
            next_five_cards = self.cards[index: index + 5]
            next_five_rank_indices = [
                card.rank_index for card in next_five_cards
            ]
            if self._every_element_increasing_by_1(next_five_rank_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)
            index += 1

        return collections_of_five_straight_cards_in_a_row

    def _every_element_increasing_by_1(self, rank_indexes):
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        return rank_indexes == straight_consecutive_indexes