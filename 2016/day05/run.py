from hashlib import md5 as hashlib_md5
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
    test(task1("abc"), "18f47a30")

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("abc"), "05ace8e3")

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    id = 0
    new_pass = []
    while len(new_pass) < 8:
        hash = md5(input + str(id))
        if hash[:5] == "00000":
            new_pass.append(hash[5])
        id += 1
    return "".join(new_pass)


def task2(input):
    id = -1
    new_pass = [None] * 8
    while not all([x != None for x in new_pass]):
        id += 1
        hash = md5(input + str(id))

        if hash[:5] == "00000":
            if not hash[5].isdigit():
                continue
            idx = int(hash[5])
            value = hash[6]
            if idx >= len(new_pass):
                continue
            if new_pass[idx] != None:
                continue
            new_pass[idx] = value

    return "".join(new_pass)


def md5(input):
    md5_hash = hashlib_md5()
    md5_hash.update(input.encode("utf-8"))
    return md5_hash.hexdigest()


if __name__ == "__main__":
    # benchmark(main)
    main()
