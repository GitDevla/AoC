import itertools
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day21.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ swap position 4 with position 0
            swap letter d with letter b
            reverse positions 0 through 4
            rotate left 1 step
            move position 1 to position 4
            move position 3 to position 0
            rotate based on position of letter b
            rotate based on position of letter d"""
    )
    test_input = parse(test_input)
    test(task1("abcde", test_input), "decab")
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1('abcdefgh',input)}")


def pt2():
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2('fbgdceah',input)}")


#########################################################


def task1(input, instr):
    input = list(input)
    for inst, args in instr:
        new = inst(input, args)
        input = new
    return "".join(input)


def task2(input, instr):
    letters = list(input)
    all_posibbilities = list(itertools.permutations(letters, len(letters)))
    for pos in all_posibbilities:
        if task1(pos, instr) == input:
            return "".join(pos)
    return input


def parse(input):
    output = []
    for l in input:
        if re.match(r"swap position (\d+) with position (\d+)", l):
            group = re.match(r"swap position (\d+) with position (\d+)", l).groups()
            output.append([swap_pos, tuple(map(int, group))])
        elif re.match(r"swap letter (\w+) with letter (\w+)", l):
            group = re.match(r"swap letter (\w+) with letter (\w+)", l).groups()
            output.append([swap_let, group])
        elif re.match(r"rotate (\w+) (\d+) step", l):
            group = re.match(r"rotate (\w+) (\d+) step", l).groups()
            output.append([rotate, (group[0], int(group[1]))])
        elif re.match(r"rotate based on position of letter (\w+)", l):
            group = re.match(r"rotate based on position of letter (\w+)", l).groups()
            output.append([rotate_based, group])
        elif re.match(r"reverse positions (\d+) through (\d+)", l):
            group = re.match(r"reverse positions (\d+) through (\d+)", l).groups()
            output.append([reverse, tuple(map(int, group))])
        elif re.match(r"move position (\d+) to position (\d+)", l):
            group = re.match(r"move position (\d+) to position (\d+)", l).groups()
            output.append([move, tuple(map(int, group))])
    return output


def swap_pos(input, arg):
    fromm = arg[0]
    to = arg[1]
    (input[fromm], input[to]) = (input[to], input[fromm])
    return input


def swap_let(input, arg):
    fromm = arg[0]
    to = arg[1]
    a = input.index(fromm)
    b = input.index(to)
    input[a] = to
    input[b] = fromm
    return input


def rotate(input, arg):
    dir = -1 if arg[0] == "left" else 1
    step = arg[1]
    new = list(input)
    for x in range(len(input)):
        new[(x + (step * dir)) % len(new)] = input[x]
    return new


def rotate_based(input, arg):
    letter = arg[0]
    idx = input.index(letter)
    if idx >= 4:
        idx += 1
    return rotate(input, ("right", idx + 1))


def reverse(input, arg):
    fromm = arg[0]
    to = arg[1] + 1
    before = input[:fromm]
    after = input[to:]
    center = input[fromm:to]
    combine = before + center[::-1] + after
    return combine


def move(input, arg):
    fromm = arg[0]
    to = arg[1]
    rem = input.pop(fromm)
    input.insert(to, rem)
    return input


if __name__ == "__main__":
    benchmark(main)
    # main()
