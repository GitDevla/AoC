import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day19.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 6)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 16)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def canBeMade(towels, target):
    if len(target) == 0:
        return True
    for i in towels:
        if target.startswith(i):
            if canBeMade(towels, target[len(i):]):
                return True
    return False

def numberOfWays(towels, target, memo=None):
    if memo is None:
        memo = {}
    counter = 0
    if len(target) == 0:
        return 1
    if target in memo:
        return memo[target]
    for i in towels:
        if target.startswith(i):
            counter += numberOfWays(towels, target[len(i):], memo)
    memo[target] = counter
    return counter

def task1(input):
    towels, targets = input
    return sum([canBeMade(towels,target) for target in targets])


def task2(input):
    towels, targets = input
    return sum([numberOfWays(towels,target) for target in targets])

def parse(input):
    towels = input[0].split(", ");
    targets = input[2:]
    return (towels,targets)

if __name__ == "__main__":
    benchmark(main)
    # main()
