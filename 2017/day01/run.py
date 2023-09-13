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
    test(task1("1122"), 3)
    test(task1("1111"), 4)
    test(task1("1234"), 0)
    test(task1("91212129"), 9)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("1212"), 6)
    test(task2("1221"), 0)
    test(task2("123425"), 4)
    test(task2("123123"), 12)
    test(task2("12131415"), 4)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    sum = 0
    input += input[0]
    for pair in zip(input[0:], input[1:]):
        if pair[0] == pair[1]:
            sum += int(pair[0])
    return sum


def task2(input):
    sum = 0
    offset = len(input) // 2
    for i, curr in enumerate(input):
        next = input[(i + offset) % len(input)]
        if curr == next:
            sum += int(curr)
    return sum


if __name__ == "__main__":
    benchmark(main)
    # main()
