from game.column import Column
from game.game_state import GameState
from game.space import Space
from game.card import Card


def get_input():
    k, m, n = map(int, input().split())

    space = Space(n, m, k)
    initial_state = GameState()

    for i in range(k):
        input_string = input()
        column = Column()
        if input_string != '#':
            for card in input_string.split():
                column.add_card(Card(card[-1], int(card[:-1])))
        initial_state.add_column(column)

    space.add_state(initial_state)
    return space
