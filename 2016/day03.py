from utils import *

FILE = "input/day03.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    arr = [[int(x) for x in l.split()] for l in input]
    sum = 0
    for s in arr:
        sum += int(is_triangle(s[0], s[1], s[2]))
    return sum


def task2(input):
    sum = 0
    for s in parse2(input):
        sum += int(is_triangle(s[0], s[1], s[2]))
    return sum


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def parse2(arr: str):
    text = []
    rows = arr
    index = 0
    while index < len(rows):
        part = rows[index : index + 3]
        part = [int(x) for l in part for x in l.split()]
        for l in range(3):
            text.append([part[0 + l], part[3 + l], part[6 + l]])
        index += 3

    return text


if __name__ == "__main__":
    # benchmark(main())
    main()
