import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *
import re

FILE = "input/day10.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ value 5 goes to bot 2
            bot 2 gives low to bot 1 and high to bot 0
            value 3 goes to bot 1
            bot 1 gives low to output 1 and high to bot 0
            bot 0 gives low to output 2 and high to output 0
            value 2 goes to bot 2"""
    )
    test_input = parse(test_input)
    test(task1(test_input, 2, 5), 2)

    # # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input,17,61)}")


def pt2():
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    instruction_re = re.compile(
        r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"
    )
    assign_re = re.compile(r"value (\d+) goes to bot (\d+)")
    robots = {}
    for l in input:
        is_assign = assign_re.search(l)
        if is_assign:
            id = int(is_assign.group(2))
            value = int(is_assign.group(1))
            exist = robots.get(id)
            if not exist:
                robots[id] = Robot(id)
            robots[id].append(value)
        else:
            is_instruction = instruction_re.search(l)
            id = int(is_instruction.group(1))
            low_id = int(is_instruction.group(3))
            high_id = int(is_instruction.group(5))
            if is_instruction.group(2) == "output":
                low_id = (low_id + 1) * -1
            if is_instruction.group(4) == "output":
                high_id = (high_id + 1) * -1

            if not robots.get(id):
                robots[id] = Robot(id)
            if not robots.get(low_id):
                robots[low_id] = Robot(low_id)
            if not robots.get(high_id):
                robots[high_id] = Robot(high_id)
            robots[id].low_to_id = low_id
            robots[id].high_to_id = high_id
    return robots


def task1(input, find1, find2):
    while True:
        curr = next(i for i in input.values() if len(i.inventory) == 2)
        inv = curr.inventory
        inv.sort()
        if inv == [find1, find2]:
            return curr.id
        curr.execute(input)


def task2(input):
    while True:
        curr = next(i for i in input.values() if len(i.inventory) == 2)
        curr.execute(input)
        if input[-1].inventory and input[-2].inventory and input[-3].inventory:
            return (
                input[-1].inventory[0] * input[-2].inventory[0] * input[-3].inventory[0]
            )


class Robot:
    def __init__(self, id) -> None:
        self.id = id
        self.inventory = []
        self.low_to_id = 0
        self.high_to_id = 0

    def append(self, value):
        self.inventory.append(value)

    def execute(self, robots):
        if self.id < 0:
            return
        if len(self.inventory) != 2:
            return
        robots[self.low_to_id].append(self.get_low())
        robots[self.high_to_id].append(self.get_high())

    def get_low(self):
        self.inventory.sort()
        try:
            value = self.inventory.pop(0)
            return value
        except:
            return None

    def get_high(self):
        self.inventory.sort()
        try:
            value = self.inventory.pop()
            return value
        except:
            return None

    def __str__(self):
        return f"({self.id}: {self.inventory})"

    def __repr__(self):
        return f"({self.id}: {self.inventory})"


if __name__ == "__main__":
    benchmark(main)
    # main()
