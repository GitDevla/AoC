import re
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
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    test_input = parse(read_test(test_input))
    test(task1(test_input), 4277556)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    test_input = parse(read_test(test_input))
    test(task2(test_input), 3263827)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    return input


def task1(input):
    out = [[] for _ in range(len(input))]
    for line in input[:-1]:
        row = re.split(r"\s+", line.strip())
        for i, val in enumerate(row):
            if i >= len(out):
                out.append([])
            out[i].append(int(val))
    ops = re.split(r"\s+", input[-1].strip())
    for i, op in enumerate(ops):
        out[i] = (out[i], op)
    input = out
    res = 0
    for nums, op in input:
        if op == "+":
            res += sum(nums)
        elif op == "*":
            temp = 1
            for n in nums:
                temp *= n
            res += temp
    return res


def task2(input):
    out = []
    a = 0
    for i in range(len(input[0])):
        num = "".join([row[i] for row in input[:-1]])
        if num.strip() == "":
            a += 1
            continue
        if a >= len(out):
            out.append([])
        out[a].append(int(num))
    ops = re.split(r"\s+", input[-1].strip())
    for i, op in enumerate(ops):
        out[i] = (out[i], op)
    res = 0
    for nums, op in out:
        if op == "+":
            res += sum(nums)
        elif op == "*":
            temp = 1
            for n in nums:
                temp *= n
            res += temp
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
