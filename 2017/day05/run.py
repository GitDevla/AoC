import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day05.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ 0
            3
            0
            1
            -3"""
    )
    test(task1(test_input), 5)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ 0
            3
            0
            1
            -3"""
    )
    test(task2(test_input), 10)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    instructions = [int(x) for x in input]
    steps = 0
    rip = 0
    while 0 <= rip and rip < len(instructions):
        instructions[rip] += 1
        rip += instructions[rip] - 1
        steps += 1
    return steps


def task2(input):
    instructions = [int(x) for x in input]
    steps = 0
    rip = 0
    while 0 <= rip and rip < len(instructions):
        if instructions[rip] >= 3:
            instructions[rip] -= 1
            rip += instructions[rip] + 1
        else:
            instructions[rip] += 1
            rip += instructions[rip] - 1
        steps += 1
    return steps


if __name__ == "__main__":
    # benchmark(main)
    main()
