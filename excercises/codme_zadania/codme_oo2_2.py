import random


class CardDeck:
    COLOURS = ["H", 'C', 'D', 'S']
    FIGURES = ['A', '2','3', '4', '5', '6','7','8','9','10','J','Q','K']

    def __init__(self):
        cards = []
        for colour in self.COLOURS:
            for figure in self.FIGURES:
                cards.append((figure, colour))
        self.cards = list(set(cards))

    def print_deck(self):
        print(self.cards)
    
    def shuffle_deck(self):
        self.cards = list(set(self.cards))

    def take_first(self):
        card = self.cards.pop(0)
        print(card)
    
    def take_random(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        print(card)

if __name__ == '__main__':
    d1 = CardDeck()
    d1.print_deck()
    d1.take_first()
    d1.print_deck()
    d1.take_random()

