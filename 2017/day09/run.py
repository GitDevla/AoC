import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day09.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1(r"{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
    test(task1(r"{{{},{},{{}}}}"), 16)
    test(task1(r"{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2(r"<random characters>"), 17)
    test(task2(r"<{!>}>"), 2)
    test(task2(r"<!!!>>"), 0)
    test(task2(r"<{o'i!a,<{i<a>"), 10)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return solve(input)[0]


def task2(input):
    return solve(input)[1]


def solve(input):
    score = 0
    garbage = 0
    group_indent = 0
    inside_garbage = False
    ignore_next = False
    for c in input:
        if ignore_next:
            ignore_next = False
            continue
        if c == ">":
            inside_garbage = False
            continue
        if c == "<":
            if inside_garbage:
                garbage += 1
            inside_garbage = True
            continue
        if c == "!":
            ignore_next = True
            continue
        if inside_garbage == True:
            garbage += 1
            continue
        if c == "{":
            group_indent += 1
        if c == "}":
            score += group_indent
            group_indent -= 1
    return (score, garbage)


if __name__ == "__main__":
    # benchmark(main)
    main()
