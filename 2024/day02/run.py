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
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 4)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def isGrowing(row):
    for i in range(len(row)-1):
        if row[i] >= row[i+1]:
            return False
    return True

def isDecreasing(row):
    for i in range(len(row)-1):
        if row[i] <= row[i+1]:
            return False
    return True


def isSafe(row):
    if not (isGrowing(row) or isDecreasing(row)):
        return False
    
    for i in range(len(row)-1):
        change = abs(row[i+1] - row[i])
        if change <= 0 or change > 3:
            return False

    return True

def task1(input):
    sum = 0
    for x in input:
        if isSafe(x):
            sum += 1
    return sum


def task2(input):
    sum = 0
    for x in input:
        if isSafe(x):
            sum += 1
            continue
        for y in range(len(x)):
            temp = x.copy()
            temp.pop(y)
            if isSafe(temp):
                sum += 1
                break
    return sum

def parse(input):
    a = []
    for line in input:
        temp = line.strip().split(' ')
        temp = [int(x) for x in temp]
        a.append(temp)
    return a


if __name__ == "__main__":
    # benchmark(main)
    main()
