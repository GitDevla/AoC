import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day15.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_a = Generator(65, 16807, 4)
    test_b = Generator(8921, 48271, 8)
    test(task1((test_a, test_b)), 588)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_a = Generator(65, 16807, 4)
    test_b = Generator(8921, 48271, 8)
    test(task2((test_a, test_b)), 309)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(gens):
    (a, b) = gens
    judge = 0
    for _ in range(40_000_000):
        a.next()
        b.next()
        if a.lower16() == b.lower16():
            judge += 1
    return judge


def task2(gens):
    (a, b) = gens
    judge = 0
    for _ in range(5_000_000):
        a.next_criteria()
        b.next_criteria()
        if a.lower16() == b.lower16():
            judge += 1
    return judge


class Generator:
    IDK = 0x7FFFFFFF

    def __init__(self, value, factor, criteria) -> None:
        self.value = value
        self.factor = factor
        self.criteria = criteria

    def next(self):
        self.value = (self.value * self.factor) % self.IDK
        return self.value

    def next_criteria(self):
        self.value = self.next()
        if self.value % self.criteria == 0:
            return self.value
        return self.next_criteria()

    def lower16(self):
        return self.value & 0xFFFF


def parse(input: str):
    a_num = int(input[0].split(" ")[-1])
    b_num = int(input[1].split(" ")[-1])
    a = Generator(a_num, 16807, 4)
    b = Generator(b_num, 48271, 8)
    return (a, b)


if __name__ == "__main__":
    # benchmark(main)
    main()
