import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day05.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 3)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 14)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    ranges = []
    ingridients = []
    split = input.index("")
    for line in input[:split]:
        a, b = line.strip().split("-")
        ranges.append((int(a), int(b)))
    for line in input[split + 1 :]:
        ingridients.append(int(line.strip()))
    return ranges, ingridients


def task1(input):
    ranges, ingridients = input
    res = 0
    for ingridient in ingridients:
        for a, b in ranges:
            if a <= ingridient <= b:
                res += 1
                break
    return res


def compress_ranges(ranges):
    changed = True
    while changed:
        changed = False
        new_ranges = []
        ranges = sorted(ranges)
        skip = False
        for i in range(len(ranges)):
            if skip:
                skip = False
                continue
            a, b = ranges[i]
            if i + 1 < len(ranges):
                a2, b2 = ranges[i + 1]
                if a2 <= b + 1:
                    new_ranges.append((a, max(b, b2)))
                    changed = True
                    skip = True
                else:
                    new_ranges.append((a, b))
            else:
                new_ranges.append((a, b))
        ranges = new_ranges
    return ranges


def task2(input):
    ranges, _ = input
    ranges = compress_ranges(ranges)
    res = 0
    for a, b in ranges:
        res += b - a + 1
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
