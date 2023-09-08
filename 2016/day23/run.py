import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day23.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ cpy 2 a
            tgl a
            tgl a
            tgl a
            cpy 1 a
            dec a
            dec a"""
    )
    test(task1(test_input), 3)

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
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    return solve(registers, input)["a"]


def task2(input):
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    return solve(registers, input)["a"]


def solve(registers, input):
    idx = 0
    input = [l.split(" ") for l in input]
    input = [
        [l[0], l[1], l[2] if len(l) >= 3 else None, l[3] if len(l) >= 4 else None]
        for l in input
    ]  # speedup
    while idx < len(input):
        cmd, a, b, c = input[idx]
        if cmd == "cpy":
            registers[b] = get_value(a, registers)
        elif cmd == "inc":
            registers[a] += 1
        elif cmd == "dec":
            registers[a] -= 1
        elif cmd == "mul":
            registers[a] += get_value(b, registers) * get_value(c, registers)
        elif cmd == "jnz":
            if get_value(a, registers):
                idx += get_value(b, registers)
                continue
        elif cmd == "tgl":
            offset = get_value(a, registers)
            if idx + offset >= len(input):
                idx += 1
                continue
            if input[idx + offset][2]:
                if input[idx + offset][0] == "jnz":
                    input[idx + offset][0] = "cpy"
                else:
                    input[idx + offset][0] = "jnz"
            else:
                if input[idx + offset][0] == "inc":
                    input[idx + offset][0] = "dec"
                else:
                    input[idx + offset][0] = "inc"
                    # i miss pointers
        idx += 1
    return registers


def get_value(value: str, registers):
    if value.lstrip("-").isnumeric():
        return int(value)
    else:
        return registers[value]


if __name__ == "__main__":
    # benchmark(main)
    main()
