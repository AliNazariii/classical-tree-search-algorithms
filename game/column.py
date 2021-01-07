class Column:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.insert(0, card)

    def __repr__(self):
        cards = ""
        if self.__len__() > 0:
            for card in self.cards:
                cards += str(card) + " "
        else:
            cards += "#"
        return cards

    def __eq__(self, column):
        if self.__len__() == column.__len__():
            for card in self.cards:
                if card not in column.cards:
                    return False
            return True
        return False

    def __len__(self):
        return len(self.cards)

    def remove_top_card(self):
        self.cards.pop(0)
