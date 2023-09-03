import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day18.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(solve("..^^.", 3), 6)
    test(solve(".^^.^.^^^^", 10), 38)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {solve(input,40)}")


def pt2():
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {solve(input,400000)}")


#########################################################


def solve(input, length):
    last_row = input
    sum = len(list(filter(lambda x: x == ".", last_row)))
    for _ in range(length - 1):
        next_row = ""
        last = "." + last_row + "."
        for x in range(len(input)):
            split = last[x : x + 3]
            is_tr = is_trap(split)
            next_row += "^" if is_tr else "."
        last_row = next_row
        sum += len(list(filter(lambda x: x == ".", last_row)))
    return sum


def is_trap(above):
    return above in ["^^.", ".^^", "^..", "..^"]


if __name__ == "__main__":
    # benchmark(main)
    main()
