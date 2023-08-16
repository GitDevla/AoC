from enum import Enum
from utils import *

FILE = "input/day02.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ULL
        RRDDD
        LURDL
        UUUUD"""
    )
    test(task1(test_input), "1985")

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ULL
        RRDDD
        LURDL
        UUUUD"""
    )
    test(task2(test_input), "5DB3")

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    return solve(input, keypad, [1, 1])


def task2(input):
    keypad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    return solve(input, keypad, [2, 0])


def solve(moves, keypad, starting_point):
    combination = ""
    current_pos = starting_point
    for line in moves:
        for move in line:
            dir = Direction[move].value
            new_pos = current_pos.copy()
            new_pos[0] += dir[0]
            new_pos[1] += dir[1]
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            if new_pos[0] >= keypad.__len__() or new_pos[1] >= keypad.__len__():
                continue
            if keypad[new_pos[0]][new_pos[1]] == None:
                continue
            current_pos = new_pos

        combination += keypad[current_pos[0]][current_pos[1]]
    return combination


class Direction(Enum):
    U = [-1, 0]
    R = [0, 1]
    D = [1, 0]
    L = [0, -1]


if __name__ == "__main__":
    # benchmark(main())
    main()
