
from .card import Card
from .column import Column
from .game_state import GameState, determine_move


class Space:  # as graph
    def __init__(self, n, m, k):
        self.states = []
        self.n = n  # n is number of cards in each color
        self.m = m  # m is number of colors
        self.k = k  # k is the number of lists

    def add_state(self, state: GameState):
        self.states.append(state)

    def extend_states(self, states):
        self.states.extend(states)

    def print(self):
        depth = 0
        print(f"\n\ndepth: {depth}")
        for state in self.states:
            if state.depth != depth:
                depth = state.depth
                print(f"\ndepth: {state.depth}")
            print(state)


def path(space: Space, state: GameState):
    current_state = state
    path = []
    while current_state:
        path.insert(0, current_state)
        current_state = current_state.parent

    for i in range(len(path) - 1):
        print(determine_move(path[i], path[i + 1]))
