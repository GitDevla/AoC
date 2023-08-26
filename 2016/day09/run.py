import sys
from pathlib import Path
import re

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day09.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("ADVENT"), 6)
    test(task1("A(1x5)BC"), 7)
    test(task1("(3x3)XYZ"), 9)
    test(task1("A(2x2)BCD(2x2)EFG"), 11)
    test(task1("(6x1)(1x3)A"), 6)
    test(task1("X(8x2)(3x3)ABCY"), 18)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("(3x3)XYZ"), 9)
    test(task2("(27x12)(20x12)(13x14)(7x10)(1x12)A"), 241920)
    test(task2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"), 445)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return estimate_length(input, False)


def task2(input):
    return estimate_length(input, True)


def estimate_length(input: str, full_unzip: bool):
    found = re.search("\((\d+)x(\d+)\)", input)
    if not found:
        return len(input)
    span = int(found.group(1))
    times = int(found.group(2))
    start_idx = found.span()[0]
    end_idx = found.span()[1]
    repeat = times * (
        span
        if not full_unzip
        else estimate_length(input[end_idx : end_idx + span], full_unzip)
    )
    return (
        len(input[:start_idx])
        + repeat
        + estimate_length(input[end_idx + span :], full_unzip)
    )


if __name__ == "__main__":
    # benchmark(main)
    main()

"""
def     1126.6178s
new     0.0089s
"""


def decompress(input: str):
    found = re.search("\(\d+x\d+\)", input)
    if not found:
        return input
    (span, times) = [int(i) for i in found.group(0).strip(")").strip("(").split("x")]
    (fro, to) = found.span(0)
    after = input[to + span :]
    new = input[to : to + span] * times
    new += decompress(after)
    return input[0:fro] + new


def decompress2(input: str):
    working_set = input
    decompressed = ""
    while True:
        start_idx = working_set.find("(")
        end_idx = working_set.find(")") + 1
        if start_idx == -1:
            break
        (span, times) = [
            int(i) for i in working_set[start_idx + 1 : end_idx - 1].split("x")
        ]

        decompressed += working_set[:start_idx]

        after = working_set[end_idx + span :]
        new = working_set[end_idx : end_idx + span] * times
        working_set = new + after
    return decompressed + working_set
