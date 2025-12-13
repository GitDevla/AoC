import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day04.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 13)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 43)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        out.append(["."] + [*line] + ["."])
    out = [["."] * len(out[0])] + out + [["."] * len(out[0])]
    return out


DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def task1(input):
    res = 0
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if input[i][j] == ".":
                continue
            occupied = 0
            for di, dj in DIRS:
                if input[i + di][j + dj] == "@":
                    occupied += 1
            if occupied < 4:
                res += 1
    return res


def task2(input):
    res = 0
    check = []
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if input[i][j] == "@":
                check.append((i, j))
    for i, j in check:
        if input[i][j] == ".":
            continue
        occupied = 0
        for di, dj in DIRS:
            if input[i + di][j + dj] == "@":
                occupied += 1
        if occupied < 4:
            res += 1
            input[i][j] = "."
            for di, dj in DIRS:
                if input[i + di][j + dj] == "@":
                    check.append((i + di, j + dj))
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
