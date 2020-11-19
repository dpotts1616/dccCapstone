from card import Card

suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
values = ('A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


class Deck:
    def __init__(self):
        self.deck = []
        for x in suits:
            for y in values:
                self.deck.append(Card(x, y))

