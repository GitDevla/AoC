import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day02.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ 5 1 9 5
            7 5 3
            2 4 6 8"""
    )
    test(task1(test_input), 18)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ 5 9 2 8
            9 4 7 3
            3 8 6 5"""
    )
    test(task2(test_input), 9)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input: str):
    cheksum = 0
    for row in input:
        nums = [int(x) for x in row.split()]
        cheksum += max(nums) - min(nums)
    return cheksum


def task2(input):
    cheksum = 0
    for row in input:
        nums = [int(x) for x in row.split()]
        pair = evenly_divisible_pair(nums)
        cheksum += pair[1] // pair[0]
    return cheksum


def evenly_divisible_pair(nums):
    for i, x in enumerate(nums):
        for y in nums[i + 1 :]:
            if x % y == 0:
                return (y, x)
            if y % x == 0:
                return (x, y)


if __name__ == "__main__":
    # benchmark(main)
    main()
