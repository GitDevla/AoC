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
    test(task1(1), 0)
    test(task1(12), 3)
    test(task1(23), 2)
    test(task1(1024), 31)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2(747), 806)

    # Solution
    input = int(read_file(FILE)[0])
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    i = 1
    radius = 0
    x = 0
    y = 0
    while i != input:
        steps = radius * 2

        for dy in range(steps - 1):
            y += 1
            i += 1
            if i == input:
                return abs(x) + abs(y)
        for dx in range(steps):
            x -= 1
            i += 1
            if i == input:
                return abs(x) + abs(y)
        for dy in range(steps):
            y -= 1
            i += 1
            if i == input:
                return abs(x) + abs(y)
        for dx in range(steps):
            x += 1
            i += 1
            if i == input:
                return abs(x) + abs(y)
        radius += 1
        x += 1
        i += 1
        if i == input:
            return abs(x) + abs(y)
    if i == input:
        return abs(x) + abs(y)


def task2(input):
    map = {(0, 0): 1}
    radius = 0
    x = 0
    y = 0
    while True:
        steps = radius * 2

        for dy in range(steps - 1):
            y += 1
            map[(x, y)] = suround(map, x, y)
            if map[(x, y)] > input:
                return map[(x, y)]
        for dx in range(steps):
            x -= 1
            map[(x, y)] = suround(map, x, y)
            if map[(x, y)] > input:
                return map[(x, y)]
        for dy in range(steps):
            y -= 1
            map[(x, y)] = suround(map, x, y)
            if map[(x, y)] > input:
                return map[(x, y)]
        for dx in range(steps):
            x += 1
            map[(x, y)] = suround(map, x, y)
            if map[(x, y)] > input:
                return map[(x, y)]
        radius += 1
        x += 1
        map[(x, y)] = suround(map, x, y)
        if map[(x, y)] > input:
            return map[(x, y)]


def suround(map, x, y):
    sum = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (x, y) == (0, 0):
                continue
            get = map.get((x + dx, y + dy))
            if get:
                sum += get
    return sum


if __name__ == "__main__":
    # benchmark(main)
    main()
