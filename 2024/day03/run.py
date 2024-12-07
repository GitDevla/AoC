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
    test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    test_input = parse(read_test(test_input))
    test(task1(test_input), 161)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    test_input = parse(read_test(test_input))
    test(task2(test_input),48)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


import re

def task1(input):
    found = re.findall("(mul\([0-9]*,[0-9]*\))", input, re.IGNORECASE)
    sum = 0
    for i in found:
        temp = i.split('(')[1].split(')')[0].split(',')
        sum += int(temp[0])*int(temp[1])
    return sum


def task2(input):
    found =  re.findall("((mul\([0-9]*,[0-9]*\))|(do\(\))|(don't\(\)))", input, re.IGNORECASE)
    found = [x[0] for x in found]

    sum = 0
    enabled = True
    for i in found:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        elif enabled:
            temp = i.split('(')[1].split(')')[0].split(',')
            sum += int(temp[0])*int(temp[1])
    return sum

def parse(input):
    return "".join(input)

if __name__ == "__main__":
    benchmark(main)
    # main()
