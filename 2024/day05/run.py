import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day05.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 143)

    # Solution
    input = read_file(FILE)
    input = parse(input)

    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 123)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def checkValidity(ordering, updates):
    curr = updates[-1]
    shouldntBe = ordering.get(curr, [])
    for i in range(len(updates)-2, -1, -1):
        if updates[i] in shouldntBe:
            return i
        
    return -1

def isValid(ordering, updates):
    for i in range(len(updates)):
        if checkValidity(ordering,updates[:i+1]) != -1:
            return False
    return True

def getCenterValue(updates):
    return updates[len(updates)//2]

def task1(input):
    (ordering, updates) = input
    return sum([getCenterValue(u) for u in updates if isValid(ordering, u)])


def fixOrdering(ordering, printers):
    i=0
    while i<len(printers):
        i+=1;
        failIndex = checkValidity(ordering, printers[:i+1])
        if failIndex != -1:
            printers[i],printers[failIndex] = printers[failIndex],printers[i]
            i = failIndex-1
        
    return printers

def task2(input):
    ordering, updates = input
    return sum([getCenterValue(fixOrdering(ordering,u)) for u in updates if not isValid(ordering, u)])

def parse(input):
    ordering = dict()
    updates = []
    seperatorIndex = input.index('')
    for line in input[:seperatorIndex]:
        line = [int(x) for x in line.split('|')]
        if line[0] not in ordering:
            ordering[line[0]] = set()
        ordering[line[0]].add(line[1])

    for line in input[seperatorIndex+1:]:
        line = [int(x) for x in line.split(',')]
        updates.append(line)
    return ordering,updates

if __name__ == "__main__":
    benchmark(main)
    # main()
