import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day01.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 3)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 6)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    a = []
    for line in input:
        rot = line[0]
        deg = line[1:]
        a.append((rot, int(deg)))
    return a


def task1(input):
    curr = 50
    res = 0
    for rot, deg in input:
        if rot == "L":
            curr -= deg
        else:
            curr += deg
        curr %= 100
        if curr == 0:
            res += 1
    return res


def task2(input):
    curr = 50
    res = 0
    for rot, deg in input:
        res += deg // 100  # full cycles
        deg %= 100
        prevcurr = curr
        if rot == "L":
            curr -= deg
        else:
            curr += deg
        if prevcurr != 0 and (curr <= 0 or curr >= 100):
            res += 1
        curr %= 100
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
