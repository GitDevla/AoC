import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day16.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(generate_dragon("1", 3), "100")
    test(generate_dragon("0", 3), "001")
    test(generate_dragon("11111", 11), "11111000000")
    test(generate_dragon("111100001010", 25), "1111000010100101011110000")
    test(generate_cheksum("110010110100"), "100")
    test(solve("10000", 20), "01100")

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {solve(input,272)}")


def pt2():
    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {solve(input,35651584)}")


#########################################################


def solve(input, length):
    draging_deez_nuts = generate_dragon(input, length)
    return generate_cheksum(draging_deez_nuts)


def generate_dragon(input, length):
    if len(input) >= length:
        return input[:length]
    copy = "".join(["0" if i == "1" else "1" for i in input[::-1]])
    return generate_dragon(f"{input}0{copy}", length)


def generate_cheksum(input):
    cheksum = "".join(
        ["1" if x[0] == x[1] else "0" for x in zip(input[::2], input[1::2])]
    )
    if len(cheksum) % 2 == 1:
        return cheksum
    return generate_cheksum(cheksum)


if __name__ == "__main__":
    benchmark(main)
    # main()
