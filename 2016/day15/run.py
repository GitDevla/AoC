import re
import sys
from pathlib import Path
from copy import deepcopy

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day15.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ Disc #1 has 5 positions; at time=0, it is at position 4.
            Disc #2 has 2 positions; at time=0, it is at position 1."""
    )
    test_input = parse(test_input)
    test(task1(test_input), 5)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(discs):
    start_time = 0
    while not went_through(discs, start_time):
        start_time += 1
    return start_time


def went_through(discs, starting_time):
    for sec in range(1, len(discs) + 1):
        if discs[sec - 1].position_at(starting_time + sec):
            return False
    return True


def task2(discs):
    discs.append(Disc(11, 0))
    return task1(discs)


def parse(input):
    reg = re.compile(
        r"Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)."
    )
    dicss = []
    for l in input:
        found = reg.search(l)
        pos = found.group(1)
        curr = found.group(2)
        dicss.append(Disc(pos, curr))
    return dicss


class Disc:
    def __init__(self, pos, curr):
        self.pos = int(pos)
        self.curr = int(curr)

    def position_at(self, time):
        return (self.curr + time) % self.pos


if __name__ == "__main__":
    # benchmark(main)
    main()
