import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day17.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1(3), 638)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(steps):
    idx = 0
    storm = [0]
    for _ in range(2017):
        idx = (idx + steps) % len(storm)
        storm.insert(idx + 1, len(storm))
        idx += 1
    return storm[idx + 1]


def task2(steps):
    idx = 0
    storm_len = 1
    after_zero = 0
    for _ in range(50_000_000):
        idx = (idx + steps) % storm_len + 1
        if idx == 1:
            after_zero = storm_len
        storm_len += 1
    return after_zero


if __name__ == "__main__":
    benchmark(main)
    # main()
