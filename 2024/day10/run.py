import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day10.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    test_input = read_test(test_input)
    test_input = parse(test_input)
    test(task1(test_input), 36)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    
    test_input="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    test_input = read_test(test_input)
    test_input = parse(test_input)
    test(task2(test_input), 81)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def find_starts(input):
    starts = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                starts.append((i, j))
    return starts

def spearheads_reachable(input, startpos):
    queue = []
    queue.append(startpos)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    paths = set()

    while len(queue) > 0:
        y, x = queue.pop(0)
        for d in dirs:
            dy, dx = d
            currHeight = input[y][x]
            
            ny, nx = y + dy, x + dx
            if ny <0 or nx < 0 or ny >= len(input) or nx >= len(input[0]):
                continue
            if currHeight+1 != input[ny][nx]:
                continue
            if input[ny][nx] == 9:
                paths.add((ny, nx))
                continue
            queue.append((ny, nx))
    return len(paths)

def spearheads_paths(input, startpos):
    queue = []
    queue.append(startpos)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    paths = 0

    while len(queue) > 0:
        y, x = queue.pop(0)
        for d in dirs:
            dy, dx = d
            currHeight = input[y][x]
            
            ny, nx = y + dy, x + dx
            if ny <0 or nx < 0 or ny >= len(input) or nx >= len(input[0]):
                continue
            if currHeight+1 != input[ny][nx]:
                continue
            if input[ny][nx] == 9:
                paths += 1
                continue
            queue.append((ny, nx))
    return paths


def task1(input):
    starts = find_starts(input)
    summa = 0
    for start in starts:
        summa += spearheads_reachable(input, start)
    return summa

def task2(input):
    starts = find_starts(input)
    summa = 0
    for start in starts:
        summa += spearheads_paths(input, start)
    return summa

def parse(input):
    return [[int(x) if x != '.' else -1 for x in line] for line in input]


if __name__ == "__main__":
    # benchmark(main)
    main()
