import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day08.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ b inc 5 if a > 1
            a inc 1 if b < 5
            c dec -10 if a >= 1
            c inc -20 if c == 10"""
    )
    test(task1(test_input), 1)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ b inc 5 if a > 1
            a inc 1 if b < 5
            c dec -10 if a >= 1
            c inc -20 if c == 10"""
    )
    test(task2(test_input), 10)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    comp = Computer(input)
    comp.execute()
    return max(comp.registers.values())


def task2(input):
    comp = Computer(input)
    comp.execute()
    return comp.highest_ever


class Computer:
    def __init__(self, instr) -> None:
        self.registers = {}
        self.instructions = instr
        self.highest_ever = 0

    def execute(self):
        regex = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+) (.+) (-?\d+)")
        for l in self.instructions:
            f = regex.search(l)
            (reg, command, value, left, comp, right) = f.groups(0)
            value = int(value)
            if self.eval_if(left, comp, right):
                if command == "dec":
                    value *= -1
                self.add(reg, value)
                if self.highest_ever < self.get(reg):
                    self.highest_ever = self.get(reg)

    def get(self, idx: str):
        if is_number(idx):
            return int(idx)
        f = self.registers.get(idx)
        if not f:
            return 0
        return f

    def add(self, idx, value):
        f = self.registers.get(idx)
        if not f:
            self.registers[idx] = 0
        self.registers[idx] += int(value)

    def eval_if(self, left, comp, right):
        return eval(f"{self.get(left)} {comp} {self.get(right)}")  # cry about it


def is_number(s):
    return bool(re.match(r"^-?\d+(?:\.\d+)?$", str(s)))


if __name__ == "__main__":
    # benchmark(main)
    main()
