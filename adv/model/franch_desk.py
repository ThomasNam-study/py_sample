import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def spades_high(card):
        rank_value = FrenchDesk.ranks.index(card.rank)

        return rank_value * len(FrenchDesk.suit_values[card.suits])


# beer_card = Card('7', 'diamonds')

deck = FrenchDesk()
print(len(deck))
print(deck[0])

# 랜덤 초이스
print(choice(deck))

print(deck[:3])

for card in reversed(deck):
    print(card)