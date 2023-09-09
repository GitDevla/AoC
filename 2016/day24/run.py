import itertools
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day24.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ ###########
            #0.1.....2#
            #.#######.#
            #4.......3#
            ###########"""
    )
    test_input = parse(test_input)
    test(task1(test_input), 14)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    _, targets = input
    costs = generate_costs(input)
    start = targets.pop(0)
    paths = itertools.permutations(targets, len(targets))
    fastest = 99999999
    for path in paths:
        path = [start] + list(path)
        price = 0
        for pair in pairs(path):
            curr_node, next_node = pair
            price += costs[f"{curr_node[0]}:{next_node[0]}"]
            if fastest <= price:
                break
        if fastest > price:
            fastest = price
    return fastest


def task2(input):
    _, targets = input
    costs = generate_costs(input)
    start = targets.pop(0)
    paths = itertools.permutations(targets, len(targets))
    fastest = 99999999
    for path in paths:
        path = [start] + list(path)
        price = 0
        for pair in pairs(path):
            curr_node, next_node = pair
            price += costs[f"{curr_node[0]}:{next_node[0]}"]
            if fastest <= price:
                break
        if fastest > price:
            fastest = price
    return fastest


def pairs(input):
    pairs = []
    for i in range(len(input) - 1):
        pairs.append((input[i], input[i + 1]))
    return pairs


def generate_costs(input):
    walls, targets = input
    paths = itertools.combinations(targets, 2)
    costs = {}
    for x in paths:
        path = path_to(walls, x[0][1][0], x[0][1][1], x[1][1][0], x[1][1][1])
        costs[f"{x[0][0]}:{x[1][0]}"] = path
        costs[f"{x[1][0]}:{x[0][0]}"] = path
    return costs


def path_to(walls, ax, ay, bx, by):
    queue = [[(ax, ay), 0]]
    visited = []
    while len(queue):
        pop = queue.pop(0)
        curr, steps = pop
        if curr in visited:
            continue
        visited.append(curr)
        if curr == (bx, by):
            return steps
        for dx in [-1, 1]:
            next = (curr[0] + dx, curr[1])
            if walls[next[1]][next[0]]:
                continue
            queue.append([next, steps + 1])
        for dy in [-1, 1]:
            next = (curr[0], curr[1] + dy)
            if walls[next[1]][next[0]]:
                continue
            queue.append([next, steps + 1])


def parse(input):
    map = [[char == "#" for char in row] for row in input]
    targets = [
        (int(char), (x, y))
        for y, row in enumerate(input)
        for x, char in enumerate(row)
        if char.isnumeric()
    ]
    return (map, targets)


if __name__ == "__main__":
    # benchmark(main)
    main()
