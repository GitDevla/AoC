import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day07.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 21)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 40)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        out.append([*line])
    return out


def dfs(input, y, x):
    if y >= len(input):
        return 0
    if input[y][x] == "^":
        left = dfs(input, y - 1, x - 1)
        input[y][x] = left
        right = dfs(input, y - 1, x + 1)
        input[y][x] = right
        return 1 + left + right
    elif input[y][x] == ".":
        res = dfs(input, y + 1, x)
        input[y][x] = res
        return res
    else:
        return int(input[y][x])
    return 0


def task2(input):
    start = None
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "S":
                start = (y, x)
    input[start[0]][start[1]] = "."
    return dfs(input, start[0], start[1]) + 1


def task1(input):
    start = None
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "S":
                start = (y, x)
    queue = [start]
    res = 0
    while queue:
        y, x = queue.pop(0)
        ny, nx = y + 1, x
        if ny >= len(input) or nx < 0 or nx >= len(input[0]):
            continue

        if input[ny][nx] == "^":
            queue.append((ny - 1, nx + 1))
            queue.append((ny - 1, nx - 1))
            res += 1
        elif input[ny][nx] == ".":
            input[ny][nx] = "|"
            queue.append((ny, nx))
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
