from functools import reduce
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day10.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(solve(5, [3, 4, 1, 5]), [3, 4, 2, 1, 0])

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(create_length("1,2,3"), [49, 44, 50, 44, 51, 17, 31, 73, 47, 23])
    test(hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), "40")
    test(task2(""), "a2582a3a0e66e6e86e3812dcb672a272")
    test(task2("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
    test(task2("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
    test(task2("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    input = [int(x) for x in input.split(",")]
    ans = solve(256, input)
    return ans[0] * ans[1]


def task2(input):
    input = create_length(input) * 64
    ret = solve(256, input)
    return hash(ret)


def solve(length, commands):
    xd = list(range(length))
    idx = 0
    skip = 0
    for c in commands:
        if c + idx > len(xd):
            start = xd[: (idx + c) % len(xd)]
            middle = xd[(idx + c) % len(xd) : idx]
            end = xd[idx:]
            temp = (end + start)[::-1]
            end = temp[: len(end)]
            start = temp[len(end) :]
            xd = start + middle + end
        else:
            start = xd[:idx]
            middle = xd[idx : c + idx]
            end = xd[c + idx :]
            xd = start + middle[::-1] + end
        idx = (idx + c + skip) % len(xd)
        skip += 1
    return xd


def create_length(input):
    return [ord(x) for x in input] + [17, 31, 73, 47, 23]


def hash(input):
    out = ""
    for block in range(len(input) // 16):
        decimal = reduce(lambda x, y: x ^ y, input[block * 16 : block * 16 + 16])
        out += f"{decimal:02x}"
    return out.strip()


if __name__ == "__main__":
    # benchmark(main)
    main()
