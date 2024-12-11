import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day11.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(aggregate_input(parse("0 1 10 99 999"),1),7)
    test(task1(parse("125 17")), 55312)

    # Solution
    input = read_file(FILE)[0]
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = read_file(FILE)[0]
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################
cache = {}
def next_value(input):
    value = 0
    if input in cache:
        return cache[input]
    
    if input == 0:
        value = [1]
    elif (len(str(input))%2==0):
        value = [int(str(input)[:len(str(input))//2]), int(str(input)[len(str(input))//2:])]
    else:
        value = [input*2024]
    cache[input] = value
    return value

def single_iteration(input):
    dictionary = {}
    for k,v in input.items():
        for n in next_value(k):
            if n not in dictionary:
                dictionary[n] = 0
            dictionary[n] += v
    return dictionary


def aggregate_input(input,repeat):
    dictionary = {}
    for x in input:
        dictionary[x] = 1

    for _ in range(repeat):
        dictionary = single_iteration(dictionary)
    
    return sum(dictionary.values())

def task1(input):
    input = aggregate_input(input, 25)
    return input


def task2(input):
    input = aggregate_input(input, 75)
    return input

def parse(input):
    return [int(x) for x in input.split()]

if __name__ == "__main__":
    benchmark(main)
    # main()
