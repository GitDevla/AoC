import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day03.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(best_joltage("987654321111111"), 98)
    test(best_joltage("811111111111119"), 89)
    test(best_joltage("234234234234278"), 78)
    test(best_joltage("818181911112111"), 92)

    test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 357)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(best_joltage("987654321111111", 12), 987654321111)
    test(best_joltage("811111111111119", 12), 811111111119)
    test(best_joltage("234234234234278", 12), 434234234278)
    test(best_joltage("818181911112111", 12), 888911112111)

    test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 3121910778619)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        out.append(line.strip())
    return out


def task1(input):
    res = 0
    for batteries in input:
        best = best_joltage(batteries)
        res += best
    return res


def best_joltage(batteries, n=2):
    best = [0] * n
    for idx, jolt_str in enumerate(batteries):
        jolt = int(jolt_str)
        for i in range(n):
            if jolt > best[i]:
                if idx < len(batteries) - (n - 1 - i):
                    best = best[:i] + [jolt] + [0] * (n - i - 1)
                    break
    return int("".join([str(i) for i in best]))


def task2(input):
    res = 0
    for batteries in input:
        best = best_joltage(batteries, 12)
        res += best
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
