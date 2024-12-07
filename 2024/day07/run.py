import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day07.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(canBeSolved(3267,[81,40,27]), True)
    test(canBeSolved(83,[17,5]), False)
    test_input="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    input = parse(read_test(test_input))
    test(task1(input), 3749)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    ops = [lambda x,y:x+y,lambda x,y:x*y,lambda x,y:int(f"{x}{y}")]
    test(canBeSolved(156,[15,6],ops), True)
    test(canBeSolved(7290,[6,8,6,15],ops), True)
    test_input="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    input = parse(read_test(test_input))
    test(task2(input), 11387)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def canBeSolved(target, nums,ops=[lambda x,y:x+y,lambda x,y:x*y],curr=0,i=1):
    if curr == 0:
        curr = nums[0]
        i = 1
    if curr == target:
        return True
    if curr > target:
        return False
    if i >= len(nums):
        return False

    nextNum = nums[i]
    for op in ops:
        if canBeSolved(target, nums,ops,op(curr,nextNum),i+1):
            return True
    return False


def task1(input):
    sum = 0
    for target,nums in input:
        if canBeSolved(target,nums):
            sum += target
    return sum


def task2(input):
    sum = 0
    for target,nums in input:
        if canBeSolved(target,nums,[lambda x,y:x+y,lambda x,y:x*y,lambda x,y:int(f"{x}{y}")]):
            sum += target
    return sum


def parse(input):
    equations = []
    for line in input:
        target,numbers = line.split(":")
        numbers = numbers.split(" ")
        numbers = [x for x in numbers if x != ""]
        numbers = [int(x) for x in numbers]
        equations.append((int(target),numbers))
    return equations

if __name__ == "__main__":
    benchmark(main)
    # main()
