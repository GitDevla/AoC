import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day17.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    test_input = parse(read_test(test_input))
    test(task1(test_input),"4,6,3,5,6,3,5,2,1,0")

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    test_input = parse(read_test(test_input))
    # test(task2(test_input),117440)
    
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################
def combo_operand(register,combo):
    if combo <=3:
        return combo
    if combo == 4:
        return register[0]
    if combo == 5:
        return register[1]
    if combo == 6:
        return register[2]
    Exception("Invalid combo operand")
    

def run_program(registers,ops):
    instruction_counter = 0
    output = []
    while instruction_counter < len(ops):
        op = ops[instruction_counter]
        literal_op = ops[instruction_counter+1]
        combo = combo_operand(registers,literal_op)
        if op == 0:
            registers[0] = registers[0] // 2**combo
        elif op == 1:
            registers[1] = registers[1] ^ literal_op
        elif op == 2:
            registers[1] = combo % 8
        elif op == 3:
            if registers[0] != 0:
                instruction_counter = literal_op
                continue
        elif op == 4:
            registers[1] = registers[1] ^ registers[2]
        elif op == 5:
            output.append(combo%8)
        elif op == 6:
            registers[1] = registers[0] // 2**combo
        elif op == 7:
            registers[2] = registers[0] // 2**combo
        instruction_counter +=2
    return output

def task1(input):
    return ",".join(map(str,run_program(input[0],input[1])))


def find_program(registers,ops):
    first = registers[0]
    instruction_counter = 0
    output = []
    target = ops.copy()
    while instruction_counter < len(ops):
        op = ops[instruction_counter]
        literal_op = ops[instruction_counter+1]
        combo = combo_operand(registers,literal_op)
        if op == 0:
            registers[0] = registers[0] // 2**combo
        elif op == 1:
            registers[1] = registers[1] ^ literal_op
        elif op == 2:
            registers[1] = combo % 8
        elif op == 3:
            if registers[0] != 0:
                instruction_counter = literal_op
                continue
        elif op == 4:
            registers[1] = registers[1] ^ registers[2]
        elif op == 5:
            if len(target) == 0:
                return False
            asd = target.pop(0)
            if combo%8 != asd:
                return False
            # else:
            #     print(f"A:{first} {asd}")
        elif op == 6:
            registers[1] = registers[0] // 2**combo
        elif op == 7:
            registers[2] = registers[0] // 2**combo
        instruction_counter +=2
    return len(target) == 0

def task2(input):
    pass

def parse(input):
    A = int(input[0].split(": ")[1])
    B = int(input[1].split(": ")[1])
    C = int(input[2].split(": ")[1])
    program = list(map(int, input[4].split(": ")[1].split(",")))
    return [A, B, C], program

if __name__ == "__main__":
    # benchmark(main)
    main()