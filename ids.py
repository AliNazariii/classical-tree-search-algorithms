import copy
from utils import get_input
from game.game_state import goal_test, expand, GameState
from game.space import Space, path


def IDS(space: Space, max_depth: int):
    for i in range(max_depth):
        print(f"\ndepth: {i}")
        new_space: Space = copy.deepcopy(space)
        result = DLS(new_space, new_space.states[0], i)
        print(f"nodes: {len(new_space.states)}")
        if result:
            path(new_space, result)
            break


def DLS(space: Space, state: GameState, limit: int):
    if goal_test(space.n, space.m, state):
        return state
    elif limit == 0:
        return None
    else:
        children = expand(state, space.k)
        space.extend_states(children)
        for child in children:
            child_result = DLS(space, child, limit - 1)
            if child_result:
                return child_result


space = get_input()
IDS(space, 14)
