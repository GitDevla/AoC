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
        """ cpy 41 a
            inc a
            inc a
            dec a
            jnz a 2
            dec a"""
    )
    test(task1(test_input), 42)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    return solve(registers, input)["a"]


def task2(input):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    return solve(registers, input)["a"]


def solve(registers, input):
    idx = 0
    input = [l.split(" ") for l in input]
    input = [[l[0], l[1], l[2] if len(l) == 3 else None] for l in input]  # speedup
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
                idx += int(b)
                continue
        idx += 1
    return registers


def get_value(value: str, registers):
    if value.isnumeric():
        return int(value)
    else:
        return registers[value]


if __name__ == "__main__":
    benchmark(main)
    # main()
