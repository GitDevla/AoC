import re
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
    test(solve([x for x in "abcde"], ["s1", "x3/4", "pe/b"]), [x for x in "baedc"])

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    letters = [x for x in "abcdefghijklmnop"]
    instr = input.split(",")
    return "".join(solve(letters, instr))


def solve(letters: str, instr):
    for i in instr:
        if i[0] == "s":
            x = int(re.match(r"s(\d+)", i).group(1))
            letters = letters[x * -1 :] + letters[: x * -1]
        elif i[0] == "x":
            (aIdx, bIdx) = [int(x) for x in list(re.match(r"x(\d+)/(\d+)", i).groups())]
            a = letters[aIdx]
            b = letters[bIdx]
            letters[aIdx] = b
            letters[bIdx] = a
        elif i[0] == "p":
            (a, b) = re.match(r"p(\w+)/(\w+)", i).groups()
            aIdx = letters.index(a)
            bIdx = letters.index(b)
            letters[aIdx] = b
            letters[bIdx] = a
    return letters


def task2(input):
    letters = [x for x in "abcdefghijklmnop"]
    instr = input.split(",")
    loop = []
    i = 1_000_000_000
    while i > 0:
        letters = solve(letters, instr)
        if letters in loop:  # skip useless looping
            i -= (i // len(loop)) * len(loop)
            loop.clear()
        loop.append(letters)
        i -= 1
    return "".join(letters)


if __name__ == "__main__":
    # benchmark(main)
    main()
