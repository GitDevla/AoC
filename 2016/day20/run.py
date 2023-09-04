import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day20.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ 5-8
            0-2
            4-7"""
    )
    test_input = parse(test_input)
    test(task1(test_input), 3)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ 5-8
            0-2
            4-7"""
    )
    test_input = parse(test_input)
    test(task2(test_input, 10), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)

    print(f"Task 2 solution: {task2(input,4294967295)}")


#########################################################


def task1(input):
    idx = 0
    while True:
        is_in = next((x for x in input if idx in x), None)
        if is_in:
            idx = is_in.stop
        else:
            return idx


def task2(input, max):
    idx = 0
    all = 0
    while idx < max:
        is_in = next((x for x in input if idx in x), None)
        if is_in:
            idx = is_in.stop
        else:
            all += 1
            idx += 1
    return all


def parse(input: str):
    ranges = []
    for l in input:
        split = list(map(int, l.split("-")))
        ranges.append(range(split[0], split[1] + 1))
    return ranges


if __name__ == "__main__":
    # benchmark(main)
    main()
