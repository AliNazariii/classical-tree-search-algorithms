class Card:
    def __init__(self, color: str, value: int):
        self.color: str = color
        self.value: int = value

    def __repr__(self):
        return f"{str(self.value)}{self.color}"

    def __eq__(self, card):
        return self.color == card.color and self.value == card.value
