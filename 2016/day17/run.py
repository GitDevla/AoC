import hashlib
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
    test(task1("ihgpwlah"), "DDRRRD")
    test(task1("kglvqrro"), "DDUDRLRRUDRD")
    test(task1("ulqzkmiv"), "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("ihgpwlah"), 370)
    test(task2("kglvqrro"), 492)
    test(task2("ulqzkmiv"), 830)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    queue = [[1, 1, input]]  # x,y, hash
    is_open = ["b", "c", "d", "e", "f"]
    while len(queue):
        curr = queue.pop(0)
        hash = md5(curr[2])[:4]
        if [curr[0], curr[1]] == [4, 4]:
            return curr[2][len(input) :]

        if 1 > curr[0] or curr[0] > 4 or 1 > curr[1] or curr[1] > 4:
            continue

        if hash[0] in is_open:
            queue.append([curr[0], curr[1] - 1, f"{curr[2]}U"])
        if hash[1] in is_open:
            queue.append([curr[0], curr[1] + 1, f"{curr[2]}D"])
        if hash[2] in is_open:
            queue.append([curr[0] - 1, curr[1], f"{curr[2]}L"])
        if hash[3] in is_open:
            queue.append([curr[0] + 1, curr[1], f"{curr[2]}R"])


def task2(input):
    queue = [[1, 1, input, 0]]  # x,y, hash
    valid_path = []
    is_open = ["b", "c", "d", "e", "f"]
    while len(queue):
        curr = queue.pop(0)
        hash = md5(curr[2])[:4]
        if [curr[0], curr[1]] == [4, 4]:
            valid_path.append(curr[3])
            continue

        if 1 > curr[0] or curr[0] > 4 or 1 > curr[1] or curr[1] > 4:
            continue

        if hash[0] in is_open:
            queue.append([curr[0], curr[1] - 1, f"{curr[2]}U", curr[3] + 1])
        if hash[1] in is_open:
            queue.append([curr[0], curr[1] + 1, f"{curr[2]}D", curr[3] + 1])
        if hash[2] in is_open:
            queue.append([curr[0] - 1, curr[1], f"{curr[2]}L", curr[3] + 1])
        if hash[3] in is_open:
            queue.append([curr[0] + 1, curr[1], f"{curr[2]}R", curr[3] + 1])
    return max(valid_path)


def md5(input):
    md5_hash = hashlib.md5()
    md5_hash.update(input.encode("utf-8"))
    return md5_hash.hexdigest()


if __name__ == "__main__":
    # benchmark(main)
    main()
