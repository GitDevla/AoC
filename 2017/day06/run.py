import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day06.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("0   2   7   0"), 5)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("0   2   7   0"), 4)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    state = [int(x) for x in input.split()]
    seen_states = []
    while state not in seen_states:
        seen_states.append(state.copy())
        blocks_to_move = max(state)
        current_idx = state.index(blocks_to_move)
        state[current_idx] = 0
        for x in range(1, blocks_to_move + 1):
            state[(current_idx + x) % len(state)] += 1
    return len(seen_states)


def task2(input):
    state = [int(x) for x in input.split()]
    seen_states = []
    while state not in seen_states:
        seen_states.append(state.copy())
        blocks_to_move = max(state)
        current_idx = state.index(blocks_to_move)
        state[current_idx] = 0
        for x in range(1, blocks_to_move + 1):
            state[(current_idx + x) % len(state)] += 1
    return len(seen_states) - seen_states.index(state)


if __name__ == "__main__":
    # benchmark(main)
    main()
