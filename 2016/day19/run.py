import math
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
    test(task1(5), 3)
    test(task1(6), 5)
    test(task1(7), 7)
    test(task1(8), 1)
    test(task1(58), 53)
    test(task1(59), 55)
    test(task1(727), 431)
    test(task1(1000), 977)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2v2(5), 2)
    test(task2v2(6), 3)
    test(task2v2(7), 5)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 2 solution: {task2v2(input)}")


#########################################################


def task1(input):
    elves = list(range(1, input + 1))
    while len(elves) > 2:
        next = elves[::2]

        if len(next) * 2 != len(elves):
            elves = next
            elves.pop(0)
        else:
            elves = next
    return elves[0]


def task2(input):
    elves = list(range(1, input + 1))
    idx = -1
    while len(elves) > 1:
        idx = (idx + 1) if (idx + 1) < len(elves) else 0
        step = math.floor(len(elves) / 2)
        temove = (idx + step) % len(elves)
        elves.pop(temove)
    return elves[0]


def task2v2(input):
    # Not my Code https://pastebin.com/Zm7tLbAe
    from collections import deque

    v1 = deque(range(1, (input + 1) // 2 + 1))
    v2 = deque(range((input + 1) // 2 + 1, input + 1))

    while True:
        if len(v2) >= len(v1):
            v2.popleft()
            if not v2:
                return v1[0]
        else:
            v1.pop()
        v1.append(v2.popleft())
        v2.append(v1.popleft())


if __name__ == "__main__":
    # benchmark(main)
    main()
