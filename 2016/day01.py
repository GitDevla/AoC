from enum import Enum
from utils import *

FILE = "input/day01.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("R2, L3"), 5)
    test(task1("R2, R2, R2"), 2)
    test(task1("R5, L5, R5, R3"), 12)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("R8, R4, R4, R8"), 4)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    split = input.split(", ")

    facing = 0
    distance = [0, 0]
    for command in split:
        rotate = command[0]
        step = int(command[1:])
        if rotate == "R":
            facing = (facing + 1) % 4
        elif rotate == "L":
            facing = (facing - 1) % 4
        for step in range(step):
            movement = list(Direction)[facing].value
            distance[0] += movement[0]
            distance[1] += movement[1]
    final_distance = abs(distance[0]) + abs(distance[1])
    return final_distance


def task2(input):
    split = input.split(", ")

    facing = 0
    distance = [0, 0]
    hashmap = {}
    for x in split:
        rotate = x[:1]
        step = x[1:]
        if rotate == "R":
            facing = (facing + 1) % 4
        elif rotate == "L":
            facing = (facing - 1) % 4
        for step in range(int(step)):
            key = hash(distance)
            if hashmap.get(key) == True:
                final_distance = abs(distance[0]) + abs(distance[1])
                return final_distance
            hashmap[key] = True
            movement = list(Direction)[facing].value
            distance[0] += movement[0]
            distance[1] += movement[1]


class Direction(Enum):
    North = [1, 0]
    East = [0, 1]
    South = [-1, 0]
    West = [0, -1]


def hash(lst):
    s = [str(i) for i in lst]
    return ",".join(s)


if __name__ == "__main__":
    main()
