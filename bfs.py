from utils import get_input
from game.game_state import goal_test, expand
from game.space import Space, path


def BFS(space: Space):
    explored = []
    frontier = [space.states[0]]
    while True:
        if len(frontier) == 0:
            print("Empty frontier")
            break
        state = frontier.pop(0)
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
                    frontier.append(child)
                    space.add_state(child)


space = get_input()
BFS(space)
