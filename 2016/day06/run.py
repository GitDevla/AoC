import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day06.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ eedadn
            drvtee
            eandsr
            raavrd
            atevrs
            tsrnev
            sdttsa
            rasrtv
            nssdts
            ntnada
            svetve
            tesnvt
            vntsnd
            vrdear
            dvrsen
            enarar"""
    )
    test(task1(test_input), "easter")

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ eedadn
            drvtee
            eandsr
            raavrd
            atevrs
            tsrnev
            sdttsa
            rasrtv
            nssdts
            ntnada
            svetve
            tesnvt
            vntsnd
            vrdear
            dvrsen
            enarar"""
    )
    test(task2(test_input), "advent")

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return solve(input, False)


def task2(input):
    return solve(input, True)


def solve(input, is_min):
    input = rotate(input)
    output = []
    for row in input:
        hashmap = {}
        for c in row:
            if hashmap.get(c) == None:
                hashmap[c] = 0
            hashmap[c] += 1
        if is_min:
            most_common = max(hashmap.items(), key=lambda x: -x[1])[0]
        else:
            most_common = max(hashmap.items(), key=lambda x: x[1])[0]
        output.append(most_common)
    return "".join(output)


def rotate(matrix):
    output = []
    for col_idx in range(len(matrix[0])):
        temp = []
        for row_idx in range(len(matrix)):
            temp.append(matrix[row_idx][col_idx])
        output.append(temp)
    return output


if __name__ == "__main__":
    # benchmark(main)
    main()
