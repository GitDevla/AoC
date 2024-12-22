import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day22.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """1
10
100
2024"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 37327623)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """1
2
3
2024"""
    test_input = parse(read_test(test_input))
    test(find_best_pattern(test_input), ((-2, 1, -1, 3),23))

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

SECRET_MODULO = 2**24-1
def next_secret_number(number):
    number ^= (number << 6) & SECRET_MODULO
    number ^= (number >> 5)
    number ^= (number << 11) & SECRET_MODULO
    return number

def n_th_secret_number(number,n):
    for i in range(n):
        number = next_secret_number(number)
    return number


def find_best_pattern(input):
    pre_calc = {}
    for i in input:
        pre_calc[i] = [[],[]]
        prev = i
        for _ in range(2000):
            next = next_secret_number(prev)
            prev = prev % 10
            curr = next % 10
            change = curr - prev
            prev = next
            pre_calc[i][0].append(change)
            pre_calc[i][1].append(curr)

    all_diffs = [x for p in pre_calc.values() for x in p[0]]
    unique_diffs = set()
    i = 0
    while i < len(all_diffs)-4:
        unique_diffs.add(tuple(all_diffs[i:i+4]))
        i += 1
    patterns = unique_diffs
    patterns = [p for p in patterns if sum(p) > 2]

    global_patterns = {}
    for nums in pre_calc:
        diff,values = pre_calc[nums]
        patterns = {}
        for i in range(len(diff)-4):
            patt = tuple(diff[i:i+4])
            val = values[i+3]
            if patt in patterns:
                continue
            patterns[patt] = val
        for p in patterns:
            if p in global_patterns:
                global_patterns[p] += patterns[p]
            else:
                global_patterns[p] = patterns[p]

    best = max(global_patterns,key=global_patterns.get)
    return  (best,global_patterns[best])

def task1(input):
    sum = 0
    for i in input:
        sum += n_th_secret_number(i,2000)
    return sum


def task2(input):
    return find_best_pattern(input)[1]


def parse(input):
    return [int(i) for i in input]


if __name__ == "__main__":
    benchmark(main)
    # main()
