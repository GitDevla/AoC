import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day12.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ 0 <-> 2
            1 <-> 1
            2 <-> 0, 3, 4
            3 <-> 2, 4
            4 <-> 2, 3, 6
            5 <-> 6
            6 <-> 4, 5"""
    )
    test_input = parse(test_input)
    test(task1(test_input), 6)

    # Solution
    input = read_file(FILE)
    input = parse(input)

    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ 0 <-> 2
            1 <-> 1
            2 <-> 0, 3, 4
            3 <-> 2, 4
            4 <-> 2, 3, 6
            5 <-> 6
            6 <-> 4, 5"""
    )
    test_input = parse(test_input)
    test(task2(test_input), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)

    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return len(traverse_group(input))


def task2(input):
    groups = 0
    while len(input):
        group = traverse_group(input)
        input = remove(input, group)
        groups += 1
    return groups


def remove(a, b):
    for x in b:
        a.remove(x)
    return a


def traverse_group(input):
    queue = [input[0]]
    visited = set([input[0]])
    while len(queue):
        curr = queue.pop(0)
        for x in curr.connected:
            if x in visited:
                continue
            visited.add(x)
            queue.append(x)
    return visited


def parse(input):
    regex = re.compile(r"(\d+) <-> (.+)")
    programs = []
    for l in input:
        f = regex.search(l)
        (id, raw_connected) = f.groups()
        programs.append(Program(id, raw_connected.split(", ")))
    for p in programs:
        new_next = []
        for asd in p.connected:
            if asd == p.id:
                continue
            new_next.append(next(x for x in programs if x.id == asd))
        p.connected = new_next
    return programs


class Program:
    def __init__(self, id, connected) -> None:
        self.id = id
        self.connected = connected

    def __repr__(self) -> str:
        return f"{self.id} <=> {self.connected}"


if __name__ == "__main__":
    # benchmark(main)
    main()
