import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day13.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input ="""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    test_input = parse(read_test(test_input))
    test(find_minimal_price(test_input[0]), 280)
    test(find_minimal_price(test_input[1]), -1)
    test(task1(test_input), 480)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################
import math
def find_minimal_price(game):
    aButton, bButton, target = game
    a1 = aButton[0]
    b1 = bButton[0]
    c1 = target[0]

    a2 = aButton[1]
    b2 = bButton[1]
    c2 = target[1]
    det = a1 * b2 - a2 * b1
    if det == 0:
        return -1
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    if x < 0 or y < 0:
        return -1
    if x != round(x) or y != round(y):
        return -1
    return round(x*3+y)
    
   

def task1(input):
    sum = 0
    for game in input:
        price = find_minimal_price(game)
        if price != -1:
            sum += price    
    return sum


def task2(input):
    sum = 0
    for game in input:
        a,b,target = game
        target = (10000000000000+ target[0], 10000000000000+target[1])
        game = (a,b,target)
        price = find_minimal_price(game)
        if price != -1:
            sum += price    
    return sum

import re
def parse(input):
    raw = "\n".join(input)
    splitted = raw.split("\n\n")
    games = []
    for x in splitted:
        targetRegex = re.compile(r"Prize: X=([0-9]+), Y=([0-9]+)")
        aButtonRegex = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)")
        bButtonRegex = re.compile(r"Button B: X\+([0-9]+), Y\+([0-9]+)")
        target = targetRegex.search(x)
        aButton = aButtonRegex.search(x)
        bButton = bButtonRegex.search(x)
        target = (int(target.group(1)), int(target.group(2)))
        aButton = (int(aButton.group(1)), int(aButton.group(2)))
        bButton = (int(bButton.group(1)), int(bButton.group(2)))
        games.append((aButton, bButton,target))

    return games

if __name__ == "__main__":
    # benchmark(main)
    main()
