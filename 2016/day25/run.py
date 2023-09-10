import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day25.txt"


def main():
    pt1()


def pt1():
    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


#########################################################


def task1(input):
    a = 0
    while True:
        registers = {"a": a, "b": 0, "c": 0, "d": 0}
        if solve(registers, input):
            return a
        a += 1


def solve(registers, input):
    idx = 0
    out = 1
    precision = 10
    input = [l.split(" ") for l in input]
    input = [[l[0], l[1], l[2] if len(l) >= 3 else None] for l in input]  # speedup
    while idx < len(input):
        cmd, a, b = input[idx]
        if cmd == "cpy":
            registers[b] = get_value(a, registers)
        elif cmd == "inc":
            registers[a] += 1
        elif cmd == "dec":
            registers[a] -= 1
        elif cmd == "jnz":
            if get_value(a, registers):
                idx += get_value(b, registers)
                continue
        elif cmd == "out":
            if out == get_value(a, registers):
                return False
            out = get_value(a, registers)
            if precision <= 0:
                return True
            precision -= 1
        idx += 1


def get_value(value: str, registers):
    if is_number(value):
        return int(value)
    else:
        return registers[value]


def is_number(s):
    return bool(re.match(r"^-?\d+(?:\.\d+)?$", str(s)))


if __name__ == "__main__":
    benchmark(main)
    # main()
