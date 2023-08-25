import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day08.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution:")
    task2(input)


#########################################################


def task1(input):
    matrix = execute(input)
    return calc_lit(matrix)


def task2(input):
    matrix = execute(input)
    print_matrix(matrix)


def execute(instr):
    matrix = np.zeros((6, 50))
    for l in instr:
        split = l.split(" ")
        if split[0] == "rect":
            (a, b) = map(lambda x: int(x), split[1].split("x"))
            rect(matrix, a, b)
        elif split[0] == "rotate":
            i = int(split[2].split("=")[1])
            by = int(split[4])
            if split[1] == "row":
                rot_row(matrix, i, by)
            elif split[1] == "column":
                rot_col(matrix, i, by)
    return matrix


def rect(matrix, a, b):
    for x in range(a):
        for y in range(b):
            matrix[y][x] = True


def rot_col(matrix, x, by):
    height = len(matrix)
    temp = [False] * height
    for y in range(height):
        temp[(y + by) % height] = matrix[y][x]
    for y in range(height):
        matrix[y][x] = temp[y]


def rot_row(matrix, y, by):
    width = len(matrix[0])
    temp = [False] * width
    for x in range(width):
        temp[(x + by) % width] = matrix[y][x]
    for x in range(width):
        matrix[y][x] = temp[x]


def calc_lit(matrix):
    sum = 0
    for y in matrix:
        for x in y:
            sum += int(x)
    return sum


def print_matrix(matrix):
    for y in matrix:
        for x in y:
            print("█" if x else " ", end="")
        print()


if __name__ == "__main__":
    # benchmark(main)
    main()
