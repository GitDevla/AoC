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
    test(is_valid("aa bb cc dd ee"), True)
    test(is_valid("aa bb cc dd aa"), False)
    test(is_valid("aa bb cc dd aaa"), True)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(is_valid2("abcde fghij"), True)
    test(is_valid2("abcde xyz ecdab"), False)
    test(is_valid2("a ab abc abd abf abj"), True)
    test(is_valid2("iiii oiii ooii oooi oooo"), True)
    test(is_valid2("oiii ioii iioi iiio"), False)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return len(list(filter(is_valid, input)))


def is_valid(input):
    s = set(input.split())
    return len(s) == len(input.split())


def is_valid2(input):
    s = set(["".join(sorted(x)) for x in input.split()])
    return len(s) == len(input.split())


def task2(input):
    return len(list(filter(is_valid2, input)))


if __name__ == "__main__":
    # benchmark(main)
    main()
