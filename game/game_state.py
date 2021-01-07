from .column import Column
import copy
from game.card import Card


class GameState:  # as graph node
    def __init__(self):
        self.columns = []
        self.parent: GameState = None
        self.depth: int = 0  # as G ---> actual cost
        self.h: int = 0

    def add_column(self, column):
        self.columns.append(column)

    def __repr__(self):
        columns = "----#----"
        for column in self.columns:
            columns += f"\n{str(column)}"
        columns += "\n----#----"
        return columns

    def increment_depth(self):
        self.depth += 1

    def set_parent(self, parent_state):
        self.parent = parent_state

    def __eq__(self, state):
        for column in self.columns:
            if column not in state.columns:
                return False
        return True

    def set_h(self, h):
        self.h = h


def goal_test(n: int, m: int, state: GameState) -> bool:
    columns = state.columns
    founded_m = 0
    for column in columns:
        if len(column) == n:
            cards = column.cards
            founded_m += 1
            color = cards[0].color
            for i in range(n):
                if i + 1 != cards[i].value or color != cards[i].color:
                    founded_m -= 1
                    break
    if founded_m == m:
        return True
    else:
        return False


def determine_move(src: GameState, dest: GameState) -> str:
    number_of_columns = len(src.columns)
    src_column_number = 0
    dest_column_number = 0
    for i in range(number_of_columns):
        src_column: Column = src.columns[i]
        dest_column: Column = dest.columns[i]
        if src_column != dest_column:
            if len(src_column) > len(dest_column):
                src_column_number = i
            elif len(src_column) < len(dest_column):
                dest_column_number = i

    return f"* {src.columns[src_column_number].cards[0]}: Column {src_column_number + 1} ---> Column {dest_column_number + 1}"


def expand(state: GameState, number_of_columns: int):
    children = []
    columns = state.columns
    for i in range(number_of_columns):
        if len(columns[i]) > 0:
            top_card: Card = (columns[i]).cards[0]
            for j in range(number_of_columns):
                if i != j:
                    new_state: GameState = copy.deepcopy(state)
                    new_columns = new_state.columns
                    if len(columns[j]) > 0:
                        dest_top_card: Card = (columns[j]).cards[0]
                        if top_card.value < dest_top_card.value:
                            new_columns[j].add_card(top_card)
                            new_columns[i].remove_top_card()

                            new_state.set_parent(state)
                            new_state.increment_depth()
                            children.append(new_state)
                    else:
                        new_columns[j].add_card(top_card)
                        new_columns[i].remove_top_card()

                        new_state.set_parent(state)
                        new_state.increment_depth()
                        children.append(new_state)
    return children
