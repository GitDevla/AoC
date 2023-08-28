from enum import Enum
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day13.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1(10, 7, 4), 11)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 1 solution: {task1(input,31,39)}")


def pt2():
    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input, x, y):
    visited = []
    queue = [[1, 1, 0]]  # x,y,step
    while len(queue):
        curr = queue.pop(0)
        if curr[0] < 0:
            continue
        if curr[1] < 0:
            continue
        if is_wall(curr[0], curr[1], input):
            continue
        if [curr[0], curr[1]] in visited:
            continue
        if curr[0] == x and curr[1] == y:
            return curr[2]
        visited.append([curr[0], curr[1]])
        for i in Direction:
            next = curr.copy()
            next[0] += i.value[0]
            next[1] += i.value[1]
            next[2] += 1
            queue.append(next)


def task2(input):
    visited = []
    queue = [[1, 1, 0]]  # x,y,step
    while len(queue):
        curr = queue.pop(0)
        if curr[0] < 0:
            continue
        if curr[1] < 0:
            continue
        if is_wall(curr[0], curr[1], input):
            continue
        if [curr[0], curr[1]] in visited:
            continue
        if curr[2] > 50:
            continue
        visited.append([curr[0], curr[1]])
        for i in Direction:
            next = curr.copy()
            next[0] += i.value[0]
            next[1] += i.value[1]
            next[2] += 1
            queue.append(next)
    return len(visited)


def is_wall(x, y, salt):
    find = x * x + 3 * x + 2 * x * y + y + y * y
    find += salt
    binary = bin(find)
    ones = len([x for x in binary[1:] if x == "1"])
    return ones % 2 != 0


class Direction(Enum):
    Up = [-1, 0]
    Down = [1, 0]
    Left = [0, -1]
    Right = [0, 1]


if __name__ == "__main__":
    # benchmark(main)
    main()
