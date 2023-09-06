import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day22.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ Filesystem            Size  Used  Avail  Use%
            /dev/grid/node-x0-y0   10T    8T     2T   80%
            /dev/grid/node-x0-y1   11T    6T     5T   54%
            /dev/grid/node-x0-y2   32T   28T     4T   87%
            /dev/grid/node-x1-y0    9T    7T     2T   77%
            /dev/grid/node-x1-y1    8T    0T     8T    0%
            /dev/grid/node-x1-y2   11T    7T     4T   63%
            /dev/grid/node-x2-y0   10T    6T     4T   60%
            /dev/grid/node-x2-y1    9T    8T     1T   88%
            /dev/grid/node-x2-y2    9T    6T     3T   66%"""
    )
    test_input = parse(test_input)
    test(task2(test_input), 7)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    valid = 0
    for a in input:
        for b in input:
            if a.used > b.free():
                continue
            if a.used == 0:
                continue
            if a == b:
                continue
            valid += 1
    return valid


def task2(input):
    free_node = next(x for x in input if x.used == 0)
    max_x = max(i.x for i in input)
    global_target = get(input, (max_x, 0))
    desired_path = path_to(input, global_target.x, global_target.y, 0, 0)
    moves = 0
    while len(desired_path):
        current_target = desired_path.pop(0)
        from_open_to_target = path_to(
            input,
            free_node.x,
            free_node.y,
            current_target.x,
            current_target.y,
            [global_target],
        )
        moves += len(from_open_to_target)
        free_node = global_target
        free_node.used = 0
        global_target = current_target
        moves += 1  # open node switches with target node
    return moves


def path_to(input, ax, ay, bx, by, exceptions=[]):
    queue = [[get(input, (ax, ay)), []]]
    visited = []
    while len(queue):
        pop = queue.pop(0)
        curr, path = pop
        if curr in visited:
            continue
        if curr in exceptions:
            continue
        visited.append(curr)
        if curr.position() == (bx, by):
            return path
        for dx in [-1, 1]:
            next = get(input, (curr.x + dx, curr.y))
            if not next:
                continue
            if next.size < curr.used:
                continue
            queue.append([next, path + [next]])
        for dy in [-1, 1]:
            next = get(input, (curr.x, curr.y + dy))
            if not next:
                continue
            if next.size < curr.used:
                continue
            queue.append([next, path + [next]])


def get(input, pos):
    try:
        return next(i for i in input if i.position() == pos)
    except:
        return None


def parse(input):
    output = []
    for l in input:
        match = re.match(r"\/dev\/grid\/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T", l)
        if not match:
            continue
        (x, y, size, used) = match.groups(0)
        output.append(Node(x, y, size, used))
    return output


class Node:
    def __init__(self, x, y, size, used):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.used = int(used)

    def position(self):
        return (self.x, self.y)

    def free(self):
        return self.size - self.used

    def __repr__(self) -> str:
        return f"{self.x},{self.y}:  {self.used}T/{self.size}T"


if __name__ == "__main__":
    # benchmark(main)
    main()
