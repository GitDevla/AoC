import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day18.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ set a 1
            add a 2
            mul a a
            mod a 5
            snd a
            set a 0
            rcv a
            jgz a -1
            set a 1
            jgz a -2"""
    )
    test(task1(test_input), 4)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ snd 1
            snd 2
            snd p
            rcv a
            rcv b
            rcv c
            rcv d"""
    )
    test(task2(test_input), 3)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(instructions):
    p = Program(0, instructions)
    return p.execute_whole()


def task2(instructions):
    a = Program(0, instructions)
    b = Program(1, instructions)
    a.connected = b
    b.connected = a
    while not (a.interupt and b.interupt):
        a.step()
        b.step()
    return len(b.played_sounds)


class Program:
    def __init__(self, id, instructions) -> None:
        self.registers = {"p": id}
        self.instructions = instructions
        self.idx = 0
        self.played_sounds = []
        self.bus = []
        self.connected = None
        self.interupt = False

    def execute_whole(self):
        while self.idx < len(self.instructions):
            ret = self.step()
            if ret:
                return ret

    def step(self):
        l = self.instructions[self.idx]
        match = re.match(r"(\w+) (.) ?(.+)?", l)
        instr = match.group(1)
        fromm = match.group(2)
        to = match.group(3)
        if instr == "snd":
            self.played_sounds.append(self.get_value(fromm))
            if self.connected:
                self.connected.bus.append(self.get_value(fromm))
        elif instr == "set":
            self.registers[fromm] = self.get_value(to)
        elif instr == "add":
            self.registers[fromm] += self.get_value(to)
        elif instr == "mul":
            self.registers[fromm] *= self.get_value(to)
        elif instr == "mod":
            self.registers[fromm] %= self.get_value(to)
        elif instr == "rcv":
            if self.connected:
                if len(self.bus) == 0:
                    self.interupt = True
                    return
                self.interupt = False
                pop = self.bus.pop(0)
                self.registers[fromm] = pop
            else:
                if not self.get_value(fromm) == 0:
                    return self.played_sounds[-1]
        elif instr == "jgz":
            if self.get_value(fromm) > 0:
                self.idx += self.get_value(to)
                return
        self.idx += 1

    def get_value(self, value: str):
        if value.lstrip("-").isnumeric():
            return int(value)
        else:
            if not self.registers.get(value):
                self.registers[value] = 0
            return self.registers[value]


if __name__ == "__main__":
    # benchmark(main)
    main()
