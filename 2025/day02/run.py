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
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 1227775554)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 4174379265)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    input = input[0].split(",")
    for line in input:
        a, b = line.split("-")
        out.append((int(a), int(b)))
    return out


def task1(input):
    res = 0
    for a, b in input:
        invalid_ids_sum = is_invalid(a, b)
        res += invalid_ids_sum
    return res


def is_invalid(a, b):
    if len(str(a)) > 1:
        num = int(str(a)[0 : len(str(a)) // 2])
    else:
        num = 0
    sum = 0
    while int(str(num) + str(num)) < a:
        num += 1
    while int(str(num) + str(num)) <= b:
        real_num = int(str(num) + str(num))
        sum += real_num
        num += 1

    return sum


def is_invalid2(a, b):
    num = 1
    invalid = set()
    repMin = len(str(a)) // len(str(num))
    repMax = len(str(b)) // len(str(num)) + 1
    while repMin > 1:
        repMin = len(str(a)) // len(str(num))
        repMax = len(str(b)) // len(str(num)) + 1
        for rep in range(repMin, repMax + 1):
            real_num = int(str(num) * rep)
            if a <= real_num <= b:
                invalid.add(real_num)
        num += 1
    return sum(invalid)


def task2(input):
    res = 0
    for a, b in input:
        invalid_ids_sum = is_invalid2(a, b)
        res += invalid_ids_sum
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
