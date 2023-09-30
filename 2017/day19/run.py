from enum import Enum
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day19.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = [
        "     |          ",
        "     |  +--+    ",
        "     A  |  C    ",
        " F---|----E|--+ ",
        "     |  |  |  D ",
        "     +B-+  +--+ ",
        "                ",
    ]
    test(task1(test_input), "ABCDEF")

    # Solution
    input = read_file_raw(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = [
        "     |          ",
        "     |  +--+    ",
        "     A  |  C    ",
        " F---|----E|--+ ",
        "     |  |  |  D ",
        "     +B-+  +--+ ",
        "                ",
    ]
    test(task2(test_input), 38)

    # Solution
    input = read_file_raw(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return solve(input)[0]


def solve(input):
    output = []
    current_face_idx = 0
    find_start = input[0].index("|")
    current_pos = Cord(find_start, 0)

    steps_taken = 1
    next_pos = current_pos + Direction.get(current_face_idx)
    while input[next_pos.y][next_pos.x] != " ":
        next = input[next_pos.y][next_pos.x]
        steps_taken += 1
        if next == "+":
            one = (current_face_idx + 1) % 4
            two = (current_face_idx + 3) % 4
            pos_one = next_pos + Direction.get(one)
            pos_two = next_pos + Direction.get(two)

            if input[pos_one.y][pos_one.x] != " ":
                next_pos = pos_one
                current_face_idx = one
                continue
            if input[pos_two.y][pos_two.x] != " ":
                next_pos = pos_two
                current_face_idx = two
                continue
        elif next not in ["|", "-"]:
            output.append(next)
        next_pos = next_pos + Direction.get(current_face_idx)
    return ("".join(output), steps_taken)


def task2(input):
    return solve(input)[1]


class Cord:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def len(self):
        return abs(self.x) + abs(self.y)

    def __iadd__(self, other):
        return Cord(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return Cord(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"


class Direction(Enum):
    down = Cord(0, 1)
    right = Cord(1, 0)
    up = Cord(0, -1)
    left = Cord(-1, 0)

    def get(idx):
        return list(Direction)[idx].value


if __name__ == "__main__":
    # benchmark(main)
    main()
