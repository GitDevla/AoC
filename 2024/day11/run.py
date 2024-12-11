import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day11.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(transform_input(parse("0 1 10 99 999"),1),[1, 2024, 1, 0, 9, 9, 2021976])
    test(task1(parse("125 17")), 55312)

    # Solution
    input = read_file(FILE)[0]
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)[0]
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def transform_input(input,repeat):
    for i in range(repeat):
        output = []
        for x in input:
            if x == 0:
                output.append(1)
            elif (len(str(x))%2==0):
                output.append(int(str(x)[:len(str(x))//2]))
                output.append(int(str(x)[len(str(x))//2:]))
            else:
                output.append(x*2024)
        input = output
        print(i)
    return input

def task1(input):
    input = transform_input(input, 25)
    return len(input)


def task2(input):
    input = transform_input(input, 75)
    return len(input)

def parse(input):
    return [int(x) for x in input.split()]

if __name__ == "__main__":
    # benchmark(main)
    main()
