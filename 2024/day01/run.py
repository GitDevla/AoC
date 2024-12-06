import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day01.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 11)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 31)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def parse(input):
    a=[]
    b=[]
    for line in input:
        temp = line.strip().split(' ')
        a.append(int(temp[0]))
        b.append(int(temp[-1]))
    return a, b

def task1(input):
    a,b = input
    a.sort()
    b.sort()
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i]-b[i])
    return sum


def task2(input):
    a,b = input
    sum= 0
    for i in range(len(a)):
        curr = a[i]
        count = len([x for x in b if x==curr])
        sum += curr*count
    return sum


if __name__ == "__main__":
    # benchmark(main)
    main()
