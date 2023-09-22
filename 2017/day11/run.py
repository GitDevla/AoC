from enum import Enum
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day11.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("ne,ne,ne"), 3)
    test(task1("ne,ne,sw,sw"), 0)
    test(task1("ne,ne,s,s"), 2)
    test(task1("se,sw,se,sw,sw"), 3)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    cmd = input.split(",")
    pos = Cord(0, 0)
    for c in cmd:
        dir = Direction[c].value
        pos += dir
    return int(pos.len())


def task2(input):
    cmd = input.split(",")
    pos = Cord(0, 0)
    farthest = 0
    for c in cmd:
        dir = Direction[c].value
        pos += dir
        if pos.len() > farthest:
            farthest = pos.len()
    return int(farthest)


class Cord:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def len(self):
        return abs(self.x) + abs(self.y)

    def __iadd__(self, other):
        return Cord(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"


class Direction(Enum):
    nw = Cord(-0.5, 0.5)
    n = Cord(0, 1)
    ne = Cord(0.5, 0.5)
    sw = Cord(-0.5, -0.5)
    s = Cord(0, -1)
    se = Cord(0.5, -0.5)


if __name__ == "__main__":
    # benchmark(main)
    main()
