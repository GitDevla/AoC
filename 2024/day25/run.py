import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day25.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input= """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 3)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def convert(grid,search = "."):
    lock = [0]*len(grid[0])
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] ==search:
                lock[x] = y
                break
    return lock

def fits(key, lock):
    for kp,lp in zip(key,lock):
        if lp>kp:
            return False
    return True

def task1(input):
    locks = []
    keys = []
    for x in input:
        if x[0][0] == "#":
            locks.append(convert(x,"."))
        else:
            keys.append(convert(x,"#"))
    
    unique_fits = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                unique_fits += 1
    return unique_fits


def task2(input):
    pass

def parse(input):
    blocks = "\n".join(input).split("\n\n")
    return [[[x for x in line] for line in block.split("\n")] for block in blocks]

if __name__ == "__main__":
    benchmark(main)
    # main()
