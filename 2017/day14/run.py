import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *
from day10.run import task2 as knot_hash  ## they should do this more

FILE = "input/day14.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("flqrgnkx"), 8108)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("flqrgnkx"), 1242)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    sum = 0
    for row in range(128):
        new_input = knot_hash(f"{input}-{row}")
        hash = "".join([hex_to_bin(l) for l in new_input])
        ones = len([x for x in hash if x == "1"])
        sum += ones
    return sum


def task2(input):
    matrix = []
    for row in range(128):
        new_input = knot_hash(f"{input}-{row}")
        hash = "".join([hex_to_bin(l) for l in new_input])
        matrix.append(hash)

    x = defrag(matrix, 9)

    return x


def defrag(matrix: str, find):
    matrix = [["+" if c == "1" else " " for c in l] for l in matrix]
    group_id = 0
    for y, row in enumerate(matrix):
        for x, _ in enumerate(row):
            changed = bfs_search(matrix, y, x)

            if changed > 0:
                group_id += 1
    return group_id


def bfs_search(matrix, y, x):
    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]
    number_of_changes = 0
    queue = [(y, x)]
    while len(queue):
        pop = queue.pop(0)
        (curr_y, curr_x) = pop
        if (
            curr_x < 0
            or curr_y < 0
            or curr_y >= len(matrix)
            or curr_x >= len(matrix[0])
        ):
            continue
        if not matrix[curr_y][curr_x] == "+":
            continue
        matrix[curr_y][curr_x] = " "
        number_of_changes += 1
        for d in directions:
            queue.append([curr_y + d[0], curr_x + d[1]])
    return number_of_changes


def hex_to_bin(input):
    return bin(int(input, 16))[2:].zfill(4)


if __name__ == "__main__":
    # benchmark(main)
    main()
