from utils import get_input
from game.game_state import goal_test, expand, GameState
from game.space import Space, path
import math


def find_min_cost(frontier) -> int:
    min_cost = math.inf
    min_state = 0
    for i in range(len(frontier)):
        cost = frontier[i].h + frontier[i].depth
        if cost < min_cost:
            min_cost = cost
            min_state = i
    return min_state


def calc_heuristic(state: GameState, n: int) -> int:
    h = 0
    for column in state.columns:
        if len(column.cards) > 0:
            length = len(column.cards)
            if column.cards[length - 1].value != length:
                h += 1
    return h


def A_star(space: Space):
    explored = []
    frontier = [space.states[0]]
    while True:
        if len(frontier) == 0:
            print("Empty frontier")
            break
        state = frontier.pop(find_min_cost(frontier))
        explored.append(state)
        if goal_test(space.n, space.m, state) == True:
            print(f"\ndepth: {state.depth}")
            path(space, state)
            print(f"explored nodes: {len(explored)}")
            print(f"nodes: {len(space.states)}")
            break
        else:
            children = expand(state, space.k)
            for child in children:
                if child not in frontier and child not in explored:
                    h = calc_heuristic(child, space.n)
                    child.set_h(h)

                    frontier.append(child)
                    space.add_state(child)


space = get_input()
A_star(space)
