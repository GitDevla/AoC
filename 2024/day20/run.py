import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day20.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    test_input = parse(read_test(test_input))
    # test(task1(test_input), 23)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def find_start(maze):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "S":
                return x, y
            
def find_end(maze):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "E":
                return x, y

def convert_maze(maze,start):
    maze = [[-1 if x == "#" else 0 for x in line]for line in maze]
    queue = [(start,0)]
    visited = set()
    while queue:
        pos, dist = queue.pop(0)
        maze[pos[1]][pos[0]] = dist
        visited.add(pos)
        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_pos = (pos[0]+move[0],pos[1]+move[1])
            if new_pos in visited:
                continue
            if maze[new_pos[1]][new_pos[0]] == -1:
                continue
            queue.append((new_pos,dist+1))
    return maze

def check_arround(maze,pos,size):
    values = []
    for y in range(pos[1] - size, pos[1] + size + 1):
        for x in range(pos[0] - (size - abs(pos[1] - y)), pos[0] + (size - abs(pos[1] - y)) + 1):
            if x < 0 or y < 0 or x >= len(maze[0]) or y >= len(maze):
                continue
            if maze[y][x] != -1:
                cost = abs(pos[0] - x) + abs(pos[1] - y)
                values.append(maze[y][x]+cost)
    return values

def treverse_maze(maze,start,end,cheat_size=2,target=None):
    queue = [(start,0)]
    visited = set()
    count = 0
    while queue:
        pos, dist = queue.pop(0)
        around = check_arround(maze,pos,cheat_size)
        for value in around:
            if value+dist <= target:
                count += 1
        visited.add(pos)
        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_pos = (pos[0]+move[0],pos[1]+move[1])
            if new_pos in visited:
                continue
            if maze[new_pos[1]][new_pos[0]] == -1:
                continue
            queue.append((new_pos,dist+1))
    return count



def task1(input):
    start = find_start(input)
    end = find_end(input)
    maze = convert_maze(input,end)
    length = max([max(x) for x in maze])
    return treverse_maze(maze,start,end,2,length-100)



def task2(input):
    start = find_start(input)
    end = find_end(input)
    maze = convert_maze(input,end)
    length = max([max(x) for x in maze])
    return treverse_maze(maze,start,end,20,length-100)

def parse(input):
    return [[x for x in line]for line in input]

if __name__ == "__main__":
    benchmark(main)
    # main()
