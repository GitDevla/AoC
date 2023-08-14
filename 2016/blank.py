from utils import *

FILE = "input/dayXX.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(1, 1)

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
    pass


def task2(input):
    pass


if __name__ == "__main__":
    # benchmark(main())
    main()
